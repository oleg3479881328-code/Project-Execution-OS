# Backup Coordination Channel Route

## Purpose

This file is the smallest durable pointer for emergency recovery of agent-to-agent communication.

Use it only when the normal active route cannot be found, cannot be read reliably, or appears inconsistent between participants.

Do not store full messages, transcripts, reports, logs, or technical state here.

## Permanent Backup Route

### Write Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/54`

### Read Here

`https://github.com/oleg3479881328-code/Project-Execution-OS/issues/54`

### Transport Type

`GitHub issue comments`

### Command

`10`

### Scope

`Project Execution OS / emergency route recovery only`

### Last Confirmed At

`2026-06-12`

## Rule For Every Agent

When processing command `10`:

1. read this file;
2. open `Read Here`;
3. inspect the latest relevant recovery notes;
4. post a short signed recovery note to `Write Here` stating the participant's believed current active channel URL and the channel it can currently read and write;
5. reconcile the correct active route with the other participant;
6. if the active durable route must change, apply `docs/CHANNEL_TRANSITION_HANDSHAKE_STANDARD.md` before routine execution resumes;
7. return to normal `01` / `02` communication after recovery.

Use:

`docs/COMMAND_10_BACKUP_CHANNEL_RECOVERY_STANDARD.md`

for the complete recovery procedure.

## Boundary

This is a stable emergency route, not the routine execution channel.

Do not use it for normal task handoffs, implementation reports, review discussion, or project logs.

Do not replace `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md` with this file.

Keep the referenced issue open and stable.