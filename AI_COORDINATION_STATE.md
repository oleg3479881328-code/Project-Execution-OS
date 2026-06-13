# AI Coordination State

## Project
Reels Factory MVP / AWS staged execution

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55

## Status
active / PREFLIGHT_READY / Stage 1 preparation gated by owner approval

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Current Task
Wait for owner authorization for Stage 1 only: prepare ComfyUI, WanVideoWrapper, full Wan model and support files, validate the environment, create a reusable AMI, terminate the temporary worker, and stop.

## Current Repository State
- Active outbound mailbox sequence: `16`
- Active issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
- Preflight report: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224
- Two-stage plan amendment: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699380801
- Read-only AWS preflight completed successfully.
- No Reels Factory GPU runtime is active.
- No persistent Reels Factory AMI exists yet.
- Reusable SSH-restricted security group and key pair are available.

## Approval Gates
- Stage 1: owner must explicitly authorize environment preparation and AMI creation.
- Stage 2: owner must separately authorize generation and provide the start image after Stage 1 completes.

## Stage 1 Required Validation
- Launch one fresh `g5.xlarge` with `100 GB gp3`.
- Install or restore ComfyUI and WanVideoWrapper.
- Download full Wan model, T5 encoder, CLIP vision, and VAE.
- Validate GPU, workflow presence, file completeness, and localhost-only ComfyUI startup.
- Do not request an image and do not run video generation.
- Stop instance, create AMI, wait for availability, record snapshots and storage estimate, terminate worker, and verify cleanup.

## Stage 2 Later
- Launch from Stage 1 AMI after separate owner approval.
- Load owner-provided image.
- Run one `3-second`, `480p` low-quality I2V clip.
- Download output, record timing and cost, terminate worker, and verify cleanup.

## Next Step
Ask the owner whether to authorize Stage 1 preparation.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #55 and repository evidence.
