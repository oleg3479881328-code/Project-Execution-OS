# Latest Log — Reels Factory MVP

Date: 2026-06-11

## Session Summary

The first AWS infrastructure smoke-test attempt was executed and then intentionally stopped by owner command before video generation.

## RunPod

- RunPod onboarding was checked earlier.
- Minimum custom funding amount confirmed: `$10`.
- No RunPod payment was made.
- RunPod remains fallback only.

## AWS Account

- Account ID: `102885960265`
- Region: `United States (Ohio)` / `us-east-2`
- GPU quota: `Running On-Demand G and VT instances` increased from `0` to `4` vCPU.
- AWS Support case: `178112387200526`
- Owner upgraded account from AWS Free Plan to paid plan.
- Credits reported before attempt: `$74.57`
- Approximate credits after stop: `$73.90`

## Canonical Execution Kit

Final reviewed kit commit:

`3f7a245605a3afed5f7cd0c6c3758e68d3a8f282`

Canonical route:

- Instance: `g5.xlarge`
- GPU: NVIDIA A10G, 24 GB VRAM
- Model: `Wan2.1-I2V-14B-480P` FP16 Diffusers
- Workflow: `wanvideo_2_1_14B_I2V_example_03.json`
- Root volume: `100 GB gp3`
- Security: source-IP only; SSH tunneling preferred

Artifacts:

1. `AWS_INSTANCE_SELECTION.md`
2. `AWS_WAN_SMOKE_TEST_RUNBOOK.md`
3. `COST_TRACKING_TEMPLATE.md`

## First AWS Smoke-Test Attempt

Execution channel:

https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

Resources:

- EC2 instance: `i-090c7666371f00d68`
- Instance type: `g5.xlarge`
- Public IP during runtime: `3.144.84.183`
- Root volume: `100 GB gp3`

Validated:

- Paid-plan upgrade removed GPU launch blocker.
- `g5.xlarge` launched successfully.
- NVIDIA A10G detected.
- SSH worked.
- ComfyUI installed.
- WanVideoWrapper installed.
- Wan model download started.

Owner stop command:

- Owner ordered all active processes stopped before generation.
- Model download interrupted.
- Video generation not performed.

Cleanup:

- EC2 instance `i-090c7666371f00d68` terminated.
- EBS root volume cleaned up through `DeleteOnTermination=true`.
- No active smoke-test AWS processes remain.

Measured interim result:

- Runtime: approximately `40 minutes`.
- Approximate cost: `$0.67`.

## Current Decision

Project is paused. No AWS GPU runtime is active.

Before restarting, choose whether to:

1. restart immediately from scratch using the existing runbook;
2. first add a persistence strategy to avoid repeating environment setup and model download cost.

## Do-Not-Repeat Work

- Do not re-request AWS G/VT quota.
- Do not repeat Free Plan diagnosis; paid-plan upgrade is complete.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`; that was an incorrect earlier assumption.
- Do not restart AWS runtime without explicit owner approval.

## Re-entry Links

- Active coordination channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47
- EC2 Launch page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- Approved quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en
