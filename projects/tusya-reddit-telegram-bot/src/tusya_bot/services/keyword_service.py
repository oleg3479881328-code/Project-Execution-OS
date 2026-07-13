from __future__ import annotations

from tusya_bot.db.repositories import KeywordRepository
from tusya_bot.domain.enums import MatchMode
from tusya_bot.domain.models import Keyword


class KeywordService:
    def __init__(self, repository: KeywordRepository) -> None:
        self._repository = repository

    async def add_keyword(
        self,
        keyword: str,
        *,
        match_mode: MatchMode = MatchMode.CONTAINS,
        case_sensitive: bool = False,
    ) -> Keyword:
        normalized = keyword.strip() if case_sensitive else keyword.strip().casefold()
        entry = Keyword(
            id=None,
            keyword=keyword.strip(),
            normalized_keyword=normalized,
            match_mode=match_mode,
            case_sensitive=case_sensitive,
        )
        return await self._repository.create(entry)

    async def list_keywords(self) -> list[Keyword]:
        return await self._repository.list_all()

    async def toggle_keyword(self, keyword_id: int, enabled: bool) -> None:
        await self._repository.update_enabled(keyword_id, enabled)

    async def delete_keyword(self, keyword_id: int) -> None:
        await self._repository.delete(keyword_id)
