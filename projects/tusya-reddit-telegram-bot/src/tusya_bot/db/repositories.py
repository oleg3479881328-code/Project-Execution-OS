from __future__ import annotations

import json
from dataclasses import asdict
from datetime import UTC, datetime
from typing import Any

import aiosqlite

from tusya_bot.domain.enums import DeliveryStatus, MatchMode, PostStatus, ResourceType
from tusya_bot.domain.errors import DuplicateKeywordError, DuplicateResourceError
from tusya_bot.domain.models import (
    DeliveryEvent,
    Keyword,
    MonitoredResource,
    RedditPost,
    ReplyDraft,
)


def utc_now() -> str:
    return datetime.now(UTC).isoformat()


def _bool_to_int(value: bool) -> int:
    return 1 if value else 0


def _row_to_resource(row: aiosqlite.Row) -> MonitoredResource:
    return MonitoredResource(
        id=int(row["id"]),
        original_input=str(row["original_input"]),
        canonical_url=str(row["canonical_url"]),
        subreddit=str(row["subreddit"]),
        resource_type=ResourceType(str(row["resource_type"])),
        search_query=row["search_query"],
        sort_mode=str(row["sort_mode"]),
        enabled=bool(row["enabled"]),
        baseline_completed=bool(row["baseline_completed"]),
        last_checked_at=row["last_checked_at"],
        next_check_at=row["next_check_at"],
        last_success_at=row["last_success_at"],
        last_error=row["last_error"],
        failure_count=int(row["failure_count"]),
        created_at=str(row["created_at"]),
        updated_at=str(row["updated_at"]),
    )


def _row_to_keyword(row: aiosqlite.Row) -> Keyword:
    return Keyword(
        id=int(row["id"]),
        keyword=str(row["keyword"]),
        normalized_keyword=str(row["normalized_keyword"]),
        match_mode=MatchMode(str(row["match_mode"])),
        enabled=bool(row["enabled"]),
        case_sensitive=bool(row["case_sensitive"]),
        created_at=str(row["created_at"]),
        updated_at=str(row["updated_at"]),
    )


def _row_to_post(row: aiosqlite.Row) -> RedditPost:
    return RedditPost(
        id=int(row["id"]),
        reddit_id=str(row["reddit_id"]),
        resource_id=int(row["resource_id"]),
        subreddit=str(row["subreddit"]),
        title=str(row["title"]),
        body=str(row["body"]),
        permalink=str(row["permalink"]),
        author=row["author"],
        created_utc=str(row["created_utc"]),
        matched_keywords_json=str(row["matched_keywords_json"]),
        first_seen_at=str(row["first_seen_at"]),
        delivered_at=row["delivered_at"],
        opened_at=row["opened_at"],
        status=PostStatus(str(row["status"])),
    )


class ResourceRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def create(self, resource: MonitoredResource) -> MonitoredResource:
        now = utc_now()
        try:
            cursor = await self._connection.execute(
                """
                INSERT INTO monitored_resources (
                  original_input, canonical_url, subreddit, resource_type, search_query,
                  sort_mode, enabled, baseline_completed, failure_count, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    resource.original_input,
                    resource.canonical_url,
                    resource.subreddit,
                    resource.resource_type.value,
                    resource.search_query,
                    resource.sort_mode,
                    _bool_to_int(resource.enabled),
                    _bool_to_int(resource.baseline_completed),
                    resource.failure_count,
                    now,
                    now,
                ),
            )
        except aiosqlite.IntegrityError as error:
            raise DuplicateResourceError(resource.canonical_url) from error
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a row id for monitored_resources")

        return MonitoredResource(
            **{
                **asdict(resource),
                "id": int(cursor.lastrowid),
                "created_at": now,
                "updated_at": now,
            }
        )

    async def list_all(self) -> list[MonitoredResource]:
        rows = await (
            await self._connection.execute(
                "SELECT * FROM monitored_resources ORDER BY id ASC"
            )
        ).fetchall()
        return [_row_to_resource(row) for row in rows]

    async def list_enabled(self) -> list[MonitoredResource]:
        rows = await (
            await self._connection.execute(
                "SELECT * FROM monitored_resources WHERE enabled = 1 ORDER BY id ASC"
            )
        ).fetchall()
        return [_row_to_resource(row) for row in rows]

    async def count_all(self) -> int:
        row = await (
            await self._connection.execute(
                "SELECT COUNT(*) AS count FROM monitored_resources"
            )
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    async def count_enabled(self) -> int:
        row = await (
            await self._connection.execute(
                "SELECT COUNT(*) AS count FROM monitored_resources WHERE enabled = 1"
            )
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    async def update_enabled(self, resource_id: int, enabled: bool) -> None:
        await self._connection.execute(
            "UPDATE monitored_resources SET enabled = ?, updated_at = ? WHERE id = ?",
            (_bool_to_int(enabled), utc_now(), resource_id),
        )

    async def update_monitoring_state(
        self,
        resource_id: int,
        *,
        baseline_completed: bool | None = None,
        last_checked_at: str | None = None,
        next_check_at: str | None = None,
        last_success_at: str | None = None,
        last_error: str | None = None,
        failure_count: int | None = None,
    ) -> None:
        assignments: list[str] = ["updated_at = ?"]
        values: list[Any] = [utc_now()]

        if baseline_completed is not None:
            assignments.append("baseline_completed = ?")
            values.append(_bool_to_int(baseline_completed))
        if last_checked_at is not None:
            assignments.append("last_checked_at = ?")
            values.append(last_checked_at)
        if next_check_at is not None:
            assignments.append("next_check_at = ?")
            values.append(next_check_at)
        if last_success_at is not None:
            assignments.append("last_success_at = ?")
            values.append(last_success_at)
        if last_error is not None:
            assignments.append("last_error = ?")
            values.append(last_error)
        if failure_count is not None:
            assignments.append("failure_count = ?")
            values.append(failure_count)

        values.append(resource_id)
        await self._connection.execute(
            f"UPDATE monitored_resources SET {', '.join(assignments)} WHERE id = ?",
            tuple(values),
        )

    async def delete(self, resource_id: int) -> None:
        await self._connection.execute(
            "DELETE FROM monitored_resources WHERE id = ?",
            (resource_id,),
        )


class KeywordRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def create(self, keyword: Keyword) -> Keyword:
        now = utc_now()
        try:
            cursor = await self._connection.execute(
                """
                INSERT INTO monitored_keywords (
                  keyword, normalized_keyword, match_mode, enabled, case_sensitive,
                  created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    keyword.keyword,
                    keyword.normalized_keyword,
                    keyword.match_mode.value,
                    _bool_to_int(keyword.enabled),
                    _bool_to_int(keyword.case_sensitive),
                    now,
                    now,
                ),
            )
        except aiosqlite.IntegrityError as error:
            raise DuplicateKeywordError(keyword.normalized_keyword) from error
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a row id for monitored_keywords")

        return Keyword(
            **{**asdict(keyword), "id": int(cursor.lastrowid), "created_at": now, "updated_at": now}
        )

    async def list_all(self) -> list[Keyword]:
        rows = await (
            await self._connection.execute(
                "SELECT * FROM monitored_keywords ORDER BY id ASC"
            )
        ).fetchall()
        return [_row_to_keyword(row) for row in rows]

    async def list_enabled(self) -> list[Keyword]:
        rows = await (
            await self._connection.execute(
                "SELECT * FROM monitored_keywords WHERE enabled = 1 ORDER BY id ASC"
            )
        ).fetchall()
        return [_row_to_keyword(row) for row in rows]

    async def count_all(self) -> int:
        row = await (
            await self._connection.execute(
                "SELECT COUNT(*) AS count FROM monitored_keywords"
            )
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    async def update_enabled(self, keyword_id: int, enabled: bool) -> None:
        await self._connection.execute(
            "UPDATE monitored_keywords SET enabled = ?, updated_at = ? WHERE id = ?",
            (_bool_to_int(enabled), utc_now(), keyword_id),
        )

    async def delete(self, keyword_id: int) -> None:
        await self._connection.execute("DELETE FROM monitored_keywords WHERE id = ?", (keyword_id,))


class PostRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def create(self, post: RedditPost) -> RedditPost:
        now = utc_now()
        cursor = await self._connection.execute(
            """
            INSERT INTO reddit_posts (
              reddit_id, resource_id, subreddit, title, body, permalink, author,
              created_utc, matched_keywords_json, first_seen_at, delivered_at, opened_at, status
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                post.reddit_id,
                post.resource_id,
                post.subreddit,
                post.title,
                post.body,
                post.permalink,
                post.author,
                post.created_utc,
                post.matched_keywords_json,
                post.first_seen_at or now,
                post.delivered_at,
                post.opened_at,
                post.status.value,
            ),
        )
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a row id for reddit_posts")
        return RedditPost(
            **{
                **asdict(post),
                "id": int(cursor.lastrowid),
                "first_seen_at": post.first_seen_at or now,
            }
        )

    async def list_existing_reddit_ids(self, reddit_ids: list[str]) -> set[str]:
        if not reddit_ids:
            return set()

        placeholders = ", ".join("?" for _ in reddit_ids)
        rows = await (
            await self._connection.execute(
                f"SELECT reddit_id FROM reddit_posts WHERE reddit_id IN ({placeholders})",
                tuple(reddit_ids),
            )
        ).fetchall()
        return {str(row["reddit_id"]) for row in rows}

    async def list_by_resource(self, resource_id: int) -> list[RedditPost]:
        rows = await (
            await self._connection.execute(
                "SELECT * FROM reddit_posts WHERE resource_id = ? ORDER BY id ASC",
                (resource_id,),
            )
        ).fetchall()
        return [_row_to_post(row) for row in rows]

    async def get_by_id(self, post_id: int) -> RedditPost | None:
        row = await (
            await self._connection.execute(
                "SELECT * FROM reddit_posts WHERE id = ?",
                (post_id,),
            )
        ).fetchone()
        return None if row is None else _row_to_post(row)

    async def list_recent_matching(
        self,
        *,
        limit: int,
        offset: int = 0,
    ) -> list[RedditPost]:
        rows = await (
            await self._connection.execute(
                """
                SELECT *
                FROM reddit_posts
                WHERE matched_keywords_json <> '[]'
                ORDER BY first_seen_at DESC, id DESC
                LIMIT ? OFFSET ?
                """,
                (limit, offset),
            )
        ).fetchall()
        return [_row_to_post(row) for row in rows]

    async def count_matching(self) -> int:
        row = await (
            await self._connection.execute(
                """
                SELECT COUNT(*) AS count
                FROM reddit_posts
                WHERE matched_keywords_json <> '[]'
                """
            )
        ).fetchone()
        return int(row["count"]) if row is not None else 0

    async def get_by_reddit_id(self, reddit_id: str) -> RedditPost | None:
        row = await (
            await self._connection.execute(
                "SELECT * FROM reddit_posts WHERE reddit_id = ?",
                (reddit_id,),
            )
        ).fetchone()
        return None if row is None else _row_to_post(row)

    async def mark_status(self, post_id: int, status: PostStatus) -> None:
        await self._connection.execute(
            "UPDATE reddit_posts SET status = ? WHERE id = ?",
            (status.value, post_id),
        )

    async def mark_opened(self, post_id: int, opened_at: str) -> None:
        await self._connection.execute(
            """
            UPDATE reddit_posts
            SET status = ?, opened_at = ?
            WHERE id = ?
            """,
            (PostStatus.OPENED.value, opened_at, post_id),
        )

    async def mark_ignored(self, post_id: int) -> None:
        await self._connection.execute(
            "UPDATE reddit_posts SET status = ? WHERE id = ?",
            (PostStatus.IGNORED.value, post_id),
        )

    async def mark_drafted(self, post_id: int) -> None:
        await self._connection.execute(
            "UPDATE reddit_posts SET status = ? WHERE id = ?",
            (PostStatus.DRAFTED.value, post_id),
        )

    async def mark_delivered(
        self,
        post_id: int,
        *,
        delivered_at: str,
    ) -> None:
        await self._connection.execute(
            """
            UPDATE reddit_posts
            SET delivered_at = ?
            WHERE id = ?
            """,
            (delivered_at, post_id),
        )


class DraftRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def create(self, draft: ReplyDraft) -> ReplyDraft:
        now = utc_now()
        cursor = await self._connection.execute(
            """
            INSERT INTO reply_drafts (
              reddit_post_id, provider, model, prompt_version, draft_text,
              user_instruction, created_at, updated_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                draft.reddit_post_id,
                draft.provider,
                draft.model,
                draft.prompt_version,
                draft.draft_text,
                draft.user_instruction,
                now,
                now,
            ),
        )
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a row id for reply_drafts")
        return ReplyDraft(
            **{
                **asdict(draft),
                "id": int(cursor.lastrowid),
                "created_at": now,
                "updated_at": now,
            }
        )


class SettingsRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def set_json(self, key: str, value: dict[str, Any]) -> None:
        now = utc_now()
        await self._connection.execute(
            """
            INSERT INTO app_settings (key, value_json, updated_at)
            VALUES (?, ?, ?)
            ON CONFLICT(key) DO UPDATE
            SET value_json = excluded.value_json, updated_at = excluded.updated_at
            """,
            (key, json.dumps(value, ensure_ascii=False), now),
        )

    async def get_json(self, key: str) -> dict[str, Any] | None:
        row = await (
            await self._connection.execute(
                "SELECT value_json FROM app_settings WHERE key = ?",
                (key,),
            )
        ).fetchone()
        return None if row is None else json.loads(str(row["value_json"]))


class DeliveryEventRepository:
    def __init__(self, connection: aiosqlite.Connection) -> None:
        self._connection = connection

    async def create(self, event: DeliveryEvent) -> DeliveryEvent:
        now = utc_now()
        cursor = await self._connection.execute(
            """
            INSERT INTO delivery_events (
              reddit_post_id, telegram_chat_id, telegram_message_id, delivery_status,
              error, created_at
            ) VALUES (?, ?, ?, ?, ?, ?)
            """,
            (
                event.reddit_post_id,
                event.telegram_chat_id,
                event.telegram_message_id,
                event.delivery_status.value,
                event.error,
                now,
            ),
        )
        if cursor.lastrowid is None:
            raise RuntimeError("SQLite did not return a row id for delivery_events")
        return DeliveryEvent(**{**asdict(event), "id": int(cursor.lastrowid), "created_at": now})

    async def list_by_post_id(self, post_id: int) -> list[DeliveryEvent]:
        rows = await (
            await self._connection.execute(
                """
                SELECT *
                FROM delivery_events
                WHERE reddit_post_id = ?
                ORDER BY id ASC
                """,
                (post_id,),
            )
        ).fetchall()
        return [
            DeliveryEvent(
                id=int(row["id"]),
                reddit_post_id=int(row["reddit_post_id"]),
                telegram_chat_id=str(row["telegram_chat_id"]),
                telegram_message_id=row["telegram_message_id"],
                delivery_status=DeliveryStatus(str(row["delivery_status"])),
                error=row["error"],
                created_at=str(row["created_at"]),
            )
            for row in rows
        ]

    async def has_success_for_post(self, post_id: int) -> bool:
        row = await (
            await self._connection.execute(
                """
                SELECT 1 AS found
                FROM delivery_events
                WHERE reddit_post_id = ? AND delivery_status = 'delivered'
                LIMIT 1
                """,
                (post_id,),
            )
        ).fetchone()
        return row is not None
