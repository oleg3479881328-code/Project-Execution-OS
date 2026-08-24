# Worker Task Numbering Standard

## Status

Mandatory global Project Execution OS standard for every delegated worker task.

## Purpose

Prevent ambiguous worker packets such as `TASK — ...` without a unique task number, and make every delegated job unambiguously identifiable in chat, durable state, QA, execution logs, and later references.

## Core Invariant

Every worker task MUST have a unique task number before its link is shown to the owner or dispatched to a worker.

Required title format:

```text
TASK <N> — <clear human-readable task name> — <date when useful>
```

Example:

```text
TASK 21 — Matt & Morgan — First-Party Content & Evidence Map — 2026-08-23
```

A title such as the following is invalid:

```text
TASK — Matt & Morgan — First-Party Content & Evidence Map
```

## Number Allocation Rule

Before creating one or more worker tasks, the controller MUST first inspect the project's current durable task state and determine the highest task number already in use for that project/task sequence.

Then allocate the next free number(s) sequentially.

Example:

```text
Highest existing task: TASK 20
New parallel tasks: TASK 21, TASK 22, TASK 23, TASK 24
```

Do not guess the next number from memory when durable state can be checked.

Do not reuse an existing task number for a new task.

Do not create several new worker packets first and number them afterward. Number allocation is a precondition to task creation/presentation.

## Task Packet Contract

Each worker packet MUST contain near the top:

```text
TASK_NUMBER: <N>
JOB_ID: TASK-<N>  # or a project-specific stable Job ID that includes the task number
TASK_NAME: <clear human-readable name>
```

The Google Doc / Notion page / GitHub issue / other durable artifact title MUST also begin with `TASK <N> —`.

The visible link given to the owner MUST include the same task number and human-readable task name.

The number in all of these locations must match exactly:

- durable artifact title;
- task packet body;
- Job ID or execution ID where applicable;
- controller's visible handoff link;
- worker completion summary;
- later QA/review references.

## Parallel Batch Rule

When several independent tasks are prepared together, reserve and assign the whole contiguous number range before presenting any links.

Example:

```text
TASK 21 — Content Evidence Map
TASK 22 — Gallery Visual Audit
TASK 23 — Technical BEFORE Baseline
TASK 24 — Competitor Research
```

This allows each worker to be referenced independently and prevents a group of anonymous `TASK — ...` documents from being confused with one another.

## Validation Before Handoff

Before sending worker links to the owner, the controller MUST verify all of the following:

1. Every task has a unique numeric `TASK <N>` identifier.
2. No allocated number collides with an existing task in the relevant project sequence.
3. Artifact title and internal task number match.
4. Job ID is present when the workflow uses Job IDs and references the same task number.
5. Visible handoff link text begins with or clearly includes the task number.
6. If multiple tasks are handed off together, their numbers are distinct and sequential unless there is a documented reason otherwise.

If any item fails, the task is NOT ready for handoff.

## Correction Rule

If an unnumbered worker task is accidentally created, the controller must correct it before dispatch whenever possible:

- determine the correct next free number;
- rename the durable artifact;
- insert/correct `TASK_NUMBER` and `JOB_ID` inside the packet;
- ensure the visible link uses the corrected numbered title;
- preserve the same artifact URL when possible rather than creating duplicates.

## Relationship to External AI Task + Result Standard

This standard is a mandatory extension of `docs/EXTERNAL_AI_NOTION_TASK_RESULT_STANDARD.md`.

Where that standard requires a Task Name and Task / Job ID, this document makes the numeric task identifier mandatory for worker tasks operating inside a numbered project workflow.

The one-link handoff rule remains unchanged: once correctly numbered, the owner should still need to send only the task URL to the worker.

## Final Rule

No numbered project workflow may hand off an anonymous worker artifact named only `TASK — ...`.

Use:

```text
find highest existing task number -> reserve next free number(s) -> create/rename task packet(s) -> verify number consistency -> hand off links
```

Task numbering is part of task identity, not cosmetic formatting.
