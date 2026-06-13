# Latest Log — Reels Factory MVP

Date: 2026-06-13
Checkpoint: Stage 1 AWS preparation authorized

## Current Status

Reels Factory AWS execution is split into two separately authorized stages.

Active channel:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55

Stage 1 authorization:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699393768

Stage 1 is authorized now. Stage 2 generation is not authorized.

## Stage 1 — Authorized

Executor may:

1. launch one temporary `g5.xlarge` in `us-east-2`;
2. use `100 GB gp3` with `DeleteOnTermination=true`;
3. reuse the approved source-IP-only SSH security group and existing key pair;
4. install or restore ComfyUI and WanVideoWrapper;
5. download the full `Wan2.1-I2V-14B-480P` model;
6. download required T5 encoder, CLIP vision, and VAE support files;
7. validate GPU visibility, workflow presence, file completeness, and localhost-only ComfyUI startup through SSH tunneling;
8. stop the instance;
9. create a custom EBS-backed AMI;
10. wait until the AMI is available;
11. record AMI ID, backing snapshot IDs, setup time, download time, total runtime, cost estimate, and snapshot-storage estimate;
12. terminate the temporary GPU worker and verify cleanup;
13. publish `STAGE_1_COMPLETE` or `BLOCKER`, then stop.

## Stage 1 Boundaries

- Do not request a start image.
- Do not run video generation.
- Do not begin Stage 2.
- Do not leave the temporary GPU worker running after AMI availability is verified.

## Stage 2 — Later

After Stage 1 completes and the owner separately authorizes Stage 2:

1. launch temporary `g5.xlarge` from the saved AMI;
2. load the owner-provided start image;
3. run one `3-second`, `480p`, low-quality I2V clip;
4. download output and record timing, quality, retries, and cost;
5. terminate the temporary worker and verify cleanup.

## Preflight Evidence

Read-only preflight completed successfully:

- no active Reels Factory GPU runtime;
- no persistent Reels Factory AMI yet;
- reusable SSH-restricted security group and key pair available;
- GPU quota already approved;
- canonical route remains `g5.xlarge` + `Wan2.1-I2V-14B-480P` FP16 Diffusers.

Preflight report:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224

## Next Safe Action

Executor reads mailbox sequence `17`, executes Stage 1 only, publishes `STAGE_1_COMPLETE` or `BLOCKER`, and stops before Stage 2.
