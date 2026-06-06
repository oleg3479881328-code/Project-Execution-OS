# Indexing Layer Stack

Type: `architecture-decision`
Lifecycle status: `candidate`
Captured: 2026-06-06

## Reusable Lesson

Repository cognition should use layered indexing rather than repeated full-repository reading.

Use:

`stable door -> live router -> curated indexes -> generated machine index -> semantic-ready corpus -> optional embeddings runtime -> canonical-file verification`

## Current Implementation

- `docs/INDEXING_STANDARD.md`
- `docs/SEMANTIC_INDEX_ARCHITECTURE.md`
- `docs/INDEXING_LAYER_STATUS.md`
- `indexes/system-index.json`
- `indexes/semantic-documents.jsonl`
- `scripts/build_system_index.py`
- `scripts/validate_system_index.py`
- `scripts/query_system_index.py`
- `.github/workflows/system-index.yml`

## Boundary

Generated artifacts are navigation aids. Canonical repository files remain the source of truth.

Semantic retrieval is not active until an embeddings runtime and storage layer pass a bounded pilot.

## Final Rule

Use indexes to reduce scanning cost, then verify the canonical source before relying on the result.