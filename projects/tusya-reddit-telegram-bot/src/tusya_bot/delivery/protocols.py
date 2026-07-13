from __future__ import annotations

from typing import Protocol

from tusya_bot.monitoring.models import DeliveryCandidate


class DeliveryService(Protocol):
    async def deliver_candidates(self, candidates: list[DeliveryCandidate]) -> None: ...
