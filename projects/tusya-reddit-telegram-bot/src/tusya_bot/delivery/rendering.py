from __future__ import annotations

import html
import json
from datetime import datetime

from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from tusya_bot.bot.callbacks import encode_callback
from tusya_bot.domain.enums import PostStatus
from tusya_bot.domain.models import RedditPost
from tusya_bot.monitoring.models import DeliveryCandidate

MAX_TELEGRAM_TEXT = 3500
FEED_PAGE_SIZE = 5


def render_candidate_card(candidate: DeliveryCandidate) -> str:
    post = candidate.post
    lines = [
        f"<b>{escape_telegram_html(post.title)}</b>",
        f"r/{escape_telegram_html(post.subreddit)}",
        f"Ключевые слова: {escape_telegram_html(', '.join(candidate.matched_keywords))}",
        f"Опубликовано: {escape_telegram_html(_format_timestamp(post.created_utc))}",
        f"Статус: {escape_telegram_html(_status_label(post.status))}",
        "Черновик не опубликован.",
    ]

    excerpt = build_excerpt(post.body)
    if excerpt:
        lines.append("")
        lines.append(f"<i>{escape_telegram_html(excerpt)}</i>")

    return "\n".join(lines)


def render_full_post(post: RedditPost) -> str:
    matched_keywords = ", ".join(_matched_keywords(post)) or "-"
    body = post.body.strip() or "Тело поста пустое."
    return "\n".join(
        [
            f"<b>{escape_telegram_html(post.title)}</b>",
            f"r/{escape_telegram_html(post.subreddit)}",
            f"Статус: {escape_telegram_html(_status_label(post.status))}",
            f"Ключевые слова: {escape_telegram_html(matched_keywords)}",
            f'Ссылка: <a href="{html.escape(post.permalink, quote=True)}">Reddit</a>',
            "",
            escape_telegram_html(body),
        ]
    )


def render_feed_page(posts: list[RedditPost], *, page: int, total_pages: int) -> str:
    if not posts:
        return "Лента пока пуста."

    lines = [f"<b>Лента</b> · страница {page + 1}/{max(total_pages, 1)}", ""]
    for index, post in enumerate(posts, start=1):
        lines.append(
            f"{index}. {_status_emoji(post.status)} "
            f"<b>{escape_telegram_html(post.title)}</b>\n"
            f"r/{escape_telegram_html(post.subreddit)} · "
            f"{escape_telegram_html(_format_timestamp(post.created_utc))}"
        )
    return "\n\n".join(lines)


def build_delivery_keyboard(post_id: int, permalink: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "📖 Открыть в боте",
                    callback_data=encode_callback("open", post_id),
                ),
                InlineKeyboardButton("🔗 Открыть Reddit", url=permalink),
            ],
            [
                InlineKeyboardButton(
                    "✍️ Создать черновик",
                    callback_data=encode_callback("draft", post_id),
                ),
                InlineKeyboardButton(
                    "🙈 Игнорировать",
                    callback_data=encode_callback("ignore", post_id),
                ),
            ],
        ]
    )


def build_feed_keyboard(
    posts: list[RedditPost],
    *,
    page: int,
    total_pages: int,
) -> InlineKeyboardMarkup:
    rows: list[list[InlineKeyboardButton]] = []
    for index, post in enumerate(posts, start=1):
        rows.append(
            [
                InlineKeyboardButton(
                    f"{index}. Открыть",
                    callback_data=encode_callback("open", post.id or 0, page=page),
                ),
                InlineKeyboardButton(
                    _status_emoji(post.status),
                    callback_data=encode_callback("noop", post.id or 0, page=page),
                ),
            ]
        )

    pagination_row: list[InlineKeyboardButton] = []
    if page > 0:
        pagination_row.append(
            InlineKeyboardButton("←", callback_data=encode_callback("feed", 0, page=page - 1))
        )
    if page + 1 < total_pages:
        pagination_row.append(
            InlineKeyboardButton("→", callback_data=encode_callback("feed", 0, page=page + 1))
        )
    if pagination_row:
        rows.append(pagination_row)
    return InlineKeyboardMarkup(rows)


