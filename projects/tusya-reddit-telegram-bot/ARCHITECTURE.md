# Architecture

## Runtime model

Один долгоживущий Python-процесс содержит Telegram application и async monitoring scheduler. Для MVP отдельный FastAPI-сервис не обязателен: health endpoint можно добавить позже, если deployment-платформа требует HTTP health check.

Компоненты:

1. Telegram UI layer
2. Application services
3. Monitoring engine
4. Reddit adapter
5. Keyword matcher
6. AI draft service
7. Persistence layer
8. Scheduler and observability

## Package layout

```text
projects/tusya-reddit-telegram-bot/
  pyproject.toml
  README.md
  PROJECT.md
  PROJECT_STATE.md
  ARCHITECTURE.md
  IMPLEMENTATION_PLAN.md
  .env.example
  src/tusya_bot/
    __main__.py
    config.py
    logging_config.py
    bot/
      application.py
      commands.py
      callbacks.py
      conversations.py
      keyboards.py
      rendering.py
      auth.py
    domain/
      models.py
      enums.py
      errors.py
    services/
      resource_service.py
      keyword_service.py
      feed_service.py
      settings_service.py
      draft_service.py
    monitoring/
      scheduler.py
      polling.py
      reddit_client.py
      normalization.py
      matcher.py
      delivery.py
    db/
      engine.py
      schema.py
      migrations.py
      repositories.py
    ai/
      client.py
      prompts.py
      schemas.py
  tests/
  logs/
```

## Data model

### monitored_resources

- id INTEGER PK
- original_input TEXT NOT NULL
- canonical_url TEXT NOT NULL UNIQUE
- subreddit TEXT NOT NULL
- resource_type TEXT NOT NULL
- search_query TEXT NULL
- sort_mode TEXT NOT NULL DEFAULT 'new'
- enabled INTEGER NOT NULL DEFAULT 1
- baseline_completed INTEGER NOT NULL DEFAULT 0
- last_checked_at TEXT NULL
- next_check_at TEXT NULL
- last_success_at TEXT NULL
- last_error TEXT NULL
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

### monitored_keywords

- id INTEGER PK
- keyword TEXT NOT NULL
- normalized_keyword TEXT NOT NULL UNIQUE
- match_mode TEXT NOT NULL DEFAULT 'contains'
- enabled INTEGER NOT NULL DEFAULT 1
- case_sensitive INTEGER NOT NULL DEFAULT 0
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

### reddit_posts

- id INTEGER PK
- reddit_id TEXT NOT NULL UNIQUE
- resource_id INTEGER NOT NULL FK
- subreddit TEXT NOT NULL
- title TEXT NOT NULL
- body TEXT NOT NULL DEFAULT ''
- permalink TEXT NOT NULL
- author TEXT NULL
- created_utc TEXT NOT NULL
- matched_keywords_json TEXT NOT NULL DEFAULT '[]'
- first_seen_at TEXT NOT NULL
- delivered_at TEXT NULL
- opened_at TEXT NULL
- status TEXT NOT NULL DEFAULT 'new'

### reply_drafts

- id INTEGER PK
- reddit_post_id INTEGER NOT NULL FK
- provider TEXT NOT NULL
- model TEXT NOT NULL
- prompt_version TEXT NOT NULL
- draft_text TEXT NOT NULL
- user_instruction TEXT NULL
- created_at TEXT NOT NULL
- updated_at TEXT NOT NULL

### app_settings

- key TEXT PK
- value_json TEXT NOT NULL
- updated_at TEXT NOT NULL

### delivery_events

- id INTEGER PK
- reddit_post_id INTEGER NOT NULL FK
- telegram_chat_id TEXT NOT NULL
- telegram_message_id TEXT NULL
- delivery_status TEXT NOT NULL
- error TEXT NULL
- created_at TEXT NOT NULL

## Reddit source strategy

MVP adapter accepts:

- `r/<subreddit>`
- subreddit URL
- `/new/` URL
- Reddit search URL

Normalization removes transient parameters such as `cId` and `iId`, preserves semantic query parameters, and creates a canonical resource identity.

Polling fetches newest posts for every active resource. The adapter must be isolated behind a protocol so the transport can be changed later without touching domain logic.

Required behavior:

- explicit user agent;
- bounded timeout;
- non-200 handling;
- schema validation;
- retry with exponential backoff and jitter;
- per-resource failure isolation;
- no logging of secrets;
- no duplicate delivery.

## Matching rules

Matching input: normalized `title + '\n' + body`.

Modes:

- contains: normalized substring;
- phrase: phrase with whitespace normalization;
- exact: token/word-boundary match, not whole-post equality.

At least one enabled keyword is sufficient for a match. Store all matched keywords. Case sensitivity is configurable per keyword.

## Baseline algorithm

For a resource with `baseline_completed = false`:

1. Fetch current newest posts.
2. Insert their Reddit IDs and metadata.
3. Do not deliver Telegram notifications.
4. Mark baseline completed only after successful transaction.

Every later poll:

1. Fetch newest posts.
2. Sort oldest to newest before processing.
3. Skip existing reddit_id values.
4. Persist unseen posts.
5. Match against enabled keywords.
6. Deliver matching posts once.
7. Record delivery event and delivered_at atomically where practical.

## Telegram UX state machine

Global commands:

- `/start`
- `/menu`
- `/cancel`
- `/status`

Conversation states:

- ADD_RESOURCE_WAIT_INPUT
- ADD_RESOURCE_CONFIRM
- EDIT_RESOURCE_WAIT_VALUE
- DELETE_RESOURCE_CONFIRM
- ADD_KEYWORD_WAIT_INPUT
- ADD_KEYWORD_CONFIRM
- EDIT_KEYWORD_WAIT_VALUE
- DELETE_KEYWORD_CONFIRM
- DRAFT_WAIT_INSTRUCTION
- SETTINGS_WAIT_VALUE

Callback payloads must be compact IDs, never entire URLs or post bodies.

## New-post card

Message contains:

- title;
- subreddit;
- matched keywords;
- publication time;
- short excerpt.

Buttons:

- `📖 Открыть в боте`
- `🔗 Открыть Reddit`
- `✍️ Создать черновик`
- `🙈 Игнорировать`

## GPT draft contract

Input:

- title;
- body;
- subreddit;
- matched keywords;
- configured language, tone and length;
- optional owner instruction.

Output is plain draft text only. No claim that it was posted. The service stores provider, model and prompt version.

## Owner authorization

Every command, message and callback must pass an owner-chat-ID check before any action. Unauthorized users receive a neutral denial and no data.

## Deployment

Recommended MVP deployment: one Docker container on an always-on host with persistent volume for SQLite and environment secrets.

Required persistent paths:

- database file;
- logs;
- optional backup directory.

Required environment:

- TELEGRAM_BOT_TOKEN
- OWNER_TELEGRAM_CHAT_ID
- OPENAI_API_KEY
- OPENAI_MODEL
- DATABASE_PATH
- POLL_INTERVAL_SECONDS
- LOG_LEVEL

## Reliability rules

- SQLite WAL mode.
- Database transactions around baseline and delivery state changes.
- Scheduler prevents overlapping poll cycles.
- One resource failure does not abort the cycle.
- Poll interval has a safe lower bound.
- History retention is bounded/configurable.
- Graceful shutdown closes scheduler, Telegram client and DB.
