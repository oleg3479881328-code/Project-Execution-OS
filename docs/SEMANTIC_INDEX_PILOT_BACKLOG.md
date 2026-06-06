# Semantic Index Pilot Backlog

Updated: 2026-06-06
Status: `candidate`

## Purpose

Define the bounded pilot required before semantic retrieval becomes an active Project Execution OS capability.

## Phase 1 — Corpus Validation

Validate:

- `indexes/semantic-documents.jsonl` generation;
- stable chunk identifiers;
- source-path preservation;
- status and domain metadata;
- duplicate handling;
- deleted-file cleanup;
- Markdown heading boundaries;
- exclusion of confidential material.

## Phase 2 — Runtime Selection

Compare only on a small corpus:

- PostgreSQL with pgvector;
- Qdrant;
- LanceDB.

Select one runtime only after measuring setup cost, filtering support, refresh behavior, and operational simplicity.

## Phase 3 — Embeddings Pilot

Index a limited set first:

- `docs/`;
- `blocks/`;
- `knowledge-library/`.

Do not index private case files, secrets, tokens, or production logs.

## Phase 4 — Retrieval Tests

Test queries where keyword search is insufficient, for example:

- phone verification inside Telegram;
- adaptive music for video scenes;
- marriage-based adjustment after a USCIS policy change;
- repository indexing and graph memory;
- prepare a Codex handoff from reusable knowledge.

Measure:

- relevant hits in top five results;
- false positives;
- stale hits;
- retrieval latency;
- context-token reduction;
- refresh reliability.

## Phase 5 — Activation Decision

Promote semantic retrieval only when:

- canonical-file verification remains mandatory;
- refresh discipline is proven;
- retrieval improves navigation quality;
- token cost drops materially;
- access boundaries remain clear;
- operational complexity is justified.

## Final Rule

Start with a bounded corpus and measurable questions. Do not deploy a vector database merely to make the system look sophisticated.