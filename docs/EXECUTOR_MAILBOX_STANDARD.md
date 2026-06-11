# Executor Mailbox Standard

Updated: 2026-06-11
Status: `active`

## Purpose

Provide a reliable bidirectional communication layer between a reasoning agent and an execution agent when issue comments alone are not sufficient for dependable readback.

This standard exists because long GitHub issue threads can be truncated, stale, or incomplete through connector read paths. The owner must not become the routine courier between agents.

## Core Model

Use three separate layers:

```text
GitHub issue / PR / review thread
-> durable discussion trail and evidence

projects/<project>/coordination/TO_EXECUTOR.md
-> latest reviewer-to-executor instruction envelope

projects/<project>/coordination/FROM_EXECUTOR.md
-> latest executor-to-reviewer status envelope
```

Optional project files remain separate:

```text
projects/<project>/PROJECT_STATE.md
-> durable project state after meaningful transitions

projects/<project>/logs/latest.md
-> human-readable current session summary
```

Do not rely on a long issue thread as the only readable current state.

## One Writer Per Mailbox

To avoid conflicts:

- the reasoning agent or reviewer writes only `TO_EXECUTOR.md`;
- the execution agent writes only `FROM_EXECUTOR.md`;
- both agents may write issue comments in the active reply surface;
- both agents update project-state files only when required by their task scope.

Do not let both sides overwrite the same mailbox file.

## Canonical Mailbox Paths

For a GitHub-backed project, use:

```text
projects/<project>/coordination/TO_EXECUTOR.md
projects/<project>/coordination/FROM_EXECUTOR.md
```

Create the `coordination/` directory when the project first needs multi-agent execution.

## Envelope Format

Each mailbox file is a compact overwrite-in-place status envelope.

Use this exact structure:

```text
# Executor Mailbox Envelope

Sequence: <integer>
Updated-At: <ISO-8601 timestamp>
Task-ID: <stable task identifier>
From: <sender role>
To: <recipient role>
Type: HANDOFF | CORRECTION | ACK | HEARTBEAT | BLOCKER | COMPLETE | STOP
Active-Channel: <URL>
Comment-URL: <URL or none>
Commit-SHA: <SHA or none>
Supersedes-Sequence: <integer or none>
Owner-Action-Required: none | <one exact action>
Next-Automatic-Action: <one exact action>

## Summary

<short factual message>

## Evidence

- <short evidence item or none>
```

Keep envelopes short. Store detailed reports in project artifacts and link them.

## Sequence Rule

Each writer maintains its own monotonically increasing sequence number.

- `TO_EXECUTOR.md` sequence increments whenever the reviewer sends a new instruction, correction, stop order, or approval.
- `FROM_EXECUTOR.md` sequence increments whenever the executor sends an acknowledgement, heartbeat, blocker, or completion report.

Do not reuse a prior sequence number for a materially new message.

## Write Rule

When the reviewer sends work to an executor:

```text
read ACTIVE_CHANNEL_ROUTE.md
-> post a signed comment in the active reply surface
-> update TO_EXECUTOR.md with the new sequence and comment URL
-> show the owner a linked receipt
```

When the executor reports status:

```text
read ACTIVE_CHANNEL_ROUTE.md
-> post a signed ACK / HEARTBEAT / BLOCKER / COMPLETE comment
-> update FROM_EXECUTOR.md with the new sequence and comment URL
-> update logs/latest.md
-> update PROJECT_STATE.md after meaningful transitions
-> continue automatically unless blocked
```

## Read Rule

For `02` or any status check, the reasoning agent must read in this order:

```text
ACTIVE_CHANNEL_ROUTE.md
-> FROM_EXECUTOR.md
-> logs/latest.md when present
-> PROJECT_STATE.md when needed
-> active issue / PR comments for evidence
-> reported commit / PR evidence
```

For an executor checking for new work:

```text
ACTIVE_CHANNEL_ROUTE.md
-> TO_EXECUTOR.md
-> active issue / PR comment for full instruction evidence
-> continue automatically if in scope
```

## Stale Or Truncated Connector Rule

If issue comments appear truncated, stale, or incomplete:

- do not conclude that no reply exists;
- trust the newest mailbox sequence as the current routing signal;
- use the active issue comment trail only as supporting evidence;
- inspect the reported commit SHA when present;
- ask the owner to relay a message only if both mailbox and active channel are unavailable.

## One Task, One Reply Surface

Use one dedicated issue, PR, or review thread for one bounded task or one tightly coupled review cycle.

Create a new continuation surface when:

- the bounded task changes;
- the execution phase changes materially;
- the thread becomes difficult to read;
- the thread exceeds approximately 12 substantive coordination comments;
- connector readback becomes unreliable;
- a completed task is followed by a new task.

Do not reuse a long issue indefinitely for unrelated phases.

## Channel Transition Rule

When moving to a new reply surface:

```text
create new issue / PR / thread
-> post origin notice in new surface
-> update ACTIVE_CHANNEL_ROUTE.md
-> update TO_EXECUTOR.md with new channel
-> post redirect notice in old surface
-> update AI_COORDINATION_STATE.md
-> append AI_COORDINATION_LOG.md transition event
-> require executor ACK in new surface
```

## Stop Order Rule

A stop order must use:

```text
Type: STOP
```

The executor must acknowledge it immediately, stop active work, perform required cleanup, update `FROM_EXECUTOR.md`, and report final cleanup evidence.

A later heartbeat from an older sequence must not override a newer stop order.

## Owner Visibility Rule

The owner is not the normal courier.

After durable writes, the sending agent shows the owner a short receipt with:

- what was sent;
- active channel;
- direct link;
- mailbox sequence;
- current state;
- next automatic action;
- whether owner action is required.

## Boundary

Mailboxes are control-plane state only.

Do not store:

- secrets;
- passwords;
- private keys;
- payment details;
- raw logs;
- large reports;
- copied issue histories.

## Final Rule

Use issue comments for audit trail.

Use `TO_EXECUTOR.md` and `FROM_EXECUTOR.md` for reliable latest-message readback.

Use one bounded task per reply surface.

Do not make the owner manually relay routine agent-to-agent communication.
