# Latest Log — Reels Factory MVP

Date: 2026-06-11
Checkpoint: saved before separate Mailbox Dispatcher session

## Current Status

Persistence strategy selected. No AWS GPU runtime is active.

Primary route:

- create a custom EBS-backed AMI after the next successful setup and generation run;
- terminate temporary GPU workers between tests;
- retain only the AMI and its backing snapshots;
- expected storage estimate: about `$4/month` if stored snapshot blocks are about `80 GB`;
- measure actual snapshot size after AMI creation.

Fallback:

- EBS snapshot-only restore route.

## AWS Account

- Account ID: `102885960265`
- Region: `us-east-2` / Ohio
- Paid-plan upgrade completed.
- GPU quota: `4 vCPU` for `Running On-Demand G and VT instances`.
- Credits before first attempt: `$74.57`
- Approximate credits after first attempt: `$73.90`

## Canonical Route

- Instance: `g5.xlarge`
- GPU: NVIDIA A10G, 24 GB VRAM
- Model: `Wan2.1-I2V-14B-480P` FP16 Diffusers
- Workflow: `wanvideo_2_1_14B_I2V_example_03.json`
- Root volume: `100 GB gp3`
- Security: source-IP-only SSH; ComfyUI bound to `127.0.0.1`; use SSH tunnel for local access

## First AWS Attempt

Execution channel:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

Validated:

- `g5.xlarge` launched successfully;
- A10G detected;
- SSH worked;
- ComfyUI installed;
- WanVideoWrapper installed;
- Wan model download started.

Stopped by owner before generation:

- EC2 instance `i-090c7666371f00d68` terminated;
- EBS cleanup confirmed;
- no active smoke-test AWS resources remain;
- runtime approximately `40 minutes`;
- approximate cost `$0.67`.

## Persistence Report

Artifact:

- `projects/reels-factory-mvp/AWS_PERSISTENCE_STRATEGY.md`

Accepted report commit:

- `e04e88e105375b148731b3f1d2861d56c36b6b67`

State-sync commits:

- `a6dfdb4a61277404e708aed4610ca5f428d751ab`
- `df159f36b4db5dccddd69c01e2918fba38971102`

Persistence correction channel:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48

## Separate System Task

Mailbox Dispatcher implementation is a separate Project Execution OS task:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49

Do not confuse it with the next Reels Factory AWS run.

## Next Safe Reels Factory Action

Wait for explicit owner approval before launching a second AWS run.

On the approved run:

1. launch fresh `g5.xlarge`;
2. complete setup and downloads;
3. generate one `3-second`, `480p` clip;
4. stop the instance;
5. create the custom AMI;
6. wait until AMI state is available;
7. record AMI and snapshot IDs;
8. terminate the GPU worker;
9. verify cleanup and measure real monthly snapshot storage cost.

## Do-Not-Repeat Work

- Do not re-request GPU quota.
- Do not repeat Free Plan diagnosis.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`.
- Do not expose ComfyUI port `8188` publicly.
- Do not restart AWS runtime without owner approval.
