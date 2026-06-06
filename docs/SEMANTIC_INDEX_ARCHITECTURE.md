# Semantic Index Architecture

## Purpose

Define how `Project Execution OS` can add semantic search without turning generated embeddings into an uncontrolled source of truth.

## Status

`candidate`

## Problem

Keyword search and curated routes are efficient for known terms, but they may miss conceptually related material expressed with different wording.

Example:

```text
user asks: phone verification through Telegram
repository says: Gateway API verification codes
```

A semantic index can connect those meanings.

## Recommended Architecture

```text
canonical repository files
  -> structural index generator
  -> semantic-ready JSONL chunks
  -> embeddings job
  -> vector store
  -> filtered retrieval
  -> canonical-file verification
  -> minimum context assembly
```

## Candidate Runtime Options

Choose only after a real pilot:

- PostgreSQL with pgvector;
- Qdrant;
- LanceDB;
- Chroma for lightweight local experiments;
- OpenSearch or Elasticsearch when broader search infrastructure already exists.

## Initial Recommendation

For a first local or small hosted pilot, use one of:

- PostgreSQL with pgvector when the project already uses PostgreSQL;
- Qdrant when a dedicated vector service is acceptable;
- LanceDB for a lightweight embedded proof of concept.

Do not select a runtime merely because it is fashionable.

## Required Metadata Filters

Every embedded chunk should preserve:

- source path;
- source commit;
- artifact type;
- domain;
- lifecycle status;
- confidentiality class;
- heading path;
- content hash;
- updated date when available.

Retrieval should filter by relevance and allowed scope before returning text.

## Confidentiality Boundary

Do not embed:

- secrets;
- API tokens;
- personal immigration files;
- confidential legal case documents;
- private client data;
- credentials;
- production logs containing sensitive data.

Use separate stores and explicit access controls if private project material is ever indexed.

## Retrieval Rule

A semantic hit is a navigation lead, not authority.

After retrieval:

1. open the canonical source file;
2. confirm lifecycle status;
3. confirm freshness;
4. verify whether the source applies to the active task;
5. load only the minimum relevant excerpts.

## Refresh Rule

Re-embed only changed chunks when possible.

Use content hashes to detect changes and delete obsolete chunks when source files are removed or replaced.

## Pilot Acceptance Criteria

A pilot should measure:

- retrieval precision;
- false-positive rate;
- stale-hit rate;
- context-token reduction;
- latency;
- storage cost;
- refresh reliability;
- confidentiality boundary compliance.

## Activation Boundary

Do not call semantic indexing `active` until:

- one repository pilot succeeds;
- refresh behavior is tested;
- stale results are handled safely;
- retrieval demonstrably reduces repeated scanning;
- access boundaries are documented.

## Final Rule

Use semantic search to find likely context, then verify canonical files before relying on the result.