# Codex Handoff Standard v1

## Purpose

This standard defines how reasoning-model work is handed to Codex for execution.

Use Codex only when executor access is actually needed for:
- repository edits;
- local commands;
- validation;
- environment inspection;
- other tool-only work.

If a task is small, safe, and can be completed directly through reasoning and drafting, do it without Codex.

## Core Model

```text
Reasoning model thinks.
Codex executes.
Reviewer verifies.
Repository memory persists.
```

## Transport Rule

The handoff packet is the payload.

GitHub issue, PR comment, or review thread is the transport when no direct runtime bridge exists.

Prefer an existing suitable project-bound GitHub channel before creating a new one.

## Full Packet

Use this for meaningful software execution work:

```text
IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Allowed Scope:
Out of Scope:
Repository Context:
Files Allowed To Change:
Forbidden Changes:
Implementation Instructions:
Acceptance Criteria:
Validation Commands / Checks:
Rollback Notes:
Execution Report Contract:
```

This is the default next artifact whenever the task is clearly Codex-bound and executor access is now the missing step.

## Packet Lite

Use this when the task is narrow, low-risk, and bounded to a few files:

```text
CODEX PACKET LITE

Objective:
Files Allowed To Change:
Forbidden Changes:
Acceptance Criteria:
Validation:
Return:
```

## Execution Report

Codex must return:

```text
EXECUTION REPORT

Status:
Files Changed:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Ready For Review: Yes / No
```

## Evidence Rule

Do not claim `saved`, `committed`, `tested`, `executed`, `reviewed`, or `completed` without evidence.

A `commit SHA` proves a repository change exists.

It does not by itself prove full correctness.

Validation evidence and review are still required.
