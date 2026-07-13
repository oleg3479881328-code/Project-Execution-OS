from __future__ import annotations

from tusya_bot.db.engine import Database
from tusya_bot.db.repositories import ResourceRepository
from tusya_bot.domain.models import MonitoredResource
from tusya_bot.monitoring.normalization import normalize_reddit_resource


class ResourceService:
    def __init__(self, database: Database) -> None:
        self._database = database

    async def add_resource(self, raw_value: str) -> MonitoredResource:
        normalized = normalize_reddit_resource(raw_value)
        resource = MonitoredResource(
            id=None,
            original_input=raw_value,
            canonical_url=normalized.canonical_url,
            subreddit=normalized.subreddit,
            resource_type=normalized.resource_type,
            search_query=normalized.search_query,
            sort_mode=normalized.sort_mode,
        )
        async with self._database.connect() as connection:
            return await ResourceRepository(connection).create(resource)

    async def list_resources(self) -> list[MonitoredResource]:
        async with self._database.connect() as connection:
            return await ResourceRepository(connection).list_all()

    async def toggle_resource(self, resource_id: int, enabled: bool) -> None:
        async with self._database.connect() as connection:
            await ResourceRepository(connection).update_enabled(resource_id, enabled)

    async def delete_resource(self, resource_id: int) -> None:
        async with self._database.connect() as connection:
            await ResourceRepository(connection).delete(resource_id)
