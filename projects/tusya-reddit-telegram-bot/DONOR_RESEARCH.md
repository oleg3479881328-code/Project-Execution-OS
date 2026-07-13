# Donor Research

Date: 2026-07-13

## Selection rule

Donors are patterns and code references, not drop-in dependencies. Before copying code, the executor must verify license, current maintenance state, security, and compatibility with our async architecture.

## Donor 1 — JCarlosWolf/reddit-telegram-monitoring-bot

Repository:
https://github.com/JCarlosWolf/reddit-telegram-monitoring-bot

Useful patterns:

- clean separation into Reddit source, filters, processor, Telegram delivery and SQLite storage;
- direct Reddit-to-Telegram notification flow;
- persistence of seen IDs to prevent duplicates;
- environment-based configuration;
- practical message format with title and direct link.

Do not copy blindly:

- synchronous infinite loop with `time.sleep`;
- background thread for monitoring;
- broad exception handling;
- direct scraping assumptions;
- fixed configuration instead of Telegram CRUD;
- no baseline transaction or owner authorization.

Adaptation decision:

Reuse the separation-of-concerns idea and SQLite deduplication pattern. Replace the thread/sleep loop with an async scheduler and repository transactions.

## Donor 2 — jheilos/reddit-keyword-notifier

Repository:
https://github.com/jheilos/reddit-keyword-notifier

Useful patterns:

- keyword matching over title and body;
- Telegram notification containing subreddit, title and link;
- Docker deployment;
- reconnect behavior;
- PRAW stream as a possible future Reddit transport.

Do not copy blindly:

- static keywords/subreddits from environment;
- no editable database;
- no stored post history or draft history;
- requires Reddit API credentials;
- one-way notifier rather than interactive management bot.

Adaptation decision:

Keep its simple notification contract and Docker pattern. Preserve our transport abstraction so we can start with public polling and later switch to PRAW/OAuth if reliability requires it.

## Donor 3 — python-telegram-bot project patterns

Official project:
https://github.com/python-telegram-bot/python-telegram-bot

Useful patterns:

- async `Application` lifecycle;
- `ConversationHandler` for add/edit flows;
- inline callback queries;
- `JobQueue` as an alternative to a separate scheduler;
- error handlers and graceful shutdown.

Adaptation decision:

Use the official async application model. Prefer compact callback IDs and service-layer calls from handlers. Do not put SQL or Reddit requests directly in Telegram handlers.

## Donor 4 — DeepSeek official API compatibility

Official docs:
https://api-docs.deepseek.com/

Useful pattern:

- OpenAI-compatible SDK with `base_url=https://api.deepseek.com`;
- current model family `deepseek-v4-flash` and `deepseek-v4-pro`;
- explicit thinking switch;
- standard `/chat/completions` endpoint.

Adaptation decision:

Use `deepseek-v4-flash` with thinking disabled for fast reply drafts. Keep the model configurable and hide the SDK behind `DraftModelClient`.

## Final donor strategy

Adopt:

- modular pipeline from Donor 1;
- matching/notification simplicity and Docker idea from Donor 2;
- async Telegram lifecycle from the official python-telegram-bot project;
- DeepSeek official OpenAI-compatible integration.

Reject:

- synchronous `while True` monitoring;
- static `.env` resource/keyword lists;
- automatic Reddit posting;
- unbounded seen-ID storage;
- secrets in code or logs;
- donor architecture copied wholesale.
