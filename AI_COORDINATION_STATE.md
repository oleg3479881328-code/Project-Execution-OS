# AI Coordination State

## Project
Project Execution OS

## Purpose
Implement and validate an automatic mailbox dispatcher so routine executor coordination no longer depends on manual owner relay.

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Previous Channels
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48 — Reels Factory persistence-strategy correction completed
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47 — Reels Factory AWS smoke-test execution and first persistence draft
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/46 — execution-kit preparation and review iterations

## Active Participants
- Oleg Povalyukhin — Project Owner
- ChatGPT — Reviewer
- Executor Agent — Infrastructure Executor

## Current Task
Correct the mailbox dispatcher state machine after review rejection of dispatcher v2.

## Current Repository State
- Global mailbox standard: `docs/EXECUTOR_MAILBOX_STANDARD.md`
- Active outbound mailbox: `coordination/TO_EXECUTOR.md`
- Active inbound mailbox: `coordination/FROM_EXECUTOR.md`
- Latest correction mailbox sequence: `3`
- Review request: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4686210580
- Rejected v2 final-status commit: `08970acf3b70ec351fd544012dae9d347205d033`
- Implementation commit under review: `46532f9d835a6a0c66e0c0294b264ca8128602e6`
- Reels Factory persistence route accepted: Custom AMI primary, EBS snapshot fallback
- No AWS GPU runtime is active.

## Accepted Changes
- Issue #49 remains the only active durable reply surface for the dispatcher task.
- Root mailboxes remain the latest-message readback layer.
- GitHub issue comments remain the audit trail.

## Open Review Items
- Critical: notifier writes ACK using sequence N, then runner incorrectly skips the same sequence as already processed.
- Post-commit SHA publication order remains incorrect.
- Dirty-tree validation runs after side effects instead of before them.
- Route-mismatch and dirty-tree blockers are not durably mirrored consistently.
- Runner must block when the active issue cannot be read.
- Quoted runner arguments require structured parsing.
- Current tests are mostly tautological and do not exercise the state machine.
- README claims must match implemented recovery behavior.
- Allowed-directory staging must include new test files.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #49 for supporting evidence;
4. inspect any reported commit or PR;
5. continue from mailbox sequence `3`.

## Required Validation
- Verify executor ACK for sequence `3` in Issue #49.
- Verify inbound mailbox sequence increment.
- Verify ACK-to-runner transition executes exactly once.
- Verify duplicate terminal sequence is a no-op.
- Verify dirty-tree blocker before side effects.
- Verify active-route mismatch blocker.
- Verify unreadable-issue blocker.
- Verify comments and mailboxes reference the real committed result SHA.
- Verify quoted argv behavior.
- Verify failed push handling.
- Verify no secrets are stored in repository.

## Update Rule
Update this snapshot only after meaningful state transitions.

## Reading Rule
Read the active route, then the inbound mailbox, then the active issue and repository evidence.
