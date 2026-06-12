---
status: active
project_mode: lightweight
---

# PROJECT STATE — Reels Factory MVP

Date: 2026-06-11
Status: active / persistence strategy selected / AWS runtime stopped
Transfer readiness: yes

## Current Phase

Prepare the second AWS smoke-test attempt using a persistence-aware route.

## Current Goal

Validate the narrowest possible working pipeline:

`generated start image -> Wan Image-to-Video -> 3-second 480p low-quality clip -> download result -> record runtime and cost -> preserve reusable AMI -> terminate GPU runtime`

## Confirmed Decisions

- Use temporary rented GPU compute only.
- Do not buy hardware.
- Do not keep GPU instances running permanently.
- Use AWS first; keep RunPod as fallback only.
- Canonical GPU route: `g5.xlarge` in `us-east-2`.
- Model route: `Wan2.1-I2V-14B-480P` FP16 Diffusers.
- Workflow: `wanvideo_2_1_14B_I2V_example_03.json`.
- First generation target: one `3-second`, low-quality, `480p` car-motion clip.
- Generate the start image through ChatGPT.
- Do not expose ComfyUI port `8188` publicly. Use SSH tunneling and bind ComfyUI to `127.0.0.1`.

## AWS Account And Credits

- AWS Account ID: `102885960265`
- Region: `us-east-2` / Ohio
- Original plan: `AWS Free Plan`
- Paid-plan upgrade: completed on `2026-06-10`
- GPU quota: `Running On-Demand G and VT instances` raised from `0` to `4` vCPU
- AWS Support case: `178112387200526`
- Credits before first attempt: `$74.57`
- Approximate credits after first attempt: `$73.90`
- Credit expiration: `2026-10-04`

## Canonical Execution Kit

Reviewed execution kit commit:

- `3f7a245605a3afed5f7cd0c6c3758e68d3a8f282`

Artifacts:

1. `AWS_INSTANCE_SELECTION.md`
2. `AWS_WAN_SMOKE_TEST_RUNBOOK.md`
3. `COST_TRACKING_TEMPLATE.md`
4. `AWS_PERSISTENCE_STRATEGY.md`

## First AWS Smoke-Test Attempt

Execution channel:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

Validated:

- `g5.xlarge` launch works after paid-plan upgrade.
- NVIDIA A10G is detected.
- SSH works.
- ComfyUI installs successfully.
- WanVideoWrapper installs successfully.
- Wan model download starts successfully.

Stopped by owner command before generation:

- EC2 instance `i-090c7666371f00d68` terminated.
- `100 GB gp3` EBS cleaned up through `DeleteOnTermination=true`.
- No active smoke-test AWS resources remained.
- Runtime: approximately `40 minutes`.
- Approximate cost: `$0.67`.

## Persistence Strategy

Persistence report:

- `AWS_PERSISTENCE_STRATEGY.md`
- reviewed candidate commit: `e04e88e105375b148731b3f1d2861d56c36b6b67`

Selected primary route:

- Create a custom EBS-backed AMI after the next successful setup.
- Between tests, terminate the GPU worker.
- Retain only the AMI and its backing EBS snapshots.
- Expected storage estimate: about `$4/month` if stored snapshot blocks are about `80 GB`.
- Actual billed snapshot size must be measured after AMI creation.

Fallback:

- EBS snapshot-only route when a separate restore path is useful.

Temporary convenience route:

- Keep a stopped instance only when the next test is expected within days and the owner explicitly accepts the higher ongoing EBS cost.

## Current State

- No AWS GPU runtime is active.
- No persistent AMI exists yet.
- No new AWS resources should be created without owner approval.
- The persistence strategy is selected; live AMI creation remains unvalidated.

## Still Pending

1. Owner approval for the second AWS smoke-test run.
2. Launch fresh `g5.xlarge`.
3. Restore ComfyUI + WanVideoWrapper setup.
4. Download Wan model and support files completely.
5. Generate one start image in ChatGPT.
6. Run one `3-second`, `480p` Image-to-Video test.
7. Download result and record quality.
8. Stop instance and create custom AMI.
9. Wait until the AMI is available.
10. Record AMI ID, backing snapshot IDs, actual stored size, and estimated monthly storage cost.
11. Terminate the temporary GPU worker.
12. Verify EBS, Elastic IP, and snapshot cleanup.

## Validated

- AWS paid-plan upgrade completed.
- AWS GPU quota increase approved.
- `g5.xlarge` launch works.
- A10G GPU is visible.
- SSH works.
- ComfyUI install works.
- WanVideoWrapper install works.
- Controlled termination and EBS cleanup work.
- Persistence research supports custom AMI as the primary route.

## Not Yet Validated

- Completed Wan model and support-file download.
- Actual generation runtime and output quality.
- Actual cost of a completed generation.
- Actual AMI creation time.
- Actual AMI launch time.
- Actual billed snapshot size.

## Next Safe Action

Wait for owner approval before launching the second AWS smoke-test attempt.

On the approved run, complete setup and generation first, then create and verify the custom AMI before terminating the temporary GPU worker.

## Do-Not-Repeat Work

- Do not re-request AWS G and VT quota.
- Do not repeat Free Plan diagnosis; paid-plan upgrade is complete.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`; it was an incorrect earlier assumption.
- Do not open public port `8188`.
- Do not launch AWS runtime without explicit owner approval.
- Do not leave temporary GPU resources active after future tests.

## Direct Links

- Persistence correction channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48
- Previous execution channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47
- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- EC2 Launch page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- Approved quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en

## Cost-Control Rules

- Keep GPU runtime temporary only.
- Terminate GPU workers between tests.
- Verify disks and related resources explicitly after termination.
- Track compute time, storage cost, public IPv4 cost, download time, export time, and retries.
- Do not store secrets, payment data, API keys, or private SSH keys in the repository.
