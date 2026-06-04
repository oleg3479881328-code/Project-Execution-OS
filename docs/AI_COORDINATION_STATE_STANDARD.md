# AI Coordination State Standard

## Purpose

This standard defines the compact continuation artifact `AI_COORDINATION_STATE.md` for GitHub-backed projects that need lightweight durable coordination state between AI sessions.

Use it when the issue or pull request thread alone is not enough for efficient re-entry.

## Core Rule

`AI_COORDINATION_STATE.md` stores the current coordination state - текущее состояние координации - only.

It is a compact operational snapshot, not a running transcript.

Use it to record the currently active channel, reply surface, latest reviewed repository state, and one next expected move.

## When To Use

Use `AI_COORDINATION_STATE.md` when at least one condition is true:

- more than one AI session may continue the same repository-bound task;
- the active GitHub thread is long enough that re-entry would be slow without a compact state file;
- the project needs a durable pointer to the current reply surface, branch, PR, or blocker state;
- the owner explicitly wants transfer-ready coordination state.

Do not create it by ritual for tiny one-step work.

## Minimum Template

```text
# AI_COORDINATION_STATE

Project:
Active Channel:
Previous Channels:
Active Participants:
Reply Surface:
Current Task:
Current Status:
Latest Reviewed Repository State:
Accepted Changes:
Open Review Items:
Required Validation:
One Next Step:
Latest Commit SHA:
Last Updated:
Updated By:
```

## Update Rule

Update this file only when the current coordination state materially changes, for example:

- the active reply surface changes;
- the latest accepted handoff changes;
- Codex posts a new execution report that changes what happens next;
- ChatGPT or a reviewer requests revisions;
- the blocker state changes;
- the next expected action changes.

## Boundary

`AI_COORDINATION_STATE.md` is current state only.

It does not replace:

- the GitHub issue, PR, or review thread;
- `AI_COORDINATION_LOG.md`;
- repository memory artifacts;
- project planning or review documents.
