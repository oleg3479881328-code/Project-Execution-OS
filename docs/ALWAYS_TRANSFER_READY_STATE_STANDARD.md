# Always Transfer-Ready State Standard

## Purpose

This standard defines the minimum continuity model that keeps an active project transferable at any moment without requiring Oleg to remember to request a handoff.

A project should be able to move from one executor to another — Codex, ChatGPT, DeepSeek, another AI agent, or a human — without hidden explanation in chat.

## Zero-State vs Active Execution

This standard starts after zero-state bootstrap.

Zero-state bootstrap is only:

```text
PROJECT.md
AGENTS.md    # optional for internal subprojects
```

After the first meaningful execution step, the project must become transfer-ready by adding:

```text
PROJECT_STATE.md
logs/latest.md
```

## Core Rule

Every meaningful project with an active execution layer must remain transfer-ready as a normal byproduct of work.

Transfer readiness is not a separate final handoff task.

After every meaningful work step, the executor must leave enough durable state for the next executor to continue without asking Oleg to reconstruct context from memory.

## Durable Interim Checkpoint Rule

Do not wait until the final report to preserve the current state.

During any long-running, multi-phase, benchmark-heavy, research-heavy, integration-heavy, or review-heavy task, the executor must save durable interim checkpoints whenever the thread of work would be costly to reconstruct.

Save an interim checkpoint at least when any of these occurs:

- a meaningful phase completes;
- a benchmark produces reusable partial results;
- a model comparison produces a provisional ranking;
- a blocker, fallback, or non-blocking failure changes the execution path;
- implementation is complete but validation is still running;
- validation is complete but publication or merge is still pending;
- the active branch, PR, issue, or reply surface changes;
- a reviewer posts an in-scope correction that future executors must see;
- execution remains active long enough that handoff risk becomes material.

The checkpoint must be durable and repository-visible or channel-visible. Do not leave important interim state only in chat memory, terminal scrollback, or an executor's local workspace.

Preferred preservation order:

```text
update PROJECT_STATE.md
-> update logs/latest.md
-> preserve reusable benchmark or research findings in a narrow durable file when needed
-> link the preserved state from the active issue or PR
```

If the project does not yet use `PROJECT_STATE.md` and `logs/latest.md`, use the narrowest existing durable state mechanism for that project, such as:

- `AI_COORDINATION_STATE.md`;
- `AI_COORDINATION_LOG.md`;
- a scoped durable report in `docs/`;
- the active GitHub issue or PR comment thread.

Do not create documentation ceremony for trivial work. Create a checkpoint only when it reduces real re-entry cost.

## Interim Checkpoint Minimum Content

A durable interim checkpoint should include only what a new executor needs to continue safely:

```text
Current Phase:
Completed:
In Progress:
Still Pending:
Measured Interim Results:
Known Failures Or Fallbacks:
Current Branch / PR / Issue:
Validated:
Not Yet Validated:
Next Safe Action:
Do-Not-Repeat Work:
```

Use a compact factual style. Avoid long narrative summaries unless they reduce real re-entry cost.

## Minimal Continuity Loop

```text
work step
-> update PROJECT_STATE.md
-> record logs/latest.md
-> save a durable interim checkpoint when reconstruction cost is material
-> update PROJECT.md only if the project front door changed
```

Do not create documentation ceremony for trivial work.

Do not leave important durable state only in chat.

## Active Minimum Set

For projects that already moved beyond zero-state bootstrap, the minimum transfer-ready set is:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

Optional artifacts may exist, but they must not replace this minimum set.

## Maintenance Rule

Update `PROJECT_STATE.md` and `logs/latest.md` after every meaningful step that changes one of these:

- current state;
- next action;
- implementation result;
- verification result;
- known blocker;
- active file set;
- constraint or do-not-break rule;
- measured interim result;
- active branch, PR, issue, or reply surface;
- do-not-repeat completed work.

Update `PROJECT.md` only when the project front door would otherwise mislead a new executor.

## Transfer Test

An active project passes the transfer test if a new executor can read:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`

and then identify the next safe action without asking Oleg for missing context.

If a significant active task is still in progress, the new executor must also be able to locate the latest durable interim checkpoint and identify:

- what has already been completed;
- what must not be repeated;
- what evidence has already been measured;
- what the next safe action is.

If that is not possible, the project is not transfer-ready.

## Anti-Bureaucracy Rule

The goal is continuity, not paperwork.

Do not require five documents when one current state file and one latest log are enough.

Do not write long narrative summaries unless they reduce real re-entry cost.

Do not create empty folders or placeholder files just to satisfy ceremony.

## Related Standards

- `docs/PROJECT_BOOTSTRAP_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`
