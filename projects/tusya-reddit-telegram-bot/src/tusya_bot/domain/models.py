from __future__ import annotations

from dataclasses import dataclass

from tusya_bot.domain.enums import DeliveryStatus, MatchMode, PostStatus, ResourceType


@dataclass(frozen=True, slots=True)
class MonitoredResource:
    id: int | None
    original_input: str
    canonical_url: str
    subreddit: str
    resource_type: ResourceType
    search_query: str | None
    sort_mode: str
    enabled: bool = True
    baseline_completed: bool = False
    last_checked_at: str | None = None
    next_check_at: str | None = None
    last_success_at: str | None = None
    last_error: str | None = None
    created_at: str | None = None
    updated_at: str | None = None


@dataclass(frozen=True, slots=True)
class Keyword:
    id: int | None
    keyword: str
    normalized_keyword: str
    match_mode: MatchMode = MatchMode.CONTAINS
    enabled: bool = True
    case_sensitive: bool = False
    created_at: str | None = None
    updated_at: str | None = None


@dataclass(frozen=True, slots=True)
class RedditPost:
    id: int | None
    reddit_id: str
    resource_id: int
    subreddit: str
    title: str
    body: str
    permalink: str
    author: str | None
    created_utc: str
    matched_keywords_json: str = "[]"
    first_seen_at: str | None = None
    delivered_at: str | None = None
    opened_at: str | None = None
    status: PostStatus = PostStatus.NEW


@dataclass(frozen=True, slots=True)
class ReplyDraft:
    id: int | None
    reddit_post_id: int
    provider: str
    model: str
    prompt_version: str
    draft_text: str
    user_instruction: str | None = None
    created_at: str | None = None
    updated_at: str | None = None


@dataclass(frozen=True, slots=True)
class DeliveryEvent:
    id: int | None
    reddit_post_id: int
    telegram_chat_id: str
    telegram_message_id: str | None
    delivery_status: DeliveryStatus
    error: str | None = None
    created_at: str | None = None