def build_post_navigation_keyboard(
    post: RedditPost,
    *,
    page: int | None = None,
) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton("🔗 Открыть Reddit", url=post.permalink),
            InlineKeyboardButton(
                "🙈 Игнорировать",
                callback_data=encode_callback("ignore", post.id or 0, page=page),
            ),
        ],
        [
            InlineKeyboardButton(
                "✍️ Создать черновик",
                callback_data=encode_callback("draft", post.id or 0, page=page),
            )
        ],
        [
            InlineKeyboardButton(
                "🔁 Регенерировать",
                callback_data=encode_callback("redraft", post.id or 0, page=page),
            ),
            InlineKeyboardButton(
                "🛠 Уточнить",
                callback_data=encode_callback("refine", post.id or 0, page=page),
            ),
        ],
    ]
    if page is not None:
        rows.append(
            [
                InlineKeyboardButton(
                    "← Назад к ленте",
                    callback_data=encode_callback("feed", 0, page=page),
                )
            ]
        )
    return InlineKeyboardMarkup(rows)


def escape_telegram_html(value: str) -> str:
    return html.escape(value, quote=False)


def chunk_text(value: str, *, limit: int = MAX_TELEGRAM_TEXT) -> list[str]:
    text = value.strip()
    if not text:
        return [""]
    chunks: list[str] = []
    while len(text) > limit:
        split_at = text.rfind("\n", 0, limit)
        if split_at == -1:
            split_at = text.rfind(" ", 0, limit)
        if split_at == -1 or split_at < limit // 2:
            split_at = limit
        chunks.append(text[:split_at].strip())
        text = text[split_at:].strip()
    chunks.append(text)
    return chunks


def build_excerpt(value: str, *, limit: int = 220) -> str:
    cleaned = " ".join(value.split())
    if not cleaned:
        return ""
    if len(cleaned) <= limit:
        return cleaned
    return f"{cleaned[: limit - 1].rstrip()}…"


def _matched_keywords(post: RedditPost) -> tuple[str, ...]:
    loaded = json.loads(post.matched_keywords_json)
    return tuple(str(item) for item in loaded)


def _format_timestamp(value: str) -> str:
    return datetime.fromisoformat(value).strftime("%Y-%m-%d %H:%M UTC")


def _status_label(status: PostStatus) -> str:
    return {
        PostStatus.NEW: "Новый",
        PostStatus.OPENED: "Открыт",
        PostStatus.IGNORED: "Игнорирован",
        PostStatus.DRAFTED: "Черновик создан",
    }[status]


def _status_emoji(status: PostStatus) -> str:
    return {
        PostStatus.NEW: "🆕",
        PostStatus.OPENED: "📖",
        PostStatus.IGNORED: "🙈",
        PostStatus.DRAFTED: "✍️",
    }[status]


def render_draft_text(
    *,
    draft_text: str,
    provider: str,
    model: str,
    prompt_version: str,
    owner_instruction: str | None,
) -> str:
    lines = [
        "<b>Черновик ответа</b>",
        "Черновик не опубликован.",
        f"Провайдер: {escape_telegram_html(provider)}",
        f"Модель: {escape_telegram_html(model)}",
        f"Версия промпта: {escape_telegram_html(prompt_version)}",
    ]
    if owner_instruction:
        lines.append(f"Уточнение: {escape_telegram_html(owner_instruction)}")
    lines.extend(["", escape_telegram_html(draft_text)])
    return "\n".join(lines)


def build_draft_keyboard(post_id: int, *, page: int | None = None) -> InlineKeyboardMarkup:
    rows = [
        [
            InlineKeyboardButton(
                "🔁 Регенерировать",
                callback_data=encode_callback("redraft", post_id, page=page),
            ),
            InlineKeyboardButton(
                "🛠 Уточнить",
                callback_data=encode_callback("refine", post_id, page=page),
            ),
        ]
    ]
    if page is not None:
        rows.append(
            [
                InlineKeyboardButton(
                    "← Назад к посту",
                    callback_data=encode_callback("open", post_id, page=page),
                )
            ]
        )
    return InlineKeyboardMarkup(rows)
