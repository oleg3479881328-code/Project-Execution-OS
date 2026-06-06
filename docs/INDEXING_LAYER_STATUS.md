# Indexing Layer Status

## Snapshot Date

`2026-06-06`

## Current State

- Structural corpus build: implemented locally through `scripts/build_system_index.py`
- Structural corpus validation: implemented locally through `scripts/validate_system_index_v3.py`
- Local semantic runtime: implemented locally through SQLite plus `sentence-transformers`
- Hosted retrieval API: inactive
- Graphify retrieval layer: inactive

## Validation Evidence

The intended local validation commands are:

```text
python scripts/build_system_index.py
python scripts/validate_system_index_v3.py
python -m pip install -r semantic-requirements.txt
python scripts/build_semantic_store.py
python scripts/query_semantic_store.py "подтверждение телефона через Telegram" --limit 5
python scripts/query_semantic_store.py "адаптивная музыка для видео" --limit 5
python scripts/query_semantic_store.py "USCIS marriage interview memo" --domain us-law --limit 5
```

Workflow validation for the semantic pilot is provided by:

`.github/workflows/semantic-index-pilot.yml`

## Operational Notes

- The SQLite store is local-only and ignored by Git.
- Retrieval quality is bounded by the generated corpus currently present in `indexes/semantic-documents.jsonl`.
- Agents must still open canonical files before relying on hits.
