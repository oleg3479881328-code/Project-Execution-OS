# PROJECT — Reels Factory MVP

## 1. Project

- Project name: `Reels Factory MVP`
- Project type: `video-production / server-rental / AI media MVP`
- Purpose: validate a repeatable low-cost pipeline for creating one original short animated reel using temporary rented GPU compute only.

## 2. Current Status

- Status: `active / paused safely`
- Current phase: prepare the second AWS smoke-test attempt
- AWS GPU runtime: `stopped`
- Persistent AMI: `not created yet`
- Owner approval required before any new AWS GPU launch

## 3. Current MVP Target

Validate the narrowest possible pipeline:

`generated start image -> Wan Image-to-Video -> 3-second 480p low-quality clip -> download result -> record runtime and cost -> preserve reusable AMI -> terminate GPU runtime`

First test concept:

- simple car-motion scene;
- verify that the vehicle visibly moves;
- verify that a video file is produced;
- measure setup time, generation time, total runtime, cost, and output quality.

## 4. Confirmed Technical Route

AWS region:

- `us-east-2` / Ohio

Canonical GPU worker:

- `g5.xlarge`
- NVIDIA A10G, 24 GB VRAM

Canonical model route:

- `Wan2.1-I2V-14B-480P` FP16 Diffusers
- workflow: `wanvideo_2_1_14B_I2V_example_03.json`

Security:

- source-IP-only SSH;
- ComfyUI bound to `127.0.0.1`;
- use SSH tunneling;
- do not expose port `8188` publicly.

## 5. Persistence Decision

Primary route:

- create a custom EBS-backed AMI after the next successful setup and generation run;
- terminate temporary GPU workers between tests;
- retain only the AMI and its backing snapshots;
- expected storage estimate: about `$4/month` if stored snapshot blocks are about `80 GB`;
- measure actual billed snapshot size after AMI creation.

Fallback:

- EBS snapshot-only restore route.

Temporary convenience route:

- keep a stopped instance only when the next test is expected within days and the owner explicitly accepts the higher ongoing EBS cost.

## 6. Completed Evidence

First AWS smoke-test attempt validated:

- paid-plan upgrade removed the Free Plan GPU blocker;
- GPU quota increase to `4 vCPU` was approved;
- `g5.xlarge` launched successfully;
- NVIDIA A10G was detected;
- SSH worked;
- ComfyUI installed successfully;
- WanVideoWrapper installed successfully;
- Wan model download started successfully;
- controlled termination and EBS cleanup worked.

The first attempt was stopped by owner command before generation.

Measured interim result:

- runtime: approximately `40 minutes`;
- approximate cost: `$0.67`;
- no active AWS smoke-test resources remain.

## 7. Still Pending

1. owner approval for the second AWS run;
2. launch fresh `g5.xlarge`;
3. complete model and support-file downloads;
4. generate one start image in ChatGPT;
5. run one `3-second`, `480p` I2V clip;
6. record runtime, cost, quality, retries, and failures;
7. stop instance;
8. create custom AMI;
9. wait until AMI is available;
10. record AMI ID, backing snapshots, actual stored size, and monthly cost;
11. terminate GPU worker;
12. verify cleanup.

## 8. Separate System Task

Mailbox Dispatcher implementation is a separate Project Execution OS task:

- active system issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49

Do not confuse the dispatcher task with the next Reels Factory AWS execution step.

## 9. Durable Source Of Truth

Read in this order:

1. `projects/reels-factory-mvp/PROJECT.md`
2. `projects/reels-factory-mvp/PROJECT_STATE.md`
3. `projects/reels-factory-mvp/logs/latest.md`
4. `projects/reels-factory-mvp/AWS_PERSISTENCE_STRATEGY.md`
5. `projects/reels-factory-mvp/AWS_WAN_SMOKE_TEST_RUNBOOK.md`

## 10. Do-Not-Repeat Work

- Do not re-request AWS GPU quota.
- Do not repeat Free Plan diagnosis; paid-plan upgrade is complete.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`; it was an incorrect earlier assumption.
- Do not expose ComfyUI port `8188` publicly.
- Do not launch AWS runtime without explicit owner approval.
- Do not leave temporary GPU resources active after tests.

## 11. Direct Links

- Persistence correction issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48
- Previous AWS execution issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47
- Separate dispatcher task: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49
- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
