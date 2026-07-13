from __future__ import annotations

from dataclasses import dataclass

from tusya_bot.domain.models import MonitoredResource, RedditPost


@dataclass(frozen=True, slots=True)
class DeliveryCandidate:
    resource: MonitoredResource
    post: RedditPost
    matched_keywords: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class CycleResult:
    trigger: str
    overlap_skipped: bool
    processed_resources: int
    emitted_candidates: int
    failed_resources: int


@dataclass(frozen=True, slots=True)
class MonitoringStatusSnapshot:
    monitoring_enabled: bool
    running: bool
    resource_count: int
    keyword_count: int
    last_cycle_started_at: str | None
    last_cycle_finished_at: str | None
    last_cycle_error: str | None
    next_cycle_at: str | None
