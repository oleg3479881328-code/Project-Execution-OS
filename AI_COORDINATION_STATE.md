# AI Coordination State

## Project
Reels Factory MVP / AWS smoke test #2

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55

## Status
active / PREFLIGHT_READY / live AWS launch gated by owner approval

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Current Task
Wait for owner authorization, then execute the bounded second AWS Wan I2V smoke test for one 3-second 480p car-motion clip and custom AMI capture.

## Current Repository State
- Active outbound mailbox sequence: `15`
- Active issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
- Preflight report: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224
- Mailbox Dispatcher v11 is accepted and Issue #52 is closed.
- Read-only AWS preflight completed successfully.
- No Reels Factory GPU runtime is active.
- No persistent Reels Factory AMI exists yet.
- Reusable SSH-restricted security group and key pair are available.
- No blocker requiring owner action exists other than explicit launch authorization.

## Approval Gate
- Executor must not launch or modify billable AWS resources before explicit owner authorization in Issue #55.

## Next Step
Ask the owner whether to authorize the live AWS launch.

## Required Validation After Authorization
- Launch one fresh `g5.xlarge` with `100 GB gp3`.
- Complete setup and downloads.
- Run one `3-second`, `480p` low-quality car-motion generation.
- Download output and record runtime and cost.
- Stop instance, create AMI, wait for availability, record backing snapshots, terminate worker, and verify cleanup.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #55 and repository evidence.
