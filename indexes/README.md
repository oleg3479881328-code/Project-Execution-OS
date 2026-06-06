# Indexes

## Purpose

This directory stores generated discovery artifacts that help agents narrow file selection before broad scanning.

## Current Files

- `semantic-documents.jsonl` -> generated structural corpus used by the semantic-store builder

## Rules

- Treat generated indexes as discovery aids, not source of truth.
- Open canonical files for any selected hit before relying on it.
- Refresh generated indexes after meaningful structural or documentation changes that should affect retrieval.
- Do not store the local SQLite vector database here. It lives under `.local/semantic-index/` and is ignored by Git.
