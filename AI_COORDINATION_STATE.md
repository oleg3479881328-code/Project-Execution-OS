# AI Coordination State

## Project
Project Execution OS / Mailbox Dispatcher

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Current Task
Complete the bounded Mailbox Dispatcher v6 correction described in Issue #52.

## Current Repository State
- Active outbound mailbox sequence: `9`
- Rejected v5 commit: `7f094010864d95fe0d4238b6d6a071548ab952da`
- Review request: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52#issuecomment-4694350514
- MarkItDown adapter PR #53 was accepted and merged.
- No AWS runtime is active.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #52 comments;
4. inspect any reported commit or PR;
5. continue from mailbox sequence `9`.

## Required Validation
- Verify executor ACK for sequence `9`.
- Verify same-sequence runner execution is allowed only from `ACK`.
- Verify structured adapter result semantics.
- Verify durable `Result-SHA`, `Status-Artifact-SHA`, and final `Comment-URL` fields.
- Verify post-run dirty-tree validation.
- Verify honest local blocker marker on push failure.
- Verify behavioral tests exercise the production paths.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #52 and repository evidence.
