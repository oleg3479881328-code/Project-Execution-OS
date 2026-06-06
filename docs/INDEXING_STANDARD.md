# Indexing Standard

## Purpose

This standard defines the bounded indexing stack used by `Project Execution OS` for repository discovery.

The indexing layer exists to narrow file selection before broad scanning.

## Layers

The current bounded stack is:

```text
curated indexes
-> generated structural corpus
-> local semantic SQLite store
-> canonical-file verification
```

## Current Generated Artifacts

- `indexes/semantic-documents.jsonl` -> generated structural corpus for semantic build input
- `.local/semantic-index/semantic-index.sqlite3` -> local-only semantic store

## Build Commands

```text
python scripts/build_system_index.py
python scripts/validate_system_index_v3.py
python -m pip install -r semantic-requirements.txt
python scripts/build_semantic_store.py
```

## Query Commands

```text
python scripts/query_semantic_store.py "подтверждение телефона через Telegram" --limit 5
python scripts/query_semantic_store.py "адаптивная музыка для видео" --limit 5
python scripts/query_semantic_store.py "USCIS marriage interview memo" --domain us-law --limit 5
```

## Rules

- Inspect curated indexes first.
- Use generated indexes to narrow candidates before broad scanning.
- Use semantic retrieval when wording is uncertain or repository wording differs from the query.
- Open canonical files for selected hits before relying on them.
- Keep the SQLite store local-only and do not commit it.
- Do not add hosted vector services or cloud embedding APIs for this pilot.

## Related Nodes

- `docs/AGENT_INDEX_FIRST_ENTRY_STANDARD.md`
- `docs/SEMANTIC_INDEX_ARCHITECTURE.md`
- `docs/SEMANTIC_SEARCH_RUNTIME.md`
- `docs/INDEXING_LAYER_STATUS.md`
