"""Twitter scraper using Apify altimis/scweet actor."""

import asyncio
import logging
import os
import re
from datetime import datetime, timezone
from html import unescape
from typing import List, Optional

from dateutil.parser import isoparse
import httpx

from .base import BaseScraper
from ..models import ContentItem, SourceType, TwitterConfig

logger = logging.getLogger(__name__)

_APIFY_BASE = "https://api.apify.com/v2"
_POLL_INTERVAL = 3.0
_MAX_WAIT = 180


class TwitterScraper(BaseScraper):
    """Fetch tweets via the Apify altimis/scweet actor."""

    def __init__(self, config: TwitterConfig, http_client: httpx.AsyncClient):
        super().__init__(config, http_client)
        self.config = config
        self.run_receipts: list[dict] = []
        self.raw_items: list[dict] = []
        self.completed_runs: dict[str, dict] = {}
        self.discussion_records: list[dict] = []
        self._start_attempted = False

    async def fetch(self, since: datetime) -> List[ContentItem]:
        if not self.config.enabled:
            return []

        users = [u.strip().lstrip("@") for u in self.config.users if u.strip()]
        keywords = [k.strip() for k in self.config.keywords if k.strip()]
        if not users and not keywords:
            logger.debug("No Twitter users or keywords configured, skipping.")
            return []

        token = os.environ.get(self.config.apify_token_env)
        if not token:
            logger.warning(
                f"Apify token not found in env var '{self.config.apify_token_env}'. Skipping Twitter."
            )
            return []

        if self.config.batch_discussions:
            return await self._fetch_official_discussions(token, users, since)

        items: List[ContentItem] = []
        seen_ids: set[str] = set()
        max_items = max(100, self.config.fetch_limit)
        requested_since = since.astimezone(timezone.utc).isoformat()

        if users:
            logger.info(f"Fetching Twitter (Apify) for users: {users}")
            await self._collect_from_payload(
                token,
                {
                    "source_mode": "profiles",
                    "profile_urls": users,
                    "search_sort": "Latest",
                    "max_items": max_items,
                    "since": requested_since,
                    "per_profile_limit": max(1, max_items // len(users)),
                },
                since,
                items,
                seen_ids,
            )

        for keyword in keywords:
            logger.info(f"Fetching Twitter (Apify) search for keyword: {keyword}")
            try:
                await self._collect_from_payload(
                    token,
                    {
                        "source_mode": "search",
                        "search_query": keyword,
                        "search_sort": "Latest",
                        "max_items": max_items,
                        "since": requested_since,
                    },
                    since,
                    items,
                    seen_ids,
                )
            except Exception as exc:
                logger.error(f"Keyword search failed for {keyword!r}: {exc}")

        logger.info(f"Fetched {len(items)} tweets via Apify.")
        return items

    def _official_discussion_payload(self, users: List[str], since: datetime) -> dict:
        if not users or self.config.keywords:
            raise ValueError('Batch discussions require official users and no extra keyword runs')
        if self.config.fetch_limit > 100:
            raise ValueError('Batch discussion test is capped at 100 rows including replies')
        if any(not re.fullmatch(r'[A-Za-z0-9_]{1,15}', user) for user in users):
            raise ValueError('Invalid X account handle')
        authors = ' OR '.join(f'from:{user}' for user in users)
        query = f'(({authors}) -filter:retweets)'
        if self.config.fetch_reply_text:
            targets = ' OR '.join(f'to:{user}' for user in users)
            query += f' OR (({targets}) filter:replies min_faves:{self.config.reply_min_likes})'
        return {
            'source_mode': 'search', 'search_query': query,
            'since': since.astimezone(timezone.utc).isoformat(),
            'until': datetime.now(timezone.utc).isoformat(),
            'search_sort': 'Top', 'max_items': max(100, self.config.fetch_limit),
        }

    async def _fetch_official_discussions(self, token, users, since):
        captured, seen = [], set()
        await self._collect_from_payload(
            token, self._official_discussion_payload(users, since), since, captured, seen
        )
        official = {user.lower() for user in users}
        authored = [item for item in captured if item.metadata['screen_name'].lower() in official]
        authored_ids = {item.metadata['tweet_id'] for item in authored}
        roots = [
            item for item in authored
            if str(item.metadata.get('in_reply_to_status_id') or '').removeprefix('tweet-') not in authored_ids
        ]
        for item in roots:
            root_id = item.metadata['tweet_id']
            conversation = item.metadata['conversation_id']
            candidates = [
                reply for reply in captured
                if reply.id != item.id
                and (str(reply.metadata.get('in_reply_to_status_id') or '').removeprefix('tweet-') == root_id
                     or reply.metadata['conversation_id'] == conversation)
                and reply.metadata.get('favorite_count', 0) >= self.config.reply_min_likes
            ]
            candidates.sort(key=lambda reply: reply.metadata.get('favorite_count', 0) * 2
                            + reply.metadata.get('reply_count', 0), reverse=True)
            selected = candidates[:self.config.max_replies_per_tweet] if self.config.fetch_reply_text else []
            replies = [{
                'id': reply.metadata['tweet_id'], 'author': reply.metadata['screen_name'],
                'text': reply.content, 'url': str(reply.url),
                'likes': reply.metadata.get('favorite_count', 0),
            } for reply in selected]
            lines = [f"[@{reply['author']} | ❤️ {reply['likes']} | {reply['url']}] {reply['text'][:500]}"
                     for reply in replies]
            item.metadata['discussion_replies'] = replies
            item.metadata['discussion_reply_lines'] = lines
            self.append_discussion_content(item, lines)
            self.discussion_records.append({
                'post_id': root_id, 'author': item.metadata['screen_name'], 'url': str(item.url),
                'captured_matching_replies': len(candidates), 'selected_replies': replies,
            })
        if self.run_receipts:
            self.run_receipts[-1].update({
                'official_posts': len(roots),
                'community_rows': len(captured) - len(authored),
                'attached_replies': sum(len(item.metadata['discussion_replies']) for item in roots),
            })
        return roots

    async def _collect_from_payload(
        self,
        token: str,
        payload: dict,
        since: datetime,
        items: List[ContentItem],
        seen_ids: set[str],
    ) -> None:
        run_id, dataset_id = await self._start_run_with_payload(token, payload)
        if not run_id or not dataset_id:
            return
        if not await self._wait_for_run(token, run_id):
            return
        raw_items = await self._fetch_dataset(token, dataset_id)
        self.raw_items = raw_items
        previous_count = len(items)
        for raw in raw_items:
            if isinstance(raw, dict) and raw.get("noResults"):
                continue
            parsed = self._parse_item(raw, since)
            if parsed and parsed.id not in seen_ids:
                seen_ids.add(parsed.id)
                items.append(parsed)
        self.run_receipts.append({
            "run_id": run_id,
            "dataset_id": dataset_id,
            "source_mode": payload.get("source_mode"),
            "requested_max_items": payload.get("max_items"),
            "requested_since": payload.get("since"),
            "requested_until": payload.get("until"),
            "search_query": payload.get("search_query"),
            "raw_rows": len(raw_items),
            "included_unique_rows": len(items) - previous_count,
            "usage_total_usd": self.completed_runs.get(run_id, {}).get('usageTotalUsd'),
            "charged_event_counts": self.completed_runs.get(run_id, {}).get('chargedEventCounts'),
            "charge_limit_usd": self.config.apify_max_total_charge_usd,
        })

    async def _start_run_with_payload(
        self, token: str, payload: dict
    ) -> tuple[Optional[str], Optional[str]]:
        if self.config.batch_discussions and self._start_attempted:
            raise RuntimeError('Only one Actor start is allowed for a batched discussion fetch')
        self._start_attempted = True
        url = f"{_APIFY_BASE}/acts/{self.config.actor_id}/runs"
        params = {}
        if self.config.apify_max_total_charge_usd is not None:
            params = {'maxTotalChargeUsd': self.config.apify_max_total_charge_usd,
                      'memory': 1024, 'timeout': 180, 'restartOnError': 'false'}
        try:
            resp = await self.client.post(url, json=payload, params=params,
                                          headers={'Authorization': f'Bearer {token}'}, timeout=30.0)
            resp.raise_for_status()
            data = resp.json()["data"]
            run_id = data["id"]
            dataset_id = data["defaultDatasetId"]
            logger.debug(f"Started Apify run {run_id}, dataset {dataset_id}")
            return run_id, dataset_id
        except Exception as exc:
            logger.error(f"Failed to start Apify run: {exc}")
            return None, None

    async def _start_run(
        self, token: str, users: List[str]
    ) -> tuple[Optional[str], Optional[str]]:
        return await self._start_run_with_payload(
            token,
            {
                "source_mode": "profiles",
                "profile_urls": users,
                "search_sort": "Latest",
                "max_items": max(100, self.config.fetch_limit),
            },
        )

    async def _wait_for_run(self, token: str, run_id: str) -> bool:
        url = f"{_APIFY_BASE}/actor-runs/{run_id}?token={token}"
        elapsed = 0.0
        while elapsed < _MAX_WAIT:
            try:
                resp = await self.client.get(url, timeout=10.0)
                resp.raise_for_status()
                status = resp.json()["data"]["status"]
                self.completed_runs[run_id] = {
                    key: resp.json()['data'].get(key)
                    for key in ('status', 'usageTotalUsd', 'chargedEventCounts')
                }
                if status == "SUCCEEDED":
                    return True
                if status in ("FAILED", "ABORTED", "TIMED-OUT"):
                    logger.error(f"Apify run {run_id} ended with status: {status}")
                    return False
            except Exception as exc:
                logger.warning(f"Error polling Apify run {run_id}: {exc}")
            await asyncio.sleep(_POLL_INTERVAL)
            elapsed += _POLL_INTERVAL
        logger.warning(f"Apify run {run_id} timed out after {_MAX_WAIT}s.")
        return False

    async def _fetch_dataset(self, token: str, dataset_id: str) -> list:
        url = f"{_APIFY_BASE}/datasets/{dataset_id}/items?token={token}"
        try:
            resp = await self.client.get(url, timeout=30.0)
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            logger.error(f"Failed to fetch Apify dataset {dataset_id}: {exc}")
            return []

    async def fetch_replies_for_item(self, item: ContentItem) -> List[str]:
        """Fetch reply texts for one tweet using scweet search mode."""
        if not self.config.fetch_reply_text:
            return []
        if self.config.batch_discussions:
            return item.metadata.get('discussion_reply_lines', [])

        token = os.environ.get(self.config.apify_token_env)
        if not token:
            return []

        conversation_id = str(item.metadata.get("conversation_id") or "")
        if not conversation_id:
            return []

        max_replies = max(self.config.max_replies_per_tweet, 0)
        if max_replies == 0:
            return []

        max_items = max(100, max_replies * 5)
        payload = {
            "source_mode": "search",
            "search_query": f"conversation_id:{conversation_id}",
            "search_sort": "Latest",
            "max_items": max_items,
        }

        run_id, dataset_id = await self._start_run_with_payload(token, payload)
        if not run_id or not dataset_id:
            return []

        if not await self._wait_for_run(token, run_id):
            return []

        rows = await self._fetch_dataset(token, dataset_id)
        return self._extract_reply_lines(item, rows, max_replies)

    def _extract_reply_lines(self, item: ContentItem, rows: list, max_replies: int) -> List[str]:
        """Convert scweet rows into compact reply lines."""
        min_likes = max(self.config.reply_min_likes, 0)
        tweet_id = str(item.metadata.get("tweet_id") or "")
        own_author = (item.author or "").lstrip("@")
        candidates = []

        for row in rows:
            if not isinstance(row, dict) or row.get("noResults"):
                continue

            row_id = str(row.get("id") or "")
            if row_id.startswith("tweet-"):
                row_id = row_id[6:]
            if tweet_id and row_id == tweet_id:
                continue

            user = row.get("user") or {}
            handle = (
                user.get("handle")
                or row.get("handle")
                or user.get("username")
                or "unknown"
            )
            if handle and own_author and handle.lower() == own_author.lower():
                continue

            text = unescape((row.get("text") or "").strip())
            if not text:
                continue

            likes = int(row.get("favorite_count") or 0)
            replies = int(row.get("reply_count") or 0)
            if likes < min_likes:
                continue

            score = likes * 2 + replies
            line = f"[@{handle} | ❤️ {likes} | 💬 {replies}] {text[:280]}"
            candidates.append((score, line))

        candidates.sort(key=lambda x: x[0], reverse=True)
        return [line for _, line in candidates[:max_replies]]

    @staticmethod
    def append_discussion_content(item: ContentItem, reply_lines: List[str]) -> bool:
        """Append reply lines under Top Comments marker."""
        if not reply_lines:
            return False

        existing = item.content or ""
        marker = "--- Top Comments ---"
        block = "\n".join(reply_lines)

        if marker in existing:
            if block in existing:
                return False
            item.content = existing + "\n" + block
            return True

        if existing:
            item.content = existing + f"\n\n{marker}\n" + block
        else:
            item.content = f"{marker}\n" + block
        return True

    def _parse_item(self, item: dict, since: datetime) -> Optional[ContentItem]:
        try:
            created_at_str = item.get("created_at")
            if not created_at_str:
                return None

            try:
                published_at = datetime.strptime(
                    created_at_str, "%a %b %d %H:%M:%S %z %Y"
                )
            except ValueError:
                published_at = isoparse(created_at_str)

            if published_at.tzinfo is None:
                published_at = published_at.replace(tzinfo=timezone.utc)

            if published_at < since:
                return None

            tweet_id = str(item.get("id_str") or item.get("id") or "")
            if not tweet_id:
                return None

            # Normalize tweet_id: scweet prefixes with "tweet-"
            numeric_id = tweet_id.removeprefix("tweet-")
            conversation_id = str(
                item.get("conversation_id")
                or item.get("tweet", {}).get("conversation_id")
                or numeric_id
            )

            user = item.get("user") or {}
            screen_name = (
                user.get("screen_name")
                or user.get("username")
                or user.get("handle")
                or item.get("handle")
                or item.get("username")
                or "unknown"
            )
            author = user.get("name") or screen_name

            text = item.get("full_text") or item.get("text") or ""
            if not text:
                return None
            text = unescape(text)

            url = item.get("tweet_url") or item.get("url")
            if not url:
                permalink = item.get("permalink")
                if permalink and screen_name != "unknown":
                    url = f"https://twitter.com/{screen_name}{permalink}"
                else:
                    url = f"https://twitter.com/{screen_name}/status/{numeric_id}"

            title_body = text[:50].replace("\n", " ").strip()
            if len(text) > 50:
                title_body += "..."

            return ContentItem(
                id=self._generate_id(SourceType.TWITTER.value, "tweet", numeric_id),
                source_type=SourceType.TWITTER,
                title=f"@{screen_name}: {title_body}",
                url=url,
                content=text,
                author=author,
                published_at=published_at,
                profile=self.config.profile,
                metadata={
                    "tweet_id": numeric_id,
                    "screen_name": screen_name,
                    "conversation_id": conversation_id,
                    "favorite_count": item.get("favorite_count", 0),
                    "retweet_count": item.get("retweet_count", 0),
                    "reply_count": item.get("reply_count", 0),
                    "view_count": item.get("view_count"),
                    "is_reply": item.get("is_reply", False),
                    "in_reply_to_status_id": item.get("in_reply_to_status_id"),
                    "in_reply_to_screen_name": item.get("in_reply_to_screen_name"),
                    "category": self.config.category,
                },
            )
        except Exception as exc:
            logger.debug(f"Failed to parse tweet: {exc}")
            return None
