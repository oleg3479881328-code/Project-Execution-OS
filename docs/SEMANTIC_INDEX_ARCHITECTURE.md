# Semantic Index Architecture

## Purpose

This document records the bounded first semantic-retrieval architecture for `Project Execution OS`.

## Architecture

```text
repository text files
-> scripts/build_system_index.py
-> indexes/semantic-documents.jsonl
-> scripts/build_semantic_store.py
-> .local/semantic-index/semantic-index.sqlite3
-> scripts/query_semantic_store.py
-> canonical-file verification
```

## Design Choices

- Embeddings: local `sentence-transformers`
- Default model: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
- Storage: local SQLite file
- Similarity: cosine similarity over normalized embeddings
- Retrieval mode: local CLI, no separate server
- Safety boundary: SQLite store stays local and ignored by Git

## Stored Data

Each semantic chunk stores:

- chunk id
- canonical source path
- heading
- inferred domain
- inferred status
- content hash
- chunk text
- normalized embedding vector

The database metadata records:

- model name
- chunk count
- embedding dimension
- build timestamp
- source corpus path

## Retrieval Rules

- Retrieval output is advisory.
- The user or agent must open canonical files for any hit used in real work.
- Domain and status filters narrow the SQL candidate set before scoring.

## Boundary

This pilot is intentionally small.

It does not add:

- hosted vector databases;
- cloud embedding APIs;
- background services;
- repository-wide autonomous mutation.
