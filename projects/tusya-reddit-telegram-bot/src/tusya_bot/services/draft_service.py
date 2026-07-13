from __future__ import annotations

import logging
from dataclasses import asdict, dataclass

from tusya_bot.ai.client import DraftModelClient, DraftRequest
from tusya_bot.db.engine import Database
from tusya_bot.db.repositories import DraftRepository, PostRepository, SettingsRepository
from tusya_bot.domain.errors import DraftGenerationError, NotFoundError
from tusya_bot.domain.models import RedditPost, ReplyDraft

logger = logging.getLogger(__name__)

SETTINGS_KEY = "draft_preferences"
DEFAULT_LANGUAGE = "English (US)"
DEFAULT_TONE = "helpful, natural, non-pushy"
DEFAULT_MAX_WORDS = 120


@dataclass(frozen=True, slots=True)
class DraftPreferences:
    language: str = DEFAULT_LANGUAGE
    tone: str = DEFAULT_TONE
    max_words: int = DEFAULT_MAX_WORDS


class DraftService:
    def __init__(
        self,
        *,
        database: Database,
        client: DraftModelClient,
    ) -> None:
        self._database = database
        self._client = client

    async def get_preferences(self) -> DraftPreferences:
        async with self._database.connect() as connection:
            payload = await SettingsRepository(connection).get_json(SETTINGS_KEY)
        if payload is None:
            return DraftPreferences()
        return DraftPreferences(
            language=str(payload.get("language", DEFAULT_LANGUAGE)),
            tone=str(payload.get("tone", DEFAULT_TONE)),
            max_words=int(payload.get("max_words", DEFAULT_MAX_WORDS)),
        )

    async def update_preferences(
        self,
        *,
        language: str,
        tone: str,
        max_words: int,
    ) -> DraftPreferences:
        preferences = DraftPreferences(
            language=language.strip() or DEFAULT_LANGUAGE,
            tone=tone.strip() or DEFAULT_TONE,
            max_words=max(20, min(max_words, 400)),
        )
        async with self._database.connect() as connection:
            await SettingsRepository(connection).set_json(
                SETTINGS_KEY,
                asdict(preferences),
            )
        return preferences

    async def create_draft(
        self,
        post_id: int,
        *,
        owner_instruction: str | None = None,
    ) -> ReplyDraft:
        post = await self._get_post(post_id)
        preferences = await self.get_preferences()
        request = DraftRequest(
            title=post.title,
            body=post.body,
            subreddit=post.subreddit,
            matched_keywords=self._matched_keywords(post),
            language=preferences.language,
            tone=preferences.tone,
            max_words=preferences.max_words,
            owner_instruction=owner_instruction,
        )
        try:
            result = await self._client.create_draft(request)
        except Exception as error:
            logger.warning("Draft generation failed for post %s: %s", post_id, type(error).__name__)
            raise DraftGenerationError("Draft generation failed") from error

        async with self._database.connect() as connection:
            draft_repo = DraftRepository(connection)
            post_repo = PostRepository(connection)
            saved = await draft_repo.create(
                ReplyDraft(
                    id=None,
                    reddit_post_id=post_id,
                    provider=result.provider,
                    model=result.model,
                    prompt_version=result.prompt_version,
                    draft_text=result.text,
                    user_instruction=owner_instruction.strip() if owner_instruction else None,
                )
            )
            await post_repo.mark_drafted(post_id)
        return saved

    async def regenerate_draft(self, post_id: int) -> ReplyDraft:
        latest = await self.get_latest_draft(post_id)
        owner_instruction = latest.user_instruction if latest is not None else None
        return await self.create_draft(post_id, owner_instruction=owner_instruction)

    async def refine_draft(self, post_id: int, owner_instruction: str) -> ReplyDraft:
        return await self.create_draft(post_id, owner_instruction=owner_instruction)

    async def get_latest_draft(self, post_id: int) -> ReplyDraft | None:
        async with self._database.connect() as connection:
            return await DraftRepository(connection).get_latest_by_post_id(post_id)

    async def list_drafts(self, post_id: int) -> list[ReplyDraft]:
        async with self._database.connect() as connection:
            return await DraftRepository(connection).list_by_post_id(post_id)

    async def _get_post(self, post_id: int) -> RedditPost:
        async with self._database.connect() as connection:
            post = await PostRepository(connection).get_by_id(post_id)
        if post is None:
            raise NotFoundError(f"Post {post_id} was not found")
        return post

    @staticmethod
    def _matched_keywords(post: RedditPost) -> tuple[str, ...]:
        import json

        loaded = json.loads(post.matched_keywords_json)
        return tuple(str(item) for item in loaded)
