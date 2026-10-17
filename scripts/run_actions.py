"""Run the digest with an AI preflight and downloadable source evidence."""

import asyncio
from collections import Counter
import json
import os
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from dotenv import load_dotenv
from src.ai.client import create_ai_client
from src.models import SourceType
from src.orchestrator import HorizonOrchestrator
from src.storage.manager import StorageManager


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


class ActionsOrchestrator(HorizonOrchestrator):
    async def fetch_all_sources(self, since):
        items = await super().fetch_all_sources(since)
        save_json('collected-items.json', [item.model_dump(mode='json') for item in items])
        counts = Counter(item.source_type.value for item in items)
        save_json('source-counts.json', dict(counts))
        posts = [item for item in items if item.source_type == SourceType.TWITTER]
        lines = ['# 本次抓取的 X 帖子', '', f'共 {len(posts)} 条；这是原始采集结果，尚未按 AI 分数筛选。', '']
        for item in posts:
            lines.extend([
                f'## @{item.author or "unknown"}', '',
                f'发布时间：{item.published_at.isoformat()}', '',
                str(item.url), '', item.content or item.title, '',
            ])
        Path('data/run-evidence/x-posts.md').write_text('\n'.join(lines), encoding='utf-8')
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
