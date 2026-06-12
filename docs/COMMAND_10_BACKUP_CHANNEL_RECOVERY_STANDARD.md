# Command 10 Backup Channel Recovery Standard

## Purpose

This standard defines emergency recovery for connected-agent communication in `Project Execution OS`.

Use it when the normal active coordination route cannot be found, cannot be read reliably, or appears inconsistent between participants.

## Command

`10` = enter backup communication-channel recovery mode.

Do not reinterpret `10` as a numbered option or as approval for unrelated work.

## Permanent Backup Pointer

Open:

`blocks/communication-channel/BACKUP_CHANNEL_ROUTE.md`

Do not guess the backup issue URL from memory or chat history.

## Required Sequence

```text
read blocks/communication-channel/BACKUP_CHANNEL_ROUTE.md
-> open Read Here
-> inspect the latest relevant recovery notes
-> post a signed ROUTE RECOVERY note to Write Here
-> state the believed current active channel URL
-> state which channel can currently be read and written
-> reconcile the correct active route with the other participant
-> if the active route changes, complete docs/CHANNEL_TRANSITION_HANDSHAKE_STANDARD.md
-> return to normal 01 / 02 communication
```

## Required Recovery Note

Use the signed format from:

`docs/AI_COORDINATION_MESSAGE_STANDARD.md`

Recommended header:

```text
FROM: <sender name and role>
TO: <recipient name and role>
SUBJECT: ROUTE RECOVERY — command 10
TYPE: ROUTE RECOVERY
PROJECT: Project Execution OS
```

The note states the sender's believed active channel URL, whether it is readable and writable, any conflicting route evidence, and the next recovery action.

## Outcomes

If the existing active route is confirmed, post a short signed confirmation in the backup issue and return to routine `01` / `02` communication.

If the active route must change, apply:

`docs/CHANNEL_TRANSITION_HANDSHAKE_STANDARD.md`

before routine communication resumes.

If evidence remains inconclusive, continue short signed recovery notes in the backup issue. Ask Oleg for manual relay only as the last resort.

## Boundary

The backup issue is for route recovery only. It is not the routine execution channel, not a project log, and not a mailbox replacement.

`10` controls communication recovery only.

## Final Rule

When normal communication is lost or inconsistent, use `10` to meet in the permanent backup issue, reconcile the actual active route, complete a transition handshake when needed, and return to normal `01` / `02` communication.