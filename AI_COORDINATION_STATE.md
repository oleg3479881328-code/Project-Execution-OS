# AI Coordination State

## Project
Reels Factory MVP / AWS staged execution

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55

## Status
active / Stage 1 preparation authorized / Stage 2 generation still gated

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Current Task
Execute Stage 1 only: launch one temporary `g5.xlarge`, prepare ComfyUI and WanVideoWrapper, download the full Wan model and support files, validate the environment, create a reusable AMI, terminate the temporary worker, verify cleanup, and stop.

## Current Repository State
- Active outbound mailbox sequence: `17`
- Active issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
- Preflight report: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224
- Two-stage plan amendment: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699380801
- Stage 1 owner authorization: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699393768
- Read-only AWS preflight completed successfully.
- No persistent Reels Factory AMI exists yet.
- Reusable SSH-restricted security group and key pair are available.

## Approval Gates
- Stage 1: authorized.
- Stage 2: not authorized. Do not request an image and do not run video generation.

## Stage 1 Required Validation
- Launch one fresh `g5.xlarge` with `100 GB gp3`.
- Install or restore ComfyUI and WanVideoWrapper.
- Download full Wan model, T5 encoder, CLIP vision, and VAE.
- Validate GPU, workflow presence, file completeness, and localhost-only ComfyUI startup.
- Do not request an image and do not run video generation.
- Stop instance, create AMI, wait for availability, record snapshots and storage estimate, terminate worker, and verify cleanup.
- Publish `STAGE_1_COMPLETE` or `BLOCKER`, then stop.

## Stage 2 Later
- Launch from Stage 1 AMI after separate owner approval.
- Load owner-provided image.
- Run one `3-second`, `480p` low-quality I2V clip.
- Download output, record timing and cost, terminate worker, and verify cleanup.

## Next Step
When `02` is received, read Issue #55 and inspect the Stage 1 execution status.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #55 and repository evidence.
