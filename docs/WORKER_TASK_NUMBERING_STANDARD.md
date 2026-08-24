# Worker Task Numbering Standard

## Status

Mandatory global Project Execution OS standard for every delegated worker task.

## Purpose

Prevent ambiguous worker packets such as `TASK — ...` without a unique task number, make every delegated job unambiguously identifiable in chat, durable state, QA, execution logs, and later references, and ensure worker chats themselves remain visually identifiable in the ChatGPT sidebar/history.

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

Each worker packet MUST contain at the very top, before background/context prose, a prominent identity block:

```text
TASK 21 — Matt & Morgan — First-Party Content & Evidence Map
TASK_NUMBER: 21
JOB_ID: TASK-21
TASK_NAME: Matt & Morgan — First-Party Content & Evidence Map
```

The FIRST VISIBLE LINE of the durable task packet MUST begin with `TASK <N> —`. Do not place generic text, execution-contract boilerplate, project name, date, or instructions above it. The owner must be able to open the task and immediately see the task number and name in the first line.

The Google Doc / Notion page / GitHub issue / other durable artifact title MUST also begin with `TASK <N> —`.

The visible link given to the owner MUST include the same task number and human-readable task name.

The number in all of these locations must match exactly:

- durable artifact title;
- first visible line of the task packet;
- task packet identity fields;
- Job ID or execution ID where applicable;
- controller's visible handoff link;
- requested worker chat title;
- worker completion summary;
- later QA/review references.

## Worker Chat Naming Rule

The worker chat itself SHOULD be named exactly the same as the canonical task title, excluding only an optional trailing date when UI title length makes the date undesirable.

Preferred chat title:

```text
TASK 21 — Matt & Morgan — First-Party Content & Evidence Map
```

The task packet MUST explicitly instruct the worker, at the top of the execution contract, to use/rename the current worker chat to this exact title if the ChatGPT surface available to that worker supports chat renaming.

Required instruction pattern:

```text
WORKER CHAT TITLE: TASK 21 — Matt & Morgan — First-Party Content & Evidence Map
If your current ChatGPT surface allows renaming the chat, rename this chat to exactly the WORKER CHAT TITLE above before substantive execution.
```

If the worker cannot programmatically or interactively rename the chat because the current surface does not expose that capability, it MUST NOT invent an alternative name. The first response/completion identity and all durable references must still use the exact canonical `TASK <N> — <name>` title.

The controller must not claim that the chat was renamed unless the worker/UI actually confirms it. This rule expresses the required canonical name and instructs the worker to apply it whenever supported.

## First-Line Visibility Rule

Visual scanability is mandatory. The task number is not allowed to be buried in metadata.

For every worker packet:

1. First visible line begins `TASK <N> — <task name>`.
2. `TASK_NUMBER`, `JOB_ID`, and `TASK_NAME` follow immediately.
3. `WORKER CHAT TITLE` follows in the same top identity block.
4. Only after this identity block may the one-link execution contract, goal, context, scope, sources, method, and output instructions appear.

This is specifically intended so the owner can see `TASK <N>` immediately when opening the task and can recognize worker chats quickly in history/sidebar views.

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
4. The first visible line begins with the same `TASK <N> — <name>` identity.
5. Job ID is present when the workflow uses Job IDs and references the same task number.
6. `WORKER CHAT TITLE` is present and matches the canonical task title.
7. The packet instructs the worker to rename the chat to that exact title when the surface supports it.
8. Visible handoff link text begins with or clearly includes the task number.
9. If multiple tasks are handed off together, their numbers are distinct and sequential unless there is a documented reason otherwise.

If any item fails, the task is NOT ready for handoff.

## Correction Rule

If an unnumbered or poorly identified worker task is accidentally created, the controller must correct it before dispatch whenever possible:

- determine the correct next free number;
- rename the durable artifact;
- make the first visible line the canonical `TASK <N> — <name>`;
- insert/correct `TASK_NUMBER`, `JOB_ID`, `TASK_NAME`, and `WORKER CHAT TITLE` inside the packet;
- insert the chat-renaming instruction;
- ensure the visible link uses the corrected numbered title;
- preserve the same artifact URL when possible rather than creating duplicates.

## Relationship to External AI Task + Result Standard

This standard is a mandatory extension of `docs/EXTERNAL_AI_NOTION_TASK_RESULT_STANDARD.md`.

Where that standard requires a Task Name and Task / Job ID, this document makes the numeric task identifier mandatory for worker tasks operating inside a numbered project workflow and adds first-line visibility plus canonical worker-chat naming.

The one-link handoff rule remains unchanged: once correctly numbered, the owner should still need to send only the task URL to the worker. The worker learns the required chat title from the packet itself; Oleg must not have to type the desired title separately.

## Final Rule

No numbered project workflow may hand off an anonymous worker artifact named only `TASK — ...`, a task packet whose number is buried below boilerplate, or a worker packet that leaves the canonical worker-chat name unspecified.

Use:

```text
find highest existing task number -> reserve next free number(s) -> create/rename task packet(s) -> put TASK identity on first visible line -> specify exact WORKER CHAT TITLE -> verify consistency -> hand off links
```

Task numbering and worker-chat naming are part of task identity, not cosmetic formatting.
