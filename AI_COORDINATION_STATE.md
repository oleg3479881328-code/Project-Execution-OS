# AI Coordination State

## Project
Project Execution OS / Mailbox Dispatcher

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Current Task
Complete the minimal Mailbox Dispatcher v7 correction described in Issue #52.

## Current Repository State
- Active outbound mailbox sequence: `10`
- Rejected v6 implementation SHA: `f30672fcb4bd4ab92aa17c29bb64d40a5b7f773d`
- Rejected v6 status artifact SHA: `7c65b7187243e5ffbea641ab3da97323aed96f7b`
- Review request: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52#issuecomment-4695116184
- MarkItDown adapter PR #53 was accepted and merged.
- No AWS runtime is active.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #52 comments;
4. inspect any reported commit or PR;
5. continue from mailbox sequence `10`.

## Required Validation
- Verify executor ACK for sequence `10`.
- Verify timeout path publishes BLOCKER without `UnboundLocalError`.
- Verify immutable linkback artifact semantics without self-reference.
- Verify strict git-status failure handling.
- Verify adapter result SHA accepts only `none` or full 40-hex SHA.
- Verify behavioral tests exercise the production paths.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #52 and repository evidence.
