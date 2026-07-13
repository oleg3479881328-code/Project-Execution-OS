from __future__ import annotations

SCHEMA_VERSION = 1

SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS monitored_resources (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  original_input TEXT NOT NULL,
  canonical_url TEXT NOT NULL UNIQUE,
  subreddit TEXT NOT NULL,
  resource_type TEXT NOT NULL,
  search_query TEXT NULL,
  sort_mode TEXT NOT NULL DEFAULT 'new',
  enabled INTEGER NOT NULL DEFAULT 1,
  baseline_completed INTEGER NOT NULL DEFAULT 0,
  last_checked_at TEXT NULL,
  next_check_at TEXT NULL,
  last_success_at TEXT NULL,
  last_error TEXT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS monitored_keywords (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  keyword TEXT NOT NULL,
  normalized_keyword TEXT NOT NULL UNIQUE,
  match_mode TEXT NOT NULL DEFAULT 'contains',
  enabled INTEGER NOT NULL DEFAULT 1,
  case_sensitive INTEGER NOT NULL DEFAULT 0,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS reddit_posts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reddit_id TEXT NOT NULL UNIQUE,
  resource_id INTEGER NOT NULL,
  subreddit TEXT NOT NULL,
  title TEXT NOT NULL,
  body TEXT NOT NULL DEFAULT '',
  permalink TEXT NOT NULL,
  author TEXT NULL,
  created_utc TEXT NOT NULL,
  matched_keywords_json TEXT NOT NULL DEFAULT '[]',
  first_seen_at TEXT NOT NULL,
  delivered_at TEXT NULL,
  opened_at TEXT NULL,
  status TEXT NOT NULL DEFAULT 'new',
  FOREIGN KEY (resource_id) REFERENCES monitored_resources(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS reply_drafts (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reddit_post_id INTEGER NOT NULL,
  provider TEXT NOT NULL,
  model TEXT NOT NULL,
  prompt_version TEXT NOT NULL,
  draft_text TEXT NOT NULL,
  user_instruction TEXT NULL,
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  FOREIGN KEY (reddit_post_id) REFERENCES reddit_posts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS app_settings (
  key TEXT PRIMARY KEY,
  value_json TEXT NOT NULL,
  updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS delivery_events (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  reddit_post_id INTEGER NOT NULL,
  telegram_chat_id TEXT NOT NULL,
  telegram_message_id TEXT NULL,
  delivery_status TEXT NOT NULL,
  error TEXT NULL,
  created_at TEXT NOT NULL,
  FOREIGN KEY (reddit_post_id) REFERENCES reddit_posts(id) ON DELETE CASCADE
);
"""
