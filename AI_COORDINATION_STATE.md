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
Publish the real mailbox dispatcher v3 implementation after the reported SHA failed GitHub resolution.

## Current Repository State
- Global mailbox standard: `docs/EXECUTOR_MAILBOX_STANDARD.md`
- Active outbound mailbox: `coordination/TO_EXECUTOR.md`
- Active inbound mailbox: `coordination/FROM_EXECUTOR.md`
- Latest correction mailbox sequence: `4`
- Publication blocker: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4686267612
- Reported missing SHA: `360cfa2119139b3f1264c609584582c6eeaf759b`
- GitHub fetch result for reported SHA: not found
- Current default branch still exposes the rejected v2 state machine
- Reels Factory persistence route accepted: Custom AMI primary, EBS snapshot fallback
- No AWS GPU runtime is active.

## Accepted Changes
- Issue #49 remains the only active durable reply surface for the dispatcher task.
- Root mailboxes remain the latest-message readback layer.
- GitHub issue comments remain the audit trail.

## Open Review Items
- Push the real v3 implementation to GitHub.
- Publish one exact fetchable 40-character SHA.
- Confirm runner executes the same sequence after notifier writes ACK and skips only terminal states.
- Confirm final pushed files include dispatcher, behavioral tests, README, inbound mailbox, and latest log.
- Publish exact test command and short output summary.
- Update `coordination/FROM_EXECUTOR.md` with the real published SHA.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #49 for supporting evidence;
4. fetch the newly reported full SHA;
5. inspect current dispatcher source and tests;
6. continue from mailbox sequence `4`.

## Required Validation
- Verify GitHub resolves the reported v3 SHA.
- Verify inbound mailbox sequence increments to `4` or later.
- Verify ACK-to-runner transition executes exactly once.
- Verify duplicate terminal sequence is a no-op.
- Verify dirty-tree blocker before side effects.
- Verify unreadable-issue blocker.
- Verify real committed SHA publication.
- Verify quoted argv behavior.
- Verify failed push handling.
- Verify behavioral tests actually call dispatcher paths.
- Verify no secrets are stored in repository.

## Update Rule
Update this snapshot only after meaningful state transitions.

## Reading Rule
Read the active route, then the inbound mailbox, then the active issue and repository evidence.
