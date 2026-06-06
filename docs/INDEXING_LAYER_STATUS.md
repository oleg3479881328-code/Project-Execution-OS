# Indexing Layer Status

Updated: 2026-06-06
Status: `operational_structural`

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
- `scripts/validate_system_index_v3.py`
- `scripts/query_system_index.py`
- `.github/workflows/system-index.yml`
- `SYSTEM_CONTEXT_MANIFEST.md`

## Current State

Implemented and confirmed:

- curated block index refresh;
- curated knowledge-library index refresh plus temporary addendum for the indexing knowledge entry;
- router entry for indexing work;
- machine-readable JSON index;
- semantic-ready JSONL corpus;
- Python generator for repository Markdown indexing;
- non-blocking validator for generated index integrity and curated-index warnings;
- local lexical query command for the semantic-ready corpus;
- GitHub Actions workflow for automatic rebuild and commit of generated artifacts;
- first successful automatic GitHub Actions refresh;
- stable context manifest update to `knowledge-aware-core-v7`.

Confirmed automatic refresh result:

- generated commit: `1b73511882ed66237fe36e96bf88befa64468000`;
- indexed Markdown artifacts: `274`.

Not active yet:

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
python scripts/validate_system_index_v3.py
```

Search the current corpus:

```bash
python scripts/query_system_index.py "telegram phone verification"
```

## Source Of Truth

Generated indexes assist navigation. Canonical repository files remain the source of truth.

## Next Validation

Run a bounded semantic-search pilot only when a real retrieval problem justifies it.