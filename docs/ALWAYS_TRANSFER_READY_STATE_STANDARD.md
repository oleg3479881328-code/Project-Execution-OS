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

## Minimal Continuity Loop

```text
work step
-> update PROJECT_STATE.md
-> record logs/latest.md
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
- constraint or do-not-break rule.

Update `PROJECT.md` only when the project front door would otherwise mislead a new executor.

## Transfer Test

An active project passes the transfer test if a new executor can read:

1. `PROJECT.md`
2. `PROJECT_STATE.md`
3. `logs/latest.md`

and then identify the next safe action without asking Oleg for missing context.

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
