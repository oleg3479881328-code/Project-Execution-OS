# AI Coordination State Standard

## Purpose

This standard defines the compact operational state file used during multi-agent project work.

The file prevents long GitHub issues, pull-request threads, or chat trails from becoming the only readable coordination memory.

## Canonical Files

For an active GitHub-backed project, use two root-level files:

```text
AI_COORDINATION_STATE.md
AI_COORDINATION_LOG.md
```

Use these files when two or more participants coordinate technical work through GitHub or another durable project channel and the active thread may become too long, fragmented, or hard to resume reliably.

When the active project contains a fast project-scoped mirror, also use:

```text
projects/<project>/logs/latest.md
```

for the newest executor status snapshot.

## Core Split

```text
GitHub issue / PR / review thread
-> message transport and durable discussion trail

AI_COORDINATION_STATE.md
-> compact current operational snapshot
-> replace in place when the current state changes

AI_COORDINATION_LOG.md
-> append-only chronological event journal
-> append meaningful events at the bottom only

projects/<project>/logs/latest.md
-> fast project-scoped status mirror
-> newest ACK / HEARTBEAT / BLOCKER / COMPLETE state
```

Do not use `AI_COORDINATION_STATE.md` as a full transcript.

Do not use `AI_COORDINATION_LOG.md` as a copied chat trail.

Do not copy every comment into either file.

## Snapshot Contents

`AI_COORDINATION_STATE.md` should contain only the minimum durable current state:

```text
Project
Purpose
Active Channel
Previous Channels
Active Participants
Current Task
Current Repository State
Accepted Changes
Open Review Items
Next Step
Required Validation
Update Rule
Reading Rule
```

## Snapshot Update Triggers

Update `AI_COORDINATION_STATE.md` only after a meaningful state transition:

- communication-channel migration;
- meaningful implementation commit;
- accepted review;
- new blocker;
- scope change;
- completed task.

Do not update it for every short coordination message.

## Fast Status Mirror Rule

When `projects/<project>/logs/latest.md` exists, treat it as the first project-scoped readback surface for the newest executor status.

Update it after every executor:

```text
ACK
HEARTBEAT
BLOCKER
COMPLETE
```

The update should include:

- timestamp;
- active task;
- status marker;
- short factual state;
- active channel URL;
- direct comment URL when available;
- current commit SHA when available;
- next automatic action;
- owner action required or `none`.

The fast mirror does not replace the issue comment. It exists to survive connector truncation, stale comment reads, or long-thread omission.

## Append-Only Log Rule

`AI_COORDINATION_LOG.md` is governed by:

`docs/AI_COORDINATION_LOG_STANDARD.md`

Existing log entries must not be rewritten, reordered, deleted, compressed, or silently corrected.

New meaningful events are appended at the bottom only.

If an earlier entry contains an error, append a correction event at the bottom.

Do not rewrite history.

## Event And Snapshot Write Order

After a meaningful transition:

```text
append event to AI_COORDINATION_LOG.md
-> update AI_COORDINATION_STATE.md if the current operational state changed
-> update projects/<project>/logs/latest.md with newest status
-> keep the active Issue / PR / review thread as message transport
```

The log is chronological history.

The snapshot is current operational state.

The project mirror is the newest execution status.

The GitHub thread is the durable discussion trail.

Do not merge these roles.

## Reading Rule

Before resuming AI-to-AI coordination in an existing project, especially when processing shorthand command `02`, read in this order when the files exist:

```text
blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md
-> projects/<project>/logs/latest.md
-> AI_COORDINATION_STATE.md
-> Active Channel
-> latest relevant comments in the active channel
-> latest repository commit or PR state
-> AI_COORDINATION_LOG.md only when historical context is required
-> Next Step
```

Do not read the whole append-only log by default when the snapshot is sufficient.

Do not assume the newest issue or the longest thread is the active channel. Use the active route and snapshot.

If the connector response is truncated, stale, or missing the newest comment:

- do not claim that no reply exists;
- report that the connector read is inconclusive;
- use `logs/latest.md`, issue metadata, and latest commit evidence as fallback;
- ask for manual relay only as the last resort.

## Channel Migration Rule

When an issue, pull request, or review thread becomes too long or unreliable to read:

```text
create a new continuation channel
-> append a Channel Migration event to AI_COORDINATION_LOG.md
-> record the new channel in AI_COORDINATION_STATE.md
-> move old channel into Previous Channels
-> post a migration notice in the old channel
-> require executor acknowledgement in the new channel
```

Do not continue posting new execution reports into an archived channel.

## State Discipline

Keep generated state and executed state separate.

A snapshot update proves that the snapshot exists in repository history.

A log append proves that an event record exists in repository history.

A fast-mirror update proves that the newest status snapshot exists in repository history.

None of these alone proves that code changes, validations, or runtime behavior are correct.

Record commit SHAs and validation evidence separately.

## Model-Neutral Rule

The files must remain model-neutral and vendor-neutral.

The executor may be:

- Codex;
- DeepSeek;
- Claude;
- another connected AI agent;
- automation;
- a human developer.

The reviewer may also be any explicitly named review-capable participant.

## Scope Boundary

Use `AI_COORDINATION_STATE.md` only for current operational coordination state.

Use `AI_COORDINATION_LOG.md` only for meaningful chronological coordination events.

Use `projects/<project>/logs/latest.md` only for the newest project-scoped status mirror.

Do not store:

- secrets;
- raw logs;
- full conversation history;
- large patches;
- copied issue threads;
- unrelated project documentation.

Store large technical artifacts in the appropriate project files and send only short references through the active channel.

## Relationship To Other Standards

Use together with:

- `docs/AI_COORDINATION_LOG_STANDARD.md`;
- `blocks/communication-channel/BLOCK.md`;
- `docs/AI_COORDINATION_HUB_STANDARD.md`;
- `docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`;
- `docs/EXECUTOR_CHANNEL_ACK_AND_PUBLISH_STANDARD.md`;
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md` when durable handoff readiness matters.

## Final Rule

Use GitHub threads for transport.

Use `AI_COORDINATION_STATE.md` for compact current state.

Use `AI_COORDINATION_LOG.md` for append-only chronological history.

Use `projects/<project>/logs/latest.md` for newest executor status.

Do not allow a long message thread to become the only resumable project memory.
