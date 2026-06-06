# Indexing Layer Status

Updated: 2026-06-06
Status: `candidate_operational`

## Purpose

Provide one compact navigation page for the committed indexing layer.

## Active Structural Layer

Use:

- `docs/INDEXING_STANDARD.md`
- `docs/SEMANTIC_INDEX_ARCHITECTURE.md`
- `docs/SEMANTIC_INDEX_PILOT_BACKLOG.md`
- `indexes/README.md`
- `indexes/system-index.json`
- `indexes/semantic-documents.jsonl`
- `indexes/BLOCK_CATALOG.generated.md`
- `indexes/KNOWLEDGE_CATALOG.generated.md`
- `scripts/build_system_index.py`
- `scripts/validate_system_index_v2.py`
- `scripts/query_system_index.py`
- `.github/workflows/system-index.yml`
- `SYSTEM_CONTEXT_MANIFEST.md`

## Current State

Implemented:

- curated block index refresh;
- curated knowledge-library index refresh plus temporary addendum for the indexing knowledge entry;
- router entry for indexing work;
- machine-readable JSON bootstrap index;
- semantic-ready JSONL bootstrap corpus;
- Python generator for repository Markdown indexing;
- Python validator for curated and generated index integrity;
- local lexical query command for the semantic-ready corpus;
- GitHub Actions workflow for automatic rebuild and commit of generated artifacts;
- stable context manifest update to `knowledge-aware-core-v7`.

Not active yet:

- confirmed first automatic GitHub Actions refresh;
- embeddings generation;
- vector database;
- semantic retrieval API;
- automatic Graphify refresh.

## Local Commands

Rebuild:

```bash
python scripts/build_system_index.py
```

Validate:

```bash
python scripts/validate_system_index_v2.py
```

Search the current corpus:

```bash
python scripts/query_system_index.py "telegram phone verification"
```

## Source Of Truth

Generated indexes assist navigation. Canonical repository files remain the source of truth.

## Next Validation

Confirm the first successful GitHub Actions refresh. After that, run the bounded semantic-search pilot only when a real retrieval problem justifies it.