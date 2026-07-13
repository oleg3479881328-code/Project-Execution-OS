# Tusya Reddit Telegram Bot

Single-owner Telegram bot for monitoring selected Reddit resources, notifying the owner about matching posts, and generating saved DeepSeek draft replies without posting anything to Reddit.

## Status

- Phases 1-5 implementation: completed in code
- Live validation with real secrets: pending
- Automatic Reddit publishing: not present

## Features

- Owner-only Telegram access
- Reddit resource CRUD inside Telegram
- Keyword CRUD inside Telegram
- Baseline to avoid old-post spam
- Deterministic polling with per-resource isolation and backoff
- Feed with open/ignore actions
- DeepSeek draft create, regenerate, and refine flows
- SQLite persistence for resources, keywords, posts, drafts, settings, and delivery events
- Docker deployment example
- Backup script and release zip packaging

## Required Configuration

Environment variables:

- `TELEGRAM_BOT_TOKEN`
- `OWNER_TELEGRAM_CHAT_ID`
- `DEEPSEEK_API_KEY`
- `DEEPSEEK_BASE_URL`
- `DEEPSEEK_MODEL`
- `DEEPSEEK_TIMEOUT_SECONDS`
- `DATABASE_PATH`
- `BACKUP_DIR`
- `POLL_INTERVAL_SECONDS`
- `REDDIT_USER_AGENT`
- `REDDIT_TIMEOUT_SECONDS`
- `LOG_LEVEL`

Use [`.env.example`](C:/Users/oleg3/Documents/Reddit%20Tusy/projects/tusya-reddit-telegram-bot/.env.example) as the template. Do not store real secret values in Git.

## Local Run

1. `python -m pip install -e .[dev]`
2. Create `.env` from `.env.example`
3. `python -m tusya_bot run`

Owner workflow:

1. `/start`
2. `/help`
3. `/add_resource`
4. `/add_keyword`
5. `/check_now`
6. `/feed`
7. `✍️ Создать черновик`
8. `/draft_settings`

## Operational Commands

- `/help` - quick owner checklist
- `/status` - monitoring state, counters, cycle timestamps, last error
- `/check_now` - immediate manual polling cycle
- `/feed` - current candidate queue
- `/monitoring_off` - pause scheduled and manual candidate emission
- `/monitoring_on` - resume monitoring after pause

## Docker

Build:

```bash
docker build -t tusya-reddit-telegram-bot:0.1.0-alpha .
```

Run with compose:

```bash
docker compose up -d
```

Persistent mounts:

- `./data:/app/data`
- `./logs:/app/logs`
- `./backups:/app/backups`

Runtime user is non-root. Healthcheck uses:

```bash
python -m tusya_bot healthcheck --database-path /app/data/tusya.sqlite3
```

## Backups And Restore

Create timestamped backup:

```bash
python scripts/backup_sqlite.py --database-path data/tusya.sqlite3 --backup-dir backups
```

Restore procedure:

1. Stop the bot.
2. Replace `data/tusya.sqlite3` with the chosen backup copy.
3. Start the bot again.
4. Run `/status` and `/feed` to verify state.

## Acceptance Without Secrets

Deterministic fake acceptance:

```bash
python scripts/fake_acceptance.py
```

This proves:

- add resource
- add keyword
- baseline sends nothing
- second poll produces one card
- open post
- create/regenerate/refine draft
- restart persistence
- duplicate suppression

## Troubleshooting

- `Access denied.`: wrong Telegram chat ID
- `Операция сейчас недоступна.`: safe runtime error path, inspect `logs/tusya-bot.log`
- `Этот пост больше недоступен.`: stale callback or deleted post
- healthcheck fails: confirm SQLite WAL mode and valid DB path
- no notifications: verify monitoring is enabled and baseline already completed
