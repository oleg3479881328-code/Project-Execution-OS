# Semantic Search Runtime

Updated: 2026-06-06
Status: `candidate_operational`

## Purpose

Provide local semantic retrieval for Project Execution OS without requiring a separate database server.

## Default Stack

- multilingual Sentence Transformers embeddings;
- local SQLite vector store;
- cosine-similarity ranking;
- optional domain and status filters;
- canonical-file verification after retrieval.

Default model:

`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

## Why This Stack

Repository files are often in English while user queries may be in Russian. A multilingual embedding model is therefore the correct default.

SQLite is the first runtime because it is local, portable, and serverless.

## Storage Boundary

Default local database path:

`.local/semantic-index/semantic-index.sqlite3`

Do not commit the database file.

## Scale Boundary

Move to pgvector or Qdrant only when measured corpus size, concurrency, or latency justifies a dedicated service.

## Retrieval Rule

A semantic hit is a navigation lead, not authority. Open the canonical file, confirm status and freshness, then load only the minimum relevant excerpt.

## Final Rule

Use semantic retrieval before broad scanning when the correct file is not obvious.