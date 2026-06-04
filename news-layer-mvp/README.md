# News Layer MVP

Minimal Miniflux-based news intake and AI-prep pipeline for local use.

## Goal

Prove this local workflow:

1. Miniflux collects feeds.
2. `pull_miniflux_articles.py` exports normalized JSONL.
3. `build_ai_bundle.py` creates an analysis bundle.
4. `generate_digest_prompt.py` prepares an LLM prompt.
5. `export_source_pack.py` exports URLs for NotebookLM.

This module intentionally does not include UI, bots, paid APIs, or custom feed infrastructure.

## Files

- `env.example` - local environment template
- `docker-compose.yml` - Miniflux + PostgreSQL stack
- `sources/starter_sources.md` - starter feed list with verification notes
- `sources/starter_sources.opml` - starter OPML import file
- `scripts/` - pipeline scripts
- `outputs/` - generated artifacts
- `logs/NEWS_LAYER_MVP_LOG.md` - execution log

## Setup

1. Copy `env.example` to `.env`.
2. Fill in `MINIFLUX_AUTH_VALUE` after you create an API key in Miniflux.
3. Start the local stack:

```powershell
docker compose up -d
```

4. Open [http://localhost:8080](http://localhost:8080).
5. Create the first Miniflux user when prompted.
6. In Miniflux, create an API key:
   `Settings -> API Keys -> Create API Key`
7. Import starter feeds:
   `Settings -> Import -> OPML`

## Script Usage

Run from the repository root:

```powershell
python news-layer-mvp/scripts/pull_miniflux_articles.py
python news-layer-mvp/scripts/build_ai_bundle.py --input news-layer-mvp/outputs/articles_YYYYMMDD_HHMMSS.jsonl
python news-layer-mvp/scripts/generate_digest_prompt.py --input news-layer-mvp/outputs/articles_YYYYMMDD_HHMMSS.jsonl
python news-layer-mvp/scripts/export_source_pack.py --input news-layer-mvp/outputs/articles_YYYYMMDD_HHMMSS.jsonl
```

Useful flags:

- `--category ai`
- `--max-articles 25`
- `--include-read`
- `--lookback-hours 24`
- `--output-dir news-layer-mvp/outputs`

## Validation Notes

- The Python scripts were validated for syntax locally.
- Downstream scripts were run against a synthetic JSONL sample.
- A live Miniflux API pull was not executed in this repository because no local Miniflux instance or API token was provided in this task.

## Optional RSSHub

RSSHub is intentionally not enabled by default in `docker-compose.yml`.
If a source has no native RSS feed, add RSSHub later as a bounded follow-up.
