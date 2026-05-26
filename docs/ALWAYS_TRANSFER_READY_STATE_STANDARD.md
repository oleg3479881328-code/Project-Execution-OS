# Always Transfer-Ready State Standard

## Purpose

This standard defines the minimum continuity model that keeps a project transferable at any moment without requiring Oleg to remember to request a handoff.

A project should be able to move from one executor to another — Codex, ChatGPT, DeepSeek, another AI agent or a human — without hidden explanation in chat.

## Core Rule

Every meaningful project with an active execution layer must remain transfer-ready as a normal byproduct of work.

Transfer readiness is not a separate final handoff task.

After every meaningful work step, the executor must leave enough durable state for the next executor to continue without asking Oleg to reconstruct context from memory.

## Minimal Continuity Loop

Use the smallest reliable loop:

```text
work step
-> update current state
-> record latest recoverable log
-> update entrypoint only if the project front door changed
```

Do not create documentation ceremony for trivial work.

Do not leave important durable state only in chat.

## Required Artifacts For File-Based Execution

For projects that use a local folder, GitHub repository, versioned files, Codex Desktop or any file-based execution workspace, the minimum transfer-ready set is:

```text
PROJECT_ENTRYPOINT.md
PROJECT_STATE.md
logs/latest.md
```

Optional artifacts may exist, but they must not replace this minimum set.

## PROJECT_ENTRYPOINT.md

The entrypoint is the stable front door.

Update it only when one of these changes:

- project purpose;
- active storage or execution layers;
- source-of-truth boundaries;
- current focus;
- next practical step;
- a major constraint that a new executor must know before working.

It must not become a transcript, raw log or full history.

## PROJECT_STATE.md

`PROJECT_STATE.md` is the live transfer switch.

It should stay short and current.

Recommended fields:

```yaml
---
status: in-progress
last_updated: YYYY-MM-DD
current_goal: ""
current_status: ""
last_completed_step: ""
next_action: ""
blocked_by: ""
active_files: []
do_not_break: []
last_verified_result: ""
---
```

The file should answer:

1. What are we trying to achieve now?
2. What is the current state?
3. What was just completed?
4. What should happen next?
5. What must not be broken?
6. What has been verified?

## logs/latest.md

`logs/latest.md` records the latest recoverable execution event.

It should be short.

Recommended structure:

```markdown
# Latest Log

## Date
YYYY-MM-DD

## Executor
Codex / ChatGPT / DeepSeek / human / other

## Action
What was attempted.

## Result
What changed or what was learned.

## Verification
What was checked.

## Issues
Errors, blockers or risks.

## Next Action
The next concrete step.
```

If long-term history is needed, copy or move older logs into `logs/history/`.

## When To Update

Update `PROJECT_STATE.md` and `logs/latest.md` after every meaningful step that changes one of these:

- current state;
- next action;
- implementation result;
- verification result;
- known blocker;
- active file set;
- constraint or do-not-break rule.

Update `PROJECT_ENTRYPOINT.md` only when the project front door would otherwise mislead a new executor.

## Executor Responsibility

Any executor working inside the project must treat state maintenance as part of the work, not as an optional report.

A task is not complete if the project cannot be resumed from the durable state files.

## Anti-Bureaucracy Rule

The goal is continuity, not paperwork.

Do not require five documents when one current state file and one latest log are enough.

Do not write long narrative summaries unless they reduce real re-entry cost.

Do not create empty folders or placeholder files just to satisfy ceremony.

## Transfer Test

A project passes the transfer test if a new executor can read:

1. `PROJECT_ENTRYPOINT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`

and then identify the next safe action without asking Oleg for missing context.

If that is not possible, the project is not transfer-ready.

## Relationship To Handoff Files

Explicit handoff snapshots are optional.

They may be generated when useful, but they must be derived from the current durable state.

The system must not depend on Oleg remembering to request a handoff.

## Related Standards

- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
