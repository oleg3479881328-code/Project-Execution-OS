from __future__ import annotations

from datetime import UTC, datetime

from tusya_bot.db.engine import Database
from tusya_bot.db.repositories import DeliveryEventRepository, PostRepository
from tusya_bot.domain.enums import DeliveryStatus
from tusya_bot.domain.errors import NotFoundError
from tusya_bot.domain.models import DeliveryEvent, RedditPost


class PostService:
    def __init__(self, database: Database) -> None:
        self._database = database

    async def get_post(self, post_id: int) -> RedditPost:
        async with self._database.connect() as connection:
            post = await PostRepository(connection).get_by_id(post_id)
        if post is None:
            raise NotFoundError(f"Post {post_id} was not found")
        return post

    async def list_feed_page(
        self,
        *,
        page: int,
        page_size: int,
    ) -> tuple[list[RedditPost], int]:
        offset = page * page_size
        async with self._database.connect() as connection:
            post_repo = PostRepository(connection)
            posts = await post_repo.list_recent_matching(limit=page_size, offset=offset)
            total = await post_repo.count_matching()
        return posts, total

    async def mark_opened(self, post_id: int) -> RedditPost:
        opened_at = datetime.now(UTC).isoformat()
        async with self._database.connect() as connection:
            post_repo = PostRepository(connection)
            await post_repo.mark_opened(post_id, opened_at)
            post = await post_repo.get_by_id(post_id)
        if post is None:
            raise NotFoundError(f"Post {post_id} was not found")
        return post

    async def mark_ignored(self, post_id: int) -> RedditPost:
        async with self._database.connect() as connection:
            post_repo = PostRepository(connection)
            await post_repo.mark_ignored(post_id)
            post = await post_repo.get_by_id(post_id)
        if post is None:
            raise NotFoundError(f"Post {post_id} was not found")
        return post

    async def record_delivery_success(
        self,
        *,
        post_id: int,
        telegram_chat_id: int,
        telegram_message_id: int,
    ) -> None:
        delivered_at = datetime.now(UTC).isoformat()
        async with self._database.connect() as connection:
            post_repo = PostRepository(connection)
            event_repo = DeliveryEventRepository(connection)
            await post_repo.mark_delivered(post_id, delivered_at=delivered_at)
            await event_repo.create(
                DeliveryEvent(
                    id=None,
                    reddit_post_id=post_id,
                    telegram_chat_id=str(telegram_chat_id),
                    telegram_message_id=str(telegram_message_id),
                    delivery_status=DeliveryStatus.DELIVERED,
                )
            )

    async def record_delivery_failure(
        self,
        *,
        post_id: int,
        telegram_chat_id: int,
        error: str,
    ) -> None:
        async with self._database.connect() as connection:
            await DeliveryEventRepository(connection).create(
                DeliveryEvent(
                    id=None,
                    reddit_post_id=post_id,
                    telegram_chat_id=str(telegram_chat_id),
                    telegram_message_id=None,
                    delivery_status=DeliveryStatus.FAILED,
                    error=error,
                )
            )

    async def already_delivered(self, post_id: int) -> bool:
        async with self._database.connect() as connection:
            post_repo = PostRepository(connection)
            event_repo = DeliveryEventRepository(connection)
            post = await post_repo.get_by_id(post_id)
            if post is None:
                raise NotFoundError(f"Post {post_id} was not found")
            return post.delivered_at is not None or await event_repo.has_success_for_post(post_id)
