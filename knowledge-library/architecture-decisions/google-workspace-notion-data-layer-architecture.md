# Google Workspace + Notion Data Layer Architecture

- **Type:** architecture-decision
- **Lifecycle status:** active
- **Decision date:** 2026-08-21
- **Owner approval:** explicit

## Source and evidence

This decision was approved by the owner after an independent review of the current use of Notion, Google Drive, Google Sheets, website data flows, automation needs, and recent Notion limit friction.

Canonical decision statement from the working discussion:

> Notion is not the universal storage layer. Google Workspace is the primary layer for files and bulk structured operational data; Notion is the human-facing project and knowledge interface. Website, graph, and automation consumers should read from structured sources rather than depend on Notion as the master database.

## Problem

The system increasingly needs to support:

- large entity datasets;
- files, PDFs, photos, video, exports, and archives;
- frequent automated updates;
- website and visualization consumers;
- cross-project reuse;
- human-friendly project management and knowledge navigation;
- protection from UI/database limits in any single SaaS tool.

Using Notion as the universal source of truth creates unnecessary coupling and can turn Notion limits or performance characteristics into a system-wide bottleneck.

## Decision

Use the following default architecture for current projects unless a project has a stronger local requirement:

```text
Google Drive -> Google Sheets -> automation / API -> Notion + websites + graphs + other consumers
```

### Google Drive

Primary durable storage for heavy and binary source materials, including:

- PDFs;
- photos;
- video;
- DOCX and other documents;
- exports;
- archives;
- raw source packages.

### Google Sheets

Default structured operational-data layer for current-scale datasets that benefit from spreadsheet editing and automated access, including:

- entities;
- contacts;
- URLs;
- relationship tables;
- venue and vendor datasets;
- crawl and enrichment results;
- SEO data;
- operational lists and imports.

For these use cases, Google Sheets may act as the current master structured dataset when scale and relational complexity remain appropriate for spreadsheets.

### Notion

Use primarily as the human-facing management and knowledge layer:

- project pages;
- decisions;
- research summaries;
- dashboards;
- documentation;
- curated entity cards;
- links to canonical files and structured datasets.

Do not automatically duplicate all rows or source files into Notion.

### Automation and consumers

Use n8n, Apps Script, APIs, or equivalent existing integrations to move, transform, synchronize, or publish data as needed.

Websites, visualization layers, graph applications, and other machine consumers should normally read from the structured source layer or a purpose-built API/data service rather than depend on Notion as their primary runtime database.

## Evolution rule

Google Sheets is the preferred current structured-data layer, not a permanent universal database.

When data volume, concurrent writes, query complexity, relational integrity, API requirements, or graph workloads exceed spreadsheet suitability, migrate the canonical structured-data layer to a purpose-built database such as PostgreSQL/Supabase or another reviewed fit-for-purpose system.

Target evolution:

```text
Current:
Drive + Sheets -> Notion / websites / graphs / automations

At larger scale:
Drive + database -> Sheets / Notion / websites / graphs / automations
```

After such a migration, Google Sheets may remain an editing, import/export, review, or operational interface rather than the source of truth.

## Applies To

- cross-project information architecture;
- entity databases;
- SEO/AEO data pipelines;
- wedding-industry ecosystem datasets;
- website content/data feeds;
- graph and visualization projects;
- research/enrichment pipelines;
- automation workflows;
- projects mixing large files with structured metadata.

## Triggers

Load this decision when:

- choosing between Notion, Google Drive, and Google Sheets;
- designing a new shared dataset;
- deciding where source files should live;
- exposing project data to a website or application;
- building sync or enrichment automation;
- a Notion database begins to grow materially;
- the same data needs to serve both humans and software.

## Do Not Load When

Do not apply mechanically when:

- the project is a small Notion-only knowledge workspace with no meaningful external data flow;
- the project already has a purpose-built database that is clearly the canonical source;
- the artifact is project-specific and its existing durable layer is already appropriate.

## When to use

Use this architecture by default for multi-tool projects where files, structured datasets, human project management, and machine consumers coexist.

## When not to use

Do not force Google Sheets into workloads that require strong transactions, complex relational constraints, high-frequency concurrency, large-scale graph queries, or database-grade runtime guarantees.

Do not use Notion as a bulk-data mirror merely for completeness.

## Adaptation notes

- Keep canonical IDs stable across Sheets, Notion, websites, and graph layers.
- Store canonical file locations rather than unnecessary duplicate binary copies.
- Synchronize only the subset of data that materially improves the Notion working interface.
- Prefer one-way publication where possible; introduce bidirectional sync only with explicit conflict rules.
- Preserve source traceability when data is transformed or enriched.

## Risks

- Sheets can itself become a bottleneck if treated as a database beyond its appropriate scale.
- Bidirectional synchronization can create conflicts and duplicate truth.
- Manual edits across multiple surfaces require clear ownership of canonical fields.
- Migration to a database should happen before spreadsheet limitations become production-critical.

## Review status

Reviewed in discussion on 2026-08-21 and explicitly approved by the owner for system-wide use.

## Related standards

- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/REFERENCE_IDEA_CAPTURE_STANDARD.md`
- `knowledge-library/README.md`
