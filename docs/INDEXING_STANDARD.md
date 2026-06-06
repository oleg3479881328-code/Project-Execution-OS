# Indexing Layer Standard

## Purpose

This standard defines the structural indexing layer for `Project Execution OS`.

Its goal is to keep navigation current, make repository knowledge machine-readable, prepare a semantic-search corpus, and prevent agents from repeatedly scanning the entire repository.

## Core Rule

Use layered indexing:

```text
stable door
  -> live router
  -> curated section indexes
  -> generated machine index
  -> semantic-ready chunk corpus
  -> optional embeddings runtime
  -> optional graph-memory layer
```

No generated index replaces canonical source files.

## Required Artifacts

### Curated navigation

- `START_HERE.md`
- `docs/ROUTER.md`
- `PROJECT_INDEX.md`
- `blocks/PROJECT_INDEX.md`
- `knowledge-library/PROJECT_INDEX.md`
- `skills/PROJECT_INDEX.md`
- `agent-library/PROJECT_INDEX.md`

### Generated indexing artifacts

- `indexes/system-index.json`
- `indexes/semantic-documents.jsonl`
- `indexes/BLOCK_CATALOG.generated.md`
- `indexes/KNOWLEDGE_CATALOG.generated.md`

### Automation

- `scripts/build_system_index.py`
- `.github/workflows/system-index.yml`

## Structural Indexing Rule

After a meaningful structural change:

1. update the relevant curated index when human-readable navigation changed;
2. regenerate machine-readable artifacts;
3. verify that new blocks contain `BLOCK.md`;
4. verify that paths remain valid;
5. verify statuses and dated snapshots where applicable;
6. preserve canonical files as the source of truth.

## Generated Index Scope

The generated index may include:

- path;
- title;
- artifact type;
- domain;
- lifecycle status when detected;
- updated or captured date when detected;
- content hash;
- related repository paths;
- source URLs;
- headings;
- search text;
- chunk identifiers for semantic ingestion.

Do not place secrets, tokens, personal data, or confidential case material in generated public indexes.

## Semantic-Ready Corpus

`indexes/semantic-documents.jsonl` is a preparation layer for future semantic search.

Each record should contain:

- stable chunk ID;
- source path;
- heading path;
- artifact type;
- domain;
- lifecycle status where available;
- text;
- content hash.

The corpus is not an embeddings database by itself.

## Semantic Search Boundary

Embeddings search is optional and requires an approved runtime and storage layer.

Before enabling embeddings:

1. choose the storage system;
2. define access boundaries;
3. exclude confidential data;
4. define refresh behavior;
5. define stale-index handling;
6. define retrieval limits;
7. validate that retrieved chunks improve context quality and cost.

## Graphify Boundary

Graphify remains an optional graph-memory layer under `docs/GRAPHIFY_STANDARD.md`.

Use it only for broad repositories or document corpora where cross-file navigation benefit justifies maintenance cost.

## Context Assembly Rule

Use generated indexes to locate the smallest sufficient context package.

Do not load the entire repository, the entire knowledge library, or the entire semantic corpus into routine work.

## Freshness Rule

Generated artifacts must record the repository commit they reflect when practical.

If an index is stale:

- report that limitation;
- verify important conclusions against canonical source files;
- refresh the index before relying on broad navigation.

## Final Rule

Index for navigation and selective loading. Never treat an index as a substitute for the underlying source of truth.