# Worker Immediate Execution Standard

## Purpose

This is a hard launch standard for every delegated ChatGPT worker task in Project Execution OS.

It removes ambiguity between **reading a task** and **executing a task**.

## Core Rule

When Oleg sends a worker chat only a durable task URL, the URL itself is the complete execution command.

```text
TASK URL ONLY = OPEN -> READ FULLY -> EXECUTE IMMEDIATELY -> WRITE DURABLE RESULT -> REPORT COMPLETION
```

No second message is required.

## Mandatory Worker Behavior

On receiving a task URL as the only user message, the worker MUST:

1. open the linked task;
2. read the complete execution contract;
3. immediately begin substantive execution using the available tools;
4. continue until the requested deliverable is completed or a genuine execution blocker is reached;
5. write the result to the durable destination required by the task;
6. perform the required verification/readback;
7. only then return the prescribed concise completion message.

## Forbidden Non-Execution Behavior

The worker MUST NOT respond merely by:

- summarizing the task;
- explaining what the task asks for;
- listing the requested steps;
- reporting that the issue is open or has zero comments;
- saying it has opened/read the task;
- asking `Should I start?`;
- asking for confirmation when the execution contract already authorizes the work;
- waiting for `RUN`, `GO`, `start`, `continue`, or another trigger message;
- returning a task link back to Oleg instead of executing it.

Any such response before substantive execution is a **worker launch failure**.

## Mandatory Task-Packet Header

Every controller-created worker task MUST put the following contract at the top, immediately after the canonical task title:

```text
## IMMEDIATE EXECUTION CONTRACT — READ FIRST
If this task URL is the only content sent to you in a fresh ChatGPT worker chat, that URL is the complete launch command.

Immediately execute the task. Do not summarize or restate the task. Do not ask for confirmation. Do not wait for RUN, GO, or any additional message.

Your first substantive chat response should come only after you have actually begun/completed the requested work, or if you hit a genuine blocker that prevents execution. Opening the task and explaining what it says is NOT execution and is a task failure.
```

This header is mandatory, not optional wording guidance.

## Genuine Blocker Rule

A worker may stop before completion only when execution is genuinely impossible with current access or evidence.

Examples:

- required connector is unavailable;
- required source cannot be accessed;
- a write requires authorization that is not available;
- a required ambiguity cannot be resolved safely from the task or accessible sources.

A blocker report must state:

1. what was attempted;
2. the exact blocker;
3. what has already been completed;
4. the minimum specific action needed to unblock.

Lack of a separate `start` message is never a blocker.

## Controller Preflight Rule

Before giving Oleg a worker link, the controller MUST verify all of the following:

- canonical task title is `TASK <number> — <task name>`;
- task is self-contained;
- mandatory immediate-execution header is present at the top;
- sources and durable destinations are explicit;
- write/no-write boundaries are explicit;
- acceptance criteria are explicit;
- completion message contract is explicit;
- no additional user explanation or trigger is required.

If any item is missing, the task is not dispatch-ready.

## Worker Chat Naming

Worker naming follows `docs/WORKER_CHAT_NAMING_STANDARD.md`.

If the UI permits renaming, the chat should be renamed to the exact canonical task identity. Chat-title handling must never delay execution.

## Relationship to Existing Standards

This standard is a hard supplement to `docs/EXTERNAL_AI_NOTION_TASK_RESULT_STANDARD.md`.

Where wording is ambiguous, this standard controls **worker launch behavior**.

The intended model remains:

```text
one link in -> immediate execution -> durable write-back -> concise result link -> controller QA
```

## Final Rule

A worker task link is not a document-reading request.

It is an execution command.

**Open it and work immediately.**