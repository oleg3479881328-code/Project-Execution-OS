# Active Coordination Channel Route

## Purpose

This file is the smallest durable pointer for agent-to-agent communication.

Use it to answer two questions only:

1. Where should the next durable message be written?
2. Where should the next incoming message be read?

Do not store full messages, transcripts, reports, logs, or technical state here.

## Current Active Route

### Write Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/42`

### Read Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/42`

### Transport Type

`GitHub issue comments`

### Scope

`Project Execution OS server-rental / AWS head-node follow-up`

### Last Confirmed At

`2026-06-10`

## Rule For Every Agent

Before sending a durable coordination message:

1. read this file;
2. write to `Write Here`;
3. report the exact destination used.

Before processing command `02` or checking for an incoming message:

1. read this file;
2. open `Read Here`;
3. inspect the latest relevant incoming comment;
4. respond from the actual content.

Do not guess the active thread.

Do not write to a different issue, pull request, Notion page, or chat trail unless this file is updated first.

## Channel Change Rule

When the active durable channel changes:

1. update this file first;
2. post redirect notice in the previous channel;
3. post origin notice in the new channel;
4. update `AI_COORDINATION_STATE.md` when the active project uses it;
5. append channel transition event to `AI_COORDINATION_LOG.md` when present.

## Boundary

This file is only a routing pointer.

It does not replace:

- `AI_COORDINATION_STATE.md`;
- `AI_COORDINATION_LOG.md`;
- issue comments;
- pull request reviews;
- project state files.
