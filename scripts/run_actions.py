"""Run the digest with an AI preflight and downloadable source evidence."""

import asyncio
from collections import Counter
from datetime import datetime, timedelta, timezone
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
import httpx
from src.ai.client import create_ai_client
from src.models import SourceType
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager
from src.scrapers.twitter import TwitterScraper


def normalize_base_url(value):
    parsed = urlsplit(value.strip().rstrip('/'))
    if parsed.scheme not in ('http', 'https') or not parsed.netloc:
        raise ValueError('HORIZON_AI_BASE_URL must be an HTTP(S) API base URL')
    if parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise ValueError('API base URL must not contain credentials, a query, or a fragment')
    path = parsed.path.rstrip('/')
    if path.endswith('/chat/completions'):
        path = path[:-len('/chat/completions')]
    if not path or re.fullmatch(r'/proxy/[^/]+', path):
        path += '/v1'
    return urlunsplit((parsed.scheme, parsed.netloc, path, '', ''))


def save_json(filename, value):
    output = Path('data/run-evidence')
    output.mkdir(parents=True, exist_ok=True)
    (output / filename).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8'
    )


def save_x_posts(posts):
    output = Path('data/run-evidence')
    output.mkdir(parents=True, exist_ok=True)
    lines = ['# 本次抓取的 X 帖子', '', f'共 {len(posts)} 条；这是原始采集结果，尚未按 AI 分数筛选。', '']
    for item in posts:
        lines.extend([
            f'## {item.author or "unknown"} (@{item.metadata.get("screen_name", "unknown")})', '',
            f'发布时间：{item.published_at.isoformat()}', '',
            str(item.url), '', item.content or item.title, '',
        ])
    (output / 'x-posts.md').write_text('\n'.join(lines), encoding='utf-8')


async def inspect_apify(config):
    """Read existing results without starting another Actor or calling AI."""
    twitter = config.sources.twitter
    headers = {'Authorization': 'Bearer ' + os.environ[twitter.apify_token_env]}
    report, posts = [], {}
    since = datetime.now(timezone.utc) - timedelta(hours=24)
    async with httpx.AsyncClient(base_url='https://api.apify.com/v2', headers=headers, timeout=30) as client:
        response = await client.get(f'/acts/{twitter.actor_id}/runs', params={'desc': 'true', 'limit': 5})
        response.raise_for_status()
        scraper = TwitterScraper(twitter, client)
        for run in response.json()['data']['items']:
            record = {key: run.get(key) for key in ('id', 'status', 'startedAt', 'statusMessage')}
            store_id = run.get('defaultKeyValueStoreId')
            if store_id:
                output = await client.get(f'/key-value-stores/{store_id}/records/OUTPUT')
                if output.status_code == 200:
                    result = output.json()
                    record['outcome'] = result.get('outcome')
                    record['message'] = result.get('message')
            dataset = run.get('defaultDatasetId')
            if dataset and run['status'] == 'SUCCEEDED':
                data = await client.get(f'/datasets/{dataset}/items', params={'limit': 100})
                data.raise_for_status()
                rows = data.json()
                record['dataset_rows'] = len(rows)
                parsed_items = []
                for row in rows:
                    item = scraper._parse_item(row, datetime.min.replace(tzinfo=timezone.utc))
                    if item:
                        parsed_items.append(item)
                        if item.published_at >= since:
                            posts[item.id] = item
                record['valid_rows'] = len(parsed_items)
                record['recent_rows'] = sum(item.published_at >= since for item in parsed_items)
                record['latest_post'] = max(
                    (item.published_at.isoformat() for item in parsed_items), default=None
                )
            report.append(record)
    save_json('apify-runs.json', report)
    ordered = sorted(posts.values(), key=lambda item: item.published_at, reverse=True)
    save_json('recovered-x-items.json', [item.model_dump(mode='json') for item in ordered])
    save_x_posts(ordered)
    for run in report:
        print('Existing Apify run:', json.dumps(run, ensure_ascii=False), flush=True)
    print(f'Exported {len(ordered)} X posts from existing datasets.', flush=True)


class ActionsOrchestrator(HorizonOrchestrator):
    async def _fetch_with_progress(self, name, scraper, since):
        outcome = await super()._fetch_with_progress(name, scraper, since)
        receipts = getattr(scraper, 'run_receipts', None)
        if receipts:
            save_json('apify-fetch-receipts.json', receipts)
            for receipt in receipts:
                print('Apify returned / retained:', json.dumps(receipt, ensure_ascii=False), flush=True)
        return outcome

    async def fetch_all_sources(self, since):
        items = await super().fetch_all_sources(since)
        save_json('collected-items.json', [item.model_dump(mode='json') for item in items])
        counts = Counter(item.source_type.value for item in items)
        save_json('source-counts.json', dict(counts))
        posts = [item for item in items if item.source_type == SourceType.TWITTER]
        save_x_posts(posts)
        print('Collected source counts:', dict(counts), flush=True)
        return items

    async def analyze_items(self, items):
        analyzed = await super().analyze_items(items)
        save_json('analyzed-items.json', [item.model_dump(mode='json') for item in analyzed])
        successful = [
            item for item in analyzed
            if item.processing and item.processing.analysis
            and item.processing.analysis.score is not None
        ]
        if items and not successful:
            raise RuntimeError('AI analysis failed for every item; refusing to publish an empty success report')
        return analyzed


async def main():
    os.chdir(ROOT)
    load_dotenv(ROOT / '.env')
    if '--inspect-apify' in sys.argv:
        config = StorageManager('data', config_path='data/config.actions.json').load_config()
        await inspect_apify(config)
        return
    original = os.environ['HORIZON_AI_BASE_URL']
    normalized = normalize_base_url(original)
    os.environ['HORIZON_AI_BASE_URL'] = normalized
    if normalized != original:
        print('Normalized API base URL to the OpenAI-compatible base path.', flush=True)
    storage = StorageManager('data', config_path='data/config.actions.json')
    config = storage.load_config()
    client = create_ai_client(config.ai)
    print('Checking AI connectivity with one small JSON completion...', flush=True)
    try:
        reply = await asyncio.wait_for(client.complete(
            system='Return only valid JSON.',
            user='Return exactly {"ok": true}.',
            max_tokens=1024,
        ), timeout=90)
        if json.loads(reply).get('ok') is not True:
            raise ValueError('AI preflight did not return the expected JSON object')
    except Exception as exc:
        message = str(getattr(exc, 'body', None) or str(exc))
        for name in ('OPENAI_API_KEY', 'APIFY_TOKEN', 'HORIZON_AI_BASE_URL', 'HORIZON_AI_MODEL'):
            secret = os.environ.get(name)
            if secret:
                message = message.replace(secret, '[redacted]')
        message = message.replace(original, '[redacted]').replace(normalized, '[redacted]')
        print(f'AI preflight failed: {type(exc).__name__}; HTTP {getattr(exc, "status_code", "n/a")}; {message[:800]}', flush=True)
        raise SystemExit(1) from None
    print('AI preflight passed: valid JSON completion received.', flush=True)
    await ActionsOrchestrator(config, storage).run(force_hours=24)


if __name__ == '__main__':
    asyncio.run(main())
