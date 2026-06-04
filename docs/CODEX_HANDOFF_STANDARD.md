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

## Owner-Facing Handoff Rule

The owner should not receive large handoff packets in chat by default.

Default behavior:

1. prepare the full execution packet inside the selected GitHub transport;
2. keep detailed instructions, constraints, acceptance criteria, and reporting format inside that transport;
3. return to the owner only the shortest useful handoff, normally a single GitHub issue, PR, or review-thread link;
4. provide the full packet in chat only when the owner explicitly asks for copy-paste text.

The purpose is to reduce chat clutter while preserving complete execution context for the executor.

## Full Packet

Use this for meaningful software execution work:

```text
IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Allowed Scope:
Out Of Scope:
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

## Evidence Rule

Do not claim `saved`, `committed`, `tested`, `executed`, `reviewed`, or `completed` without evidence.

A `commit SHA` proves a repository change exists.

It does not by itself prove full correctness.

Validation evidence and review are still required.
