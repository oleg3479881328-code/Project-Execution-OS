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
Existing Solution Search Required:
Implementation Instructions:
Acceptance Criteria:
Validation Commands / Checks:
Rollback Notes:
Execution Report Contract:
```

This is the default next artifact whenever the task is clearly Codex-bound and executor access is now the missing step.

For any API-based AI model integration, the handoff packet - пакет передачи задачи - must also include the complete block:

```text
API Model Runtime Check

Provider:
Model:
API-based AI model: Yes / No
Prompt caching supported: Yes / No / Unknown
Usage fields available:
Cache-hit fields available:
Cache-miss fields available:
Stable prefix ordering preserved: Yes / No / Not Applicable
Runtime logging implemented: Yes / No
If not implemented, blocker or reason:
```

For tasks not involving an API-based AI model integration, this line is allowed:

```text
API Model Runtime Check: Not Applicable
```

## Packet Lite

Use this when the task is narrow, low-risk, and bounded to a few files:

```text
CODEX PACKET LITE

Objective:
Files Allowed To Change:
Forbidden Changes:
Existing Solution Search Required:
Acceptance Criteria:
Validation:
Return:
```

For architecture, implementation, configuration, debugging, automation, and integration work, `Existing Solution Search Required` defaults to `Yes` unless there is a stated reason otherwise.

The same API Model Runtime Check requirement applies to `CODEX PACKET LITE` whenever the task includes an API-based AI model integration.

## Execution Report

Codex must return:

```text
EXECUTION REPORT

Status:
Files Changed:
Existing Solutions Checked:
Solution Reused Or Adapted:
Why Custom Implementation Was Necessary:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Ready For Review: Yes / No
```

For any API-based AI model integration, the execution report - отчёт исполнителя - must also answer the complete `API Model Runtime Check` block.

For tasks not involving an API-based AI model integration, this line is allowed:

```text
API Model Runtime Check: Not Applicable
```

## Evidence Rule

Do not claim `saved`, `committed`, `tested`, `executed`, `reviewed`, or `completed` without evidence.

A `commit SHA` proves a repository change exists.

It does not by itself prove full correctness.

Validation evidence and review are still required.
