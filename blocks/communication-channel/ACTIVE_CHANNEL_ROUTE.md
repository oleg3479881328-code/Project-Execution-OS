# Active Coordination Channel Route

## Purpose

This file is the smallest durable pointer for agent-to-agent communication.

Use it to answer:

1. Where should the next durable message be written?
2. Where should the next incoming message be read?
3. Which compact mailbox files carry the latest bidirectional state?

Do not store full messages, transcripts, reports, logs, or technical state here.

## Current Active Route

### Write Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51`

### Read Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51`

### Reviewer To Executor Mailbox

`coordination/TO_EXECUTOR.md`

### Executor To Reviewer Mailbox

`coordination/FROM_EXECUTOR.md`

### Transport Type

`GitHub issue comments + compact repository mailboxes`

### Scope

`Project Execution OS / MarkItDown local document intake adapter MVP`

### Last Confirmed At

`2026-06-11`

## Rule For Every Agent

Before sending a durable coordination message:

1. read this file;
2. write to `Write Here`;
3. update the sender-owned mailbox when one is listed;
4. report the exact destination used.

Before processing command `02` or checking for an incoming message:

1. read this file;
2. read the incoming mailbox listed above;
3. open `Read Here` for supporting evidence;
4. inspect the latest relevant commit or PR when reported;
5. respond from the reconciled current state.

Do not guess the active thread.

Do not claim that no reply exists merely because a long issue-thread read is truncated or stale. Use the compact mailbox as the primary latest-message signal.

Do not write to a different issue, pull request, Notion page, or chat trail unless this file is updated first.

## Channel Change Rule

When the active durable channel changes:

1. create the new bounded reply surface;
2. update this file;
3. post redirect notice in the previous channel;
4. post origin notice in the new channel;
5. update `AI_COORDINATION_STATE.md` when the active project uses it;
6. append channel transition event to `AI_COORDINATION_LOG.md` when present;
7. update both mailbox files with the new task and channel;
8. require executor acknowledgement in the new channel.

## Boundary

This file is only a routing pointer.

It does not replace:

- `AI_COORDINATION_STATE.md`;
- `AI_COORDINATION_LOG.md`;
- issue comments;
- pull request reviews;
- project state files;
- mailbox contents.
