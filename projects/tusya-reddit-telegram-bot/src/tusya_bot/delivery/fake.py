from __future__ import annotations

from tusya_bot.delivery.protocols import DeliveryService
from tusya_bot.monitoring.models import DeliveryCandidate


class CollectingDeliveryService(DeliveryService):
    def __init__(self) -> None:
        self.emitted: list[DeliveryCandidate] = []
        self.last_batch_failures = 0

    async def deliver_candidates(self, candidates: list[DeliveryCandidate]) -> None:
        self.last_batch_failures = 0
        self.emitted.extend(candidates)
