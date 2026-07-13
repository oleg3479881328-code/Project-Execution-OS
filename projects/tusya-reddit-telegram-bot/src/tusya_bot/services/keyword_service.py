from __future__ import annotations

from tusya_bot.db.engine import Database
from tusya_bot.db.repositories import KeywordRepository
from tusya_bot.domain.enums import MatchMode
from tusya_bot.domain.models import Keyword


class KeywordService:
    def __init__(self, database: Database) -> None:
        self._database = database

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
        async with self._database.connect() as connection:
            return await KeywordRepository(connection).create(entry)

    async def list_keywords(self) -> list[Keyword]:
        async with self._database.connect() as connection:
            return await KeywordRepository(connection).list_all()

    async def toggle_keyword(self, keyword_id: int, enabled: bool) -> None:
        async with self._database.connect() as connection:
            await KeywordRepository(connection).update_enabled(keyword_id, enabled)

    async def delete_keyword(self, keyword_id: int) -> None:
        async with self._database.connect() as connection:
            await KeywordRepository(connection).delete(keyword_id)
