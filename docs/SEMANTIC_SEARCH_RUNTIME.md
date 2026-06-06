# Semantic Search Runtime

## Purpose

This document defines the local commands and operating behavior for the semantic-search pilot.

## Local Setup

Install the runtime:

```text
python -m pip install -r semantic-requirements.txt
```

Build the structural corpus:

```text
python scripts/build_system_index.py
python scripts/validate_system_index_v3.py
```

Build the local semantic store:

```text
python scripts/build_semantic_store.py
```

The default database path is:

`.local/semantic-index/semantic-index.sqlite3`

## Query

Run a semantic query:

```text
python scripts/query_semantic_store.py "подтверждение телефона через Telegram" --limit 5
```

Optional filters:

```text
python scripts/query_semantic_store.py "USCIS marriage interview memo" --domain us-law --status reference --limit 5
```

## Runtime Behavior

- The build script reads `indexes/semantic-documents.jsonl`.
- Missing embedding dependencies fail with a clear install instruction.
- Embeddings are normalized at build and query time.
- Query results are ranked by cosine similarity.
- Results print score, source path, heading, and a bounded excerpt.
- Output reminds the user that hits are navigation leads and canonical files must be opened before reliance.

## Rebuild Policy

Rebuild after meaningful repository-document changes that should affect retrieval quality.

Do not commit the SQLite store.

Do commit refreshed generated corpus files under `indexes/` when they are intentionally updated.
