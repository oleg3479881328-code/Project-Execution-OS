# Codex Packet — News Layer MVP

## Mission

Build the first working MVP loop for the News Layer:

```text
Miniflux
  ↓
recent or unread articles through the Miniflux API
  ↓
AI-ready article bundle
  ↓
digest / source pack / watchlist candidates
```

This packet is intentionally narrow. Do not build a custom news platform.

## Status

`ready_for_execution`

## Execution Principle

MVP first.

A rough working pipeline is better than a polished architecture that does not run.

## Hard Constraints

- Do not build a custom RSS reader.
- Do not build a custom UI.
- Do not build a custom database unless absolutely required.
- Do not replace Miniflux intake with custom feed scraping.
- Do not implement RSSHub unless it is needed for a source without RSS.
- Do not add paid APIs in the MVP.
- Do not store real credentials in the repository.
- Logs must live in the project root or module root.
- All execution decisions, errors, and fixes must be logged.

## Preferred Stack

- Miniflux as primary intake core.
- RSSHub as optional source expansion layer.
- Python for MVP scripts unless the repository already standardizes another runtime.
- Local configuration through environment variables.
- Markdown and JSONL for first outputs.

## Expected Folder Structure

Create a bounded module:

```text
news-layer-mvp/
├── README.md
├── env.example
├── docker-compose.yml
├── sources/
│   ├── starter_sources.md
│   └── starter_sources.opml
├── scripts/
│   ├── pull_miniflux_articles.py
│   ├── build_ai_bundle.py
│   ├── export_source_pack.py
│   └── generate_digest_prompt.py
├── outputs/
│   ├── .gitkeep
│   └── README.md
└── logs/
    └── NEWS_LAYER_MVP_LOG.md
```

If the repo already has a better equivalent structure, adapt minimally and explain the reason in the log.

## Configuration Example

Create `env.example` only. Do not create a real local config file with private values.

Required fields:

```text
MINIFLUX_BASE_URL=http://localhost:8080
MINIFLUX_AUTH_VALUE=replace_with_local_value
NEWS_OUTPUT_DIR=outputs
NEWS_MAX_ARTICLES=50
NEWS_DEFAULT_CATEGORY=all
```

Optional fields:

```text
RSSHUB_BASE_URL=http://localhost:1200
NEWS_INCLUDE_READ=false
NEWS_LOOKBACK_HOURS=48
```

## Docker Compose MVP

Create `docker-compose.yml` for local Miniflux plus PostgreSQL.

Optional RSSHub service can be included but disabled or clearly marked optional.

Acceptance:

- local compose setup starts Miniflux and Postgres;
- README explains where to open Miniflux locally;
- README explains how to create the local auth value for API calls.

## Starter Sources

Create starter source list with conservative sources only.

Buckets:

- politics;
- economy;
- law;
- immigration;
- AI;
- technology;
- markets;
- local.

Do not overfill. Use a small starter set and leave TODO markers.

Create:

- `starter_sources.md` for human-readable source plan;
- `starter_sources.opml` for import.

If exact feed URL is uncertain, do not invent it. Put it under `TODO_VERIFY` in markdown, not in OPML.

## Script 1 — Pull Miniflux Articles

Create `scripts/pull_miniflux_articles.py`.

Required behavior:

- read config from environment variables;
- call Miniflux REST API;
- fetch recent or unread entries;
- normalize articles into JSONL;
- include title, url, author, published_at, feed title, category if available, status, and summary/content snippet;
- write output to `outputs/articles_<timestamp>.jsonl`;
- write execution notes to `logs/NEWS_LAYER_MVP_LOG.md`;
- handle HTTP errors clearly.

No AI call in this script.

## Script 2 — Build AI Bundle

Create `scripts/build_ai_bundle.py`.

Required behavior:

- read latest or specified JSONL article file;
- deduplicate by canonical URL/title;
- group roughly by feed/category/domain;
- create a Markdown bundle for AI analysis;
- write to `outputs/ai_bundle_<timestamp>.md`.

Bundle must include:

```text
# AI News Bundle

## Instructions For Analysis

Produce:
1. What happened
2. What is confirmed
3. What is uncertain
4. Why it matters
5. Practical meaning
6. Confidence
7. What to watch next
8. Source pack

## Articles
...
```

## Script 3 — Export Source Pack

Create `scripts/export_source_pack.py`.

Required behavior:

- read latest or specified JSONL article file;
- export clean URLs only;
- deduplicate URLs;
- write `outputs/source_pack_<timestamp>.txt`;
- no descriptions in source pack file.

This matches NotebookLM export behavior.

## Script 4 — Generate Digest Prompt

Create `scripts/generate_digest_prompt.py`.

Required behavior:

- produce a reusable prompt file from an AI bundle;
- prompt must instruct the model to output a readable digest, not a headline dump;
- prompt must require confidence labels;
- prompt must require source links grouped by item;
- write to `outputs/digest_prompt_<timestamp>.md`.

No model API call required in MVP.

## README Requirements

`news-layer-mvp/README.md` must include:

1. what this MVP does;
2. what it does not do;
3. setup steps;
4. Miniflux local auth setup steps;
5. how to import OPML;
6. how to run scripts;
7. expected outputs;
8. troubleshooting;
9. next steps.

Keep it practical.

## Logging Requirements

Create `logs/NEWS_LAYER_MVP_LOG.md`.

It must record:

- created files;
- commands tested;
- assumptions;
- errors;
- fixes;
- skipped items;
- next recommended execution step.

Do not claim commands were tested unless actually tested.

If not tested, write `generated_not_executed`.

## Acceptance Criteria

MVP is accepted when:

1. local Miniflux setup instructions exist;
2. scripts exist and are runnable;
3. `env.example` exists without private values;
4. source OPML exists with only verified feed URLs;
5. article pull script writes JSONL;
6. AI bundle script writes Markdown;
7. source pack script writes clean URL list;
8. digest prompt script writes reusable digest prompt;
9. logs clearly distinguish generated state from executed state;
10. no custom news reader UI was built.

## Non-Goals

- automated scheduled monitoring;
- web dashboard;
- user accounts;
- permanent News Library schema;
- vector database;
- semantic search;
- direct LLM API calls;
- Telegram bot;
- email digest automation;
- multi-agent routing.

These come later only after the basic loop works.

## Suggested First Manual Test

After implementation:

1. start Miniflux;
2. import OPML;
3. wait for feeds to fetch;
4. create the local API auth value;
5. run pull script;
6. run bundle script;
7. run source-pack script;
8. paste digest prompt into ChatGPT or another model;
9. verify the output is actually useful.

## Final Instruction To Codex

Implement the smallest working version.

Do not polish.

Do not expand scope.

Do not invent custom infrastructure where Miniflux or RSSHub already solves the intake problem.
