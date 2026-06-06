# Indexes

## Purpose

This folder stores generated navigation artifacts for `Project Execution OS`.

## Generated Files

- `system-index.json` — machine-readable repository catalog;
- `semantic-documents.jsonl` — semantic-ready text chunks for future embeddings ingestion;
- `BLOCK_CATALOG.generated.md` — generated block artifact catalog;
- `KNOWLEDGE_CATALOG.generated.md` — generated knowledge-library artifact catalog.

## Source Of Truth

Generated indexes are navigation aids. Canonical repository files remain the source of truth.

## Refresh

Run:

```bash
python scripts/build_system_index.py
```

## Validate

Run:

```bash
python scripts/validate_system_index_v2.py
```

## Search Current Corpus

Run:

```bash
python scripts/query_system_index.py "telegram phone verification"
```

The query tool performs lightweight lexical ranking over the prepared corpus. It is useful before an embeddings runtime is activated.

## Automation

The GitHub Actions workflow refreshes generated artifacts after relevant structural changes:

`.github/workflows/system-index.yml`

## Semantic Search Boundary

`semantic-documents.jsonl` is not an embeddings database. It is the prepared corpus for a later approved embeddings runtime.
