# Indexing Layer Status

Updated: 2026-06-06
Status: `candidate_operational`

## Purpose

Provide one compact navigation page for the committed indexing layer.

## Active Structural Layer

Use:

- `docs/INDEXING_STANDARD.md`
- `docs/SEMANTIC_INDEX_ARCHITECTURE.md`
- `indexes/README.md`
- `indexes/system-index.json`
- `indexes/semantic-documents.jsonl`
- `indexes/BLOCK_CATALOG.generated.md`
- `indexes/KNOWLEDGE_CATALOG.generated.md`
- `scripts/build_system_index.py`
- `scripts/validate_system_index.py`
- `.github/workflows/system-index.yml`

## Current State

Implemented:

- curated block index refresh;
- curated knowledge-library index refresh;
- router entry for indexing work;
- machine-readable JSON bootstrap index;
- semantic-ready JSONL bootstrap corpus;
- Python generator for repository Markdown indexing;
- Python validator for curated and generated index integrity;
- GitHub Actions workflow for automatic rebuild and commit of generated artifacts.

Not active yet:

- embeddings generation;
- vector database;
- semantic retrieval API;
- automatic Graphify refresh.

## Source Of Truth

Generated indexes assist navigation. Canonical repository files remain the source of truth.

## Next Validation

Confirm the first successful GitHub Actions refresh. After that, run a bounded semantic-search pilot only when a real retrieval problem justifies it.
