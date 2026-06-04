# AI Coordination Log Standard

## Purpose

This standard defines the append-only artifact `AI_COORDINATION_LOG.md` for GitHub-backed projects that need a compact durable coordination history across AI sessions.

Use it when a short history of handoffs, reports, review requests, and channel changes will materially improve continuation.

## Core Rule

`AI_COORDINATION_LOG.md` is the coordination history - журнал координации - for meaningful durable messages and state changes.

It is not a replacement for full GitHub comments, pull request review history, or git history.

The log is append-only.

## When To Use

Use `AI_COORDINATION_LOG.md` when:

- the project has repeated AI-to-AI handoffs;
- the active GitHub thread is accumulating multiple execution cycles;
- a compact audit trail will help later review or re-entry;
- the owner wants durable continuation evidence inside the project repository.

Skip it for trivial one-message work.

## Minimum Entry Template

```text
# AI_COORDINATION_LOG

## YYYY-MM-DD HH:MM TZ

- From:
- To:
- Type:
- Channel:
- Reply Surface:
- Summary:
- State Impact:
- Next Step:
```

Append new entries.

Do not rewrite, reorder, delete, compress, or silently correct earlier log entries.

If an earlier entry is wrong, append a new correction entry at the bottom.

## Logging Rule

Record entries for durable coordination events such as:

- ChatGPT posts or updates an implementation handoff;
- Codex posts an execution report;
- a reviewer requests revisions or approves work;
- the active GitHub reply surface changes;
- the task enters or exits a blocker state.

## Boundary

`AI_COORDINATION_LOG.md` is a compact coordination history.

It does not authorize actions, replace issue comments, or substitute for validation evidence.
