# Always Transfer-Ready State Standard

## Purpose

This standard defines the minimum continuity model that keeps an active project transferable at any moment without requiring Oleg to remember to request a handoff.

A project should be able to move from one executor to another — Codex, ChatGPT, DeepSeek, another AI agent, or a human — without hidden explanation in chat.

This standard follows `docs/CANONICAL_LIVE_STATE_CHECKPOINT_STANDARD.md`: one live current state is primary; checkpoints are rare frozen recovery/audit artifacts; a chat boundary alone never creates a migration.

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

The primary mechanism is continuous maintenance of the single canonical live current state plus the current work log — not repeated migration snapshots.

## Durable Interim Preservation Rule

Do not wait until the final report to preserve important current state.

During any long-running, multi-phase, benchmark-heavy, research-heavy, integration-heavy, or review-heavy task, preserve durable interim facts whenever the thread of work would be costly to reconstruct.

Normally this means updating the existing live state and work log when any of these occurs:

- a meaningful phase completes;
- a benchmark produces reusable partial results;
- a model comparison produces a provisional ranking;
- a blocker, fallback, or non-blocking failure changes the execution path;
- implementation is complete but validation is still running;
- validation is complete but publication or merge is still pending;
- the active branch, PR, issue, or reply surface changes;
- a reviewer posts an in-scope correction that future executors must see;
- execution remains active long enough that re-entry risk becomes material.

Do not create a new frozen checkpoint for each such event. Create a checkpoint only when preserving an exact transition state has real rollback, audit, or handoff value under `docs/CANONICAL_LIVE_STATE_CHECKPOINT_STANDARD.md`.

The preserved state must be durable and repository-visible or channel-visible. Do not leave important interim state only in chat memory, terminal scrollback, or an executor's local workspace.

Preferred preservation order:

```text
update PROJECT_STATE.md
-> update logs/latest.md
-> preserve reusable benchmark or research findings in a narrow durable file when needed
-> create a frozen checkpoint only when the checkpoint trigger is real
-> link preserved state from the active issue or PR when useful
```

If the project does not yet use `PROJECT_STATE.md` and `logs/latest.md`, use the narrowest existing durable state mechanism for that project, such as:

- a Notion `Current State` page/block and current Work Log;
- `AI_COORDINATION_STATE.md`;
- `AI_COORDINATION_LOG.md`;
- a scoped durable report in `docs/`;
- the active GitHub issue or PR comment thread.

Do not create documentation ceremony for trivial work.

## Live State Minimum Content

The canonical live current state should include only what a new executor needs to continue safely:

```text
Current Objective / Phase:
Verified Current State:
Completed:
In Progress:
Still Pending:
Known Failures / Blockers / Risks:
Current Branch / PR / Issue / Deployment:
Validated:
Not Yet Validated:
Superseded / Obsolete:
Next Safe Action:
Do-Not-Repeat Work:
Last Verified:
```

Use a compact factual style. Avoid long narrative summaries unless they reduce real re-entry cost.

## Minimal Continuity Loop

```text
work step
-> update PROJECT_STATE.md when current state or next action changed
-> record logs/latest.md when meaningful work or validation occurred
-> create a checkpoint only for a real recovery/audit boundary
-> update PROJECT.md only if the project front door changed
```

Do not create documentation ceremony for trivial work.

Do not leave important durable state only in chat.

Do not create a migration merely because a chat ended or a new chat started.

## Active Minimum Set

For projects that already moved beyond zero-state bootstrap, the minimum transfer-ready set is:

```text
PROJECT.md
PROJECT_STATE.md
logs/latest.md
```

For Notion-first projects, use the equivalent:

```text
START HERE / Project Entrypoint
Current State
Current Work Log
```

Optional artifacts may exist, but they must not replace the single live state.

## Maintenance Rule

Update the live current state and current work log after every meaningful step that changes one of these:

- current state;
- next action;
- implementation result;
- verification result;
- known blocker or risk;
- active file set;
- constraint or do-not-break rule;
- measured interim result;
- active branch, PR, issue, deployment, or reply surface;
- do-not-repeat completed work;
- an obsolete route or decision that could mislead a future executor.

Update the project entrypoint only when the project front door would otherwise mislead a new executor.

## Transfer Test

An active repository-first project passes the transfer test if a new executor can read:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`

and then identify the next safe action without asking Oleg for missing context.

A Notion-first project passes when the executor can read:

1. `START HERE` / Project Entrypoint
2. canonical live `Current State`
3. current Work Log or latest relevant checkpoint

and continue safely.

Historical migrations are not default reading. They are consulted only when the live state points to one for recovery, audit, or transition evidence.

## Anti-Bureaucracy Rule

The goal is continuity, not paperwork.

Do not require five documents when one current state file and one latest log are enough.

Do not write long narrative summaries unless they reduce real re-entry cost.

Do not create empty folders or placeholder files just to satisfy ceremony.

Do not create chat-by-chat migration pages.

## Related Standards

- `docs/CANONICAL_LIVE_STATE_CHECKPOINT_STANDARD.md`
- `docs/PROJECT_MEMORY_STANDARD.md`
- `docs/PROJECT_BOOTSTRAP_STANDARD.md`
- `docs/PROJECT_LIFECYCLE_MODEL.md`
- `docs/PROJECT_ENTRYPOINT_STANDARD.md`
- `docs/PROJECT_STRUCTURE_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`
