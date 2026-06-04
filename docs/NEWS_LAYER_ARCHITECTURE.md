# News Layer Architecture

## Purpose

This document defines the initial architecture decision for the News Layer.

The system must not invent a custom news collector from scratch while strong open-source RSS and feed-reader infrastructure already exists.

## Status

`candidate`

## Decision

Use proven open-source intake tools for news collection, then build the Project Execution OS value layer on top.

Initial preferred stack:

```text
RSSHub
  ↓
Miniflux
  ↓
AI Analysis Layer
  ↓
Digest / Timeline / Watchlist / Source Pack / Decision Memo
  ↓
News Library / Reference Layer / Knowledge Layer / Project Layer
```

## Components

### RSSHub

Role: source expansion and RSS generation.

Use RSSHub when a useful source does not expose a clean native RSS feed.

RSSHub is not the analysis layer. It is a feed-source bridge.

### Miniflux

Role: primary intake, feed storage, filtering, search, API access, webhooks, article extraction, and automation integration.

Miniflux is the preferred intake core because it is simple, lightweight, API-friendly, webhook-friendly, and built around PostgreSQL.

### FreshRSS

Role: fallback or alternative intake core.

FreshRSS is strong when multi-user RSS reading, tags, extensions, web scraping, and a more full-featured reader interface matter more than a minimal automation-friendly core.

### Folo

Role: product/interface reference, not core infrastructure.

Folo is useful as a reference for AI-assisted reading, summaries, translation, discovery, and modern timeline experience.

Do not depend on Folo as the first system foundation unless future testing proves it fits better than Miniflux for the owner’s workflow.

## Build vs Reuse Rule

Do not build:

- feed fetching;
- RSS parsing;
- feed storage;
- basic article list UI;
- basic feed filtering;
- basic feed import/export;
- basic article extraction;
- notification/webhook plumbing.

Reuse existing tools for those.

Build only the owner-specific intelligence layer:

- digest contracts;
- source scoring;
- claim/fact separation;
- timeline reconstruction;
- watchlist logic;
- NotebookLM source-pack export;
- personal/project relevance scoring;
- decision memo output;
- storage routing into Reference, Knowledge, Project, or News Library layers.

## MVP Direction

MVP should be ugly but working.

Minimum useful version:

1. Miniflux running locally or on a small server.
2. RSSHub available for sources without RSS.
3. A curated OPML/source list for initial topics.
4. A script or agent routine pulls unread/recent articles from Miniflux API.
5. AI groups articles by topic.
6. AI outputs a digest with confidence and practical meaning.
7. Source pack can be exported as clean URLs for NotebookLM.

Do not start with a custom UI.

Do not start with a giant database schema.

Do not start with full automation.

First prove the intake → analysis → digest loop.

## Initial Topic Buckets

Suggested first buckets:

- politics;
- economy;
- law;
- immigration;
- AI;
- technology;
- markets;
- local;
- project-relevant platforms.

## Data Flow

```text
Sources
  ↓
RSS / RSSHub routes
  ↓
Miniflux categories, filters, bookmarks, search
  ↓
AI processing
  ↓
Processed outputs
  ↓
Storage decision
```

## Output Contracts

The AI layer should produce:

- `quick_brief`;
- `digest`;
- `timeline`;
- `watchlist`;
- `source_pack`;
- `decision_memo`.

These output types are defined in `docs/NEWS_LAYER.md`.

## Storage Decision

Each processed item must route to one of:

- ignore;
- raw reference;
- processed news archive;
- watchlist;
- project implication;
- central reusable knowledge candidate.

## Why This Architecture

This architecture avoids wasting work on solved infrastructure.

Miniflux and RSSHub handle the boring but critical intake layer.

Project Execution OS should focus on the non-generic value: making the news digestible, useful, source-backed, and decision-oriented.

## Risks

- RSS coverage is incomplete for some modern platforms.
- Some sites block scraping or change markup.
- RSSHub routes may break.
- Miniflux requires PostgreSQL.
- Legal/political topics require extra source discipline.
- AI summaries may overstate certainty if source scoring is weak.

## Next Implementation Packet

Create a Codex-ready MVP packet for:

1. local Miniflux setup;
2. optional RSSHub setup;
3. initial OPML/source list;
4. Miniflux API pull script;
5. digest generation contract;
6. source-pack export.

## Final Rule

Use open-source intake. Build only the intelligence layer.
