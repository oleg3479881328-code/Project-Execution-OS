from __future__ import annotations

import asyncio
import json
import random
from collections.abc import Callable
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta

from tusya_bot.db.engine import Database
from tusya_bot.db.repositories import KeywordRepository, PostRepository, ResourceRepository
from tusya_bot.delivery.protocols import DeliveryService
from tusya_bot.domain.models import Keyword, MonitoredResource, RedditPost
from tusya_bot.monitoring.matcher import KeywordRule, find_matching_keywords
from tusya_bot.monitoring.models import (
    CycleResult,
    DeliveryCandidate,
    MonitoringStatusSnapshot,
)
from tusya_bot.reddit.client import RedditFetchedPost, RedditResourceClient


@dataclass(frozen=True, slots=True)
class BackoffPolicy:
    base_interval_seconds: int
    max_multiplier: int = 8
    max_jitter_seconds: int = 30

    def next_delay_seconds(
        self,
        *,
        failure_count: int,
        jitter_seconds: float,
    ) -> int:
        multiplier = min(2 ** max(failure_count - 1, 0), self.max_multiplier)
        return int(self.base_interval_seconds * multiplier + jitter_seconds)


class MonitoringEngine:
    def __init__(
        self,
        *,
        database: Database,
        reddit_client: RedditResourceClient,
        delivery_service: DeliveryService,
        poll_interval_seconds: int,
        backoff_policy: BackoffPolicy | None = None,
        now_fn: Callable[[], datetime] | None = None,
        jitter_fn: Callable[[float], float] | None = None,
    ) -> None:
        self._database = database
        self._reddit_client = reddit_client
        self._delivery_service = delivery_service
        self._poll_interval_seconds = poll_interval_seconds
        self._backoff_policy = backoff_policy or BackoffPolicy(
            base_interval_seconds=poll_interval_seconds
        )
        self._now_fn = now_fn or (lambda: datetime.now(UTC))
        self._jitter_fn = jitter_fn or (
            lambda max_jitter: random.uniform(0.0, max_jitter)
        )
        self._lock = asyncio.Lock()
        self._monitoring_enabled = True
        self._last_cycle_started_at: str | None = None
        self._last_cycle_finished_at: str | None = None
        self._last_cycle_error: str | None = None
        self._next_cycle_at: str | None = None

    def set_monitoring_enabled(self, enabled: bool) -> None:
        self._monitoring_enabled = enabled
        if not enabled:
            self._next_cycle_at = None
        elif self._next_cycle_at is None:
            self._next_cycle_at = self._format_time(
                self._now_fn() + timedelta(seconds=self._poll_interval_seconds)
            )

    async def get_status_snapshot(self) -> MonitoringStatusSnapshot:
        async with self._database.connect() as connection:
            resource_repo = ResourceRepository(connection)
            keyword_repo = KeywordRepository(connection)
            resource_count = await resource_repo.count_all()
            keyword_count = await keyword_repo.count_all()

        return MonitoringStatusSnapshot(
            monitoring_enabled=self._monitoring_enabled,
            running=self._lock.locked(),
            resource_count=resource_count,
            keyword_count=keyword_count,
            last_cycle_started_at=self._last_cycle_started_at,
            last_cycle_finished_at=self._last_cycle_finished_at,
            last_cycle_error=self._last_cycle_error,
            next_cycle_at=self._next_cycle_at,
        )

    async def run_cycle(self, *, trigger: str) -> CycleResult:
        if self._lock.locked():
            return CycleResult(
                trigger=trigger,
                overlap_skipped=True,
                processed_resources=0,
                emitted_candidates=0,
                failed_resources=0,
            )

        async with self._lock:
            started_at = self._now_fn()
            self._last_cycle_started_at = self._format_time(started_at)
            self._last_cycle_error = None

            async with self._database.connect() as connection:
                resource_repo = ResourceRepository(connection)
                keyword_repo = KeywordRepository(connection)
                resources = await resource_repo.list_enabled()
                keywords = await keyword_repo.list_enabled()

            candidates: list[DeliveryCandidate] = []
            processed_resources = 0
            failed_resources = 0

            for resource in resources:
                if trigger == "scheduled" and not self._is_due(resource, started_at):
                    continue
                processed_resources += 1
                try:
                    candidates.extend(
                        await self._process_resource(
                            resource=resource,
                            keywords=keywords,
                            polled_at=started_at,
                        )
                    )
                except Exception as error:
                    failed_resources += 1
                    self._last_cycle_error = str(error)
                    await self._record_failure(
                        resource=resource,
                        polled_at=started_at,
                        error_message=str(error),
                    )

            if candidates:
                await self._delivery_service.deliver_candidates(candidates)

            finished_at = self._now_fn()
            self._last_cycle_finished_at = self._format_time(finished_at)
            self._next_cycle_at = self._format_time(
                finished_at + timedelta(seconds=self._poll_interval_seconds)
            )
            return CycleResult(
                trigger=trigger,
                overlap_skipped=False,
                processed_resources=processed_resources,
                emitted_candidates=len(candidates),
                failed_resources=failed_resources,
            )

    async def _process_resource(
        self,
        *,
        resource: MonitoredResource,
        keywords: list[Keyword],
        polled_at: datetime,
    ) -> list[DeliveryCandidate]:
        fetched_posts = await self._reddit_client.fetch_posts(resource)
        sorted_posts = sorted(fetched_posts, key=lambda post: post.created_utc)

        async with self._database.connect() as connection:
            resource_repo = ResourceRepository(connection)
            post_repo = PostRepository(connection)

            if not resource.baseline_completed:
                await self._persist_baseline(
                    resource=resource,
                    fetched_posts=sorted_posts,
                    keywords=keywords,
                    post_repo=post_repo,
                )
                await resource_repo.update_monitoring_state(
                    resource.id or 0,
                    baseline_completed=True,
                    last_checked_at=self._format_time(polled_at),
                    last_success_at=self._format_time(polled_at),
                    last_error="",
                    next_check_at=self._format_time(
                        polled_at + timedelta(seconds=self._poll_interval_seconds)
                    ),
                    failure_count=0,
                )
                return []

            existing_ids = await post_repo.list_existing_reddit_ids(
                [post.reddit_id for post in sorted_posts]
            )
            candidates: list[DeliveryCandidate] = []

            for fetched_post in sorted_posts:
                if fetched_post.reddit_id in existing_ids:
                    continue
                matched_keywords = self._match_keywords(
                    title=fetched_post.title,
                    body=fetched_post.body,
                    keywords=keywords,
                )
                saved_post = await post_repo.create(
                    self._build_reddit_post(
                        resource=resource,
                        fetched_post=fetched_post,
                        matched_keywords=matched_keywords,
                    )
                )
                if matched_keywords:
                    candidates.append(
                        DeliveryCandidate(
                            resource=resource,
                            post=saved_post,
                            matched_keywords=matched_keywords,
                        )
                    )

            await resource_repo.update_monitoring_state(
                resource.id or 0,
                last_checked_at=self._format_time(polled_at),
                last_success_at=self._format_time(polled_at),
                last_error="",
                next_check_at=self._format_time(
                    polled_at + timedelta(seconds=self._poll_interval_seconds)
                ),
                failure_count=0,
            )
            return candidates

    async def _persist_baseline(
        self,
        *,
        resource: MonitoredResource,
        fetched_posts: list[RedditFetchedPost],
        keywords: list[Keyword],
        post_repo: PostRepository,
    ) -> None:
        for fetched_post in fetched_posts:
            matched_keywords = self._match_keywords(
                title=fetched_post.title,
                body=fetched_post.body,
                keywords=keywords,
            )
            await post_repo.create(
                self._build_reddit_post(
                    resource=resource,
                    fetched_post=fetched_post,
                    matched_keywords=matched_keywords,
                )
            )

    async def _record_failure(
        self,
        *,
        resource: MonitoredResource,
        polled_at: datetime,
        error_message: str,
    ) -> None:
        failure_count = resource.failure_count + 1
        jitter_seconds = self._jitter_fn(self._backoff_policy.max_jitter_seconds)
        next_delay_seconds = self._backoff_policy.next_delay_seconds(
            failure_count=failure_count,
            jitter_seconds=jitter_seconds,
        )
        next_check_at = polled_at + timedelta(seconds=next_delay_seconds)

        async with self._database.connect() as connection:
            await ResourceRepository(connection).update_monitoring_state(
                resource.id or 0,
                last_checked_at=self._format_time(polled_at),
                last_error=error_message,
                next_check_at=self._format_time(next_check_at),
                failure_count=failure_count,
            )

    def _is_due(self, resource: MonitoredResource, now: datetime) -> bool:
        if resource.next_check_at is None:
            return True
        return self._parse_time(resource.next_check_at) <= now

    def _match_keywords(
        self,
        *,
        title: str,
        body: str,
        keywords: list[Keyword],
    ) -> tuple[str, ...]:
        rules = [
            KeywordRule(
                keyword=keyword.keyword,
                match_mode=keyword.match_mode.value,
                case_sensitive=keyword.case_sensitive,
            )
            for keyword in keywords
        ]
        return find_matching_keywords(title=title, body=body, rules=rules)

    def _build_reddit_post(
        self,
        *,
        resource: MonitoredResource,
        fetched_post: RedditFetchedPost,
        matched_keywords: tuple[str, ...],
    ) -> RedditPost:
        return RedditPost(
            id=None,
            reddit_id=fetched_post.reddit_id,
            resource_id=resource.id or 0,
            subreddit=fetched_post.subreddit,
            title=fetched_post.title,
            body=fetched_post.body,
            permalink=fetched_post.permalink,
            author=fetched_post.author,
            created_utc=fetched_post.created_utc,
            matched_keywords_json=json.dumps(list(matched_keywords), ensure_ascii=False),
        )

    @staticmethod
    def _format_time(value: datetime) -> str:
        return value.astimezone(UTC).isoformat()

    @staticmethod
    def _parse_time(value: str) -> datetime:
        return datetime.fromisoformat(value)
