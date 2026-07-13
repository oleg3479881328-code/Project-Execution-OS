from __future__ import annotations

import logging

from telegram import Bot
from telegram.constants import ParseMode
from telegram.error import TelegramError

from tusya_bot.delivery.protocols import DeliveryService
from tusya_bot.delivery.rendering import build_delivery_keyboard, render_candidate_card
from tusya_bot.monitoring.models import DeliveryCandidate
from tusya_bot.services.post_service import PostService

logger = logging.getLogger(__name__)


class TelegramDeliveryService(DeliveryService):
    def __init__(
        self,
        *,
        bot: Bot,
        owner_chat_id: int,
        post_service: PostService,
    ) -> None:
        self._bot = bot
        self._owner_chat_id = owner_chat_id
        self._post_service = post_service
        self.last_batch_failures = 0

    async def deliver_candidates(self, candidates: list[DeliveryCandidate]) -> None:
        self.last_batch_failures = 0
        for candidate in candidates:
            post_id = candidate.post.id
            if post_id is None:
                continue
            if await self._post_service.already_delivered(post_id):
                continue
            try:
                message = await self._bot.send_message(
                    chat_id=self._owner_chat_id,
                    text=render_candidate_card(candidate),
                    parse_mode=ParseMode.HTML,
                    reply_markup=build_delivery_keyboard(
                        post_id,
                        candidate.post.permalink,
                    ),
                    disable_web_page_preview=True,
                )
            except TelegramError as error:
                logger.warning("Telegram delivery failed for post %s: %s", post_id, error)
                self.last_batch_failures += 1
                await self._post_service.record_delivery_failure(
                    post_id=post_id,
                    telegram_chat_id=self._owner_chat_id,
                    error="Telegram delivery failed.",
                )
                continue

            await self._post_service.record_delivery_success(
                post_id=post_id,
                telegram_chat_id=self._owner_chat_id,
                telegram_message_id=message.message_id,
            )
