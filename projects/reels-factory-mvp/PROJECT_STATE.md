# PROJECT STATE — Reels Factory MVP

Date: 2026-06-11
Status: active / paused after controlled AWS smoke-test stop
Transfer readiness: yes

## Current Phase

Resume planning after the first AWS smoke-test attempt was intentionally stopped by the owner before video generation.

## Current Goal

Validate the narrowest possible working pipeline:

`generated start image -> Wan Image-to-Video -> 3-second 480p low-quality test clip -> download result -> record runtime and cost -> terminate GPU runtime`

The first AWS attempt validated infrastructure setup only. It did not reach generation.

## Completed

### Project Decisions

- Use temporary rented GPU compute only.
- Do not buy hardware.
- Do not keep expensive GPU servers running permanently.
- Do not use SaaS video-generation platforms for the MVP.
- For the first smoke test, use one generated input image and test only the video layer.
- Generate the start image through ChatGPT rather than testing Flux in the first pass.
- Use Wan in Image-to-Video mode.
- First test duration: `3 seconds`.
- First test quality: minimum practical settings, target `480p`.
- First test concept: a simple car-motion scene to verify that the vehicle moves and an output video file is produced.

### RunPod Evaluation

RunPod onboarding was inspected but no payment was made.

Confirmed from the RunPod UI:

- Product route for our use case: `Pods`.
- GPU deployment requires prepaid RunPod credits.
- Preset funding amounts shown: `$150`, `$200`, `$250`, `$500`.
- `Other` allows a custom amount.
- Minimum custom funding amount: `$10`.
- No RunPod credits were purchased.

Decision:

- Keep RunPod as fallback only.
- Do not pay RunPod while AWS remains the preferred route.

### AWS Account And Credits

AWS account details provided by owner:

- AWS Account ID: `102885960265`
- Original plan: `AWS Free Plan`
- Paid-plan upgrade: completed by owner on `2026-06-10`
- Credits reported before smoke-test attempt: `$74.57`
- Approximate remaining credits after stop: `$73.90`
- Credit expiration: `2026-10-04`

### AWS EC2 GPU Quota

Region:

- `United States (Ohio)` / `us-east-2`

Quota:

- Name: `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Initial value: `0`
- Requested increase: `4` vCPU
- AWS Support case: `178112387200526`
- Support response: approved
- Applied value: `4`

Interpretation:

- AWS GPU access for one 4-vCPU G-family instance is enabled in Ohio.

### Canonical Execution Kit

Final reviewed kit commit:

- `3f7a245605a3afed5f7cd0c6c3758e68d3a8f282`

Canonical route:

- Instance: `g5.xlarge`
- GPU: NVIDIA A10G, 24 GB VRAM
- Compute price: `$1.006/hr` plus small EBS and IPv4 charges
- Model: `Wan2.1-I2V-14B-480P` FP16 Diffusers
- Workflow: `wanvideo_2_1_14B_I2V_example_03.json`
- Root volume: `100 GB gp3`
- Security: source-IP only; SSH tunneling preferred

Artifacts under `projects/reels-factory-mvp/`:

1. `AWS_INSTANCE_SELECTION.md`
2. `AWS_WAN_SMOKE_TEST_RUNBOOK.md`
3. `COST_TRACKING_TEMPLATE.md`

### First AWS Smoke-Test Attempt

Execution channel:

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

Resources created and used:

- EC2 instance: `i-090c7666371f00d68`
- Instance type: `g5.xlarge`
- Public IP during runtime: `3.144.84.183`
- Root volume: `100 GB gp3`

Validated during runtime:

- `g5.xlarge` launch worked after paid-plan upgrade.
- NVIDIA A10G GPU was detected.
- SSH access worked.
- ComfyUI installation completed.
- WanVideoWrapper installation completed.
- Model download for `Wan2.1-I2V-14B-480P` started.

Owner stop command:

- The owner explicitly ordered all processes stopped before generation.
- Model download was interrupted.
- Video generation was not performed.

Cleanup confirmed:

- EC2 instance `i-090c7666371f00d68` terminated.
- Temporary AWS processes stopped.
- `100 GB gp3` EBS volume cleaned up through `DeleteOnTermination=true`.
- No active smoke-test AWS resources remained after cleanup confirmation.

Measured interim result:

- Runtime: approximately `40 minutes`.
- Approximate cost: `$0.67`.

## In Progress

- No AWS runtime is active.
- Project is paused pending owner decision on the next restart strategy.

## Still Pending

1. Decide whether to restart on AWS immediately or optimize the restart plan first.
2. Recreate temporary GPU runtime only after owner approval.
3. Restore ComfyUI + WanVideoWrapper environment.
4. Download model and support files.
5. Generate one start image in ChatGPT.
6. Run one `3-second`, low-quality, `480p` Image-to-Video test.
7. Download result.
8. Record:
   - setup time;
   - model download time;
   - generation time;
   - total GPU runtime;
   - AWS cost;
   - storage cost;
   - output quality;
   - retries and failures.
9. Terminate runtime and verify cleanup again.

## Measured Interim Results

- RunPod minimum custom preload: `$10`.
- AWS GPU quota: `4` vCPU approved.
- Canonical AWS instance: `g5.xlarge`.
- First infrastructure-only attempt runtime: approximately `40 minutes`.
- First infrastructure-only attempt cost: approximately `$0.67`.
- ComfyUI + WanVideoWrapper setup path reached successfully.
- Generation quality and time remain unvalidated.

## Known Failures Or Fallbacks

- AWS Free Plan initially blocked non-Free-Tier GPU launch; owner resolved this by upgrading to paid plan.
- RunPod remains fallback and requires minimum `$10` prepaid credits.
- Recreating AWS runtime from scratch repeats installation and download cost unless a persistence strategy is chosen first.

## Validated

- AWS account has credits.
- AWS paid-plan upgrade completed.
- AWS EC2 GPU quota increase approved.
- `g5.xlarge` launches successfully under the approved quota.
- NVIDIA A10G is visible in runtime.
- SSH access works.
- ComfyUI installation works.
- WanVideoWrapper installation works.
- Controlled termination and cleanup works.

## Not Yet Validated

- Completed download of Wan model and support files.
- Actual Wan generation runtime for a 3-second 480p clip.
- Output quality.
- Cost of a completed generation attempt.
- Best persistence strategy for avoiding repeated setup cost.

## Next Safe Action

Before restarting paid GPU runtime, choose one of two bounded routes:

1. restart immediately using the existing runbook and accept repeated setup/download cost;
2. first add a persistence plan so model and environment reuse do not require rebuilding from scratch.

No AWS GPU runtime should be launched until the owner selects a route.

## Do-Not-Repeat Work

- Do not re-request AWS G and VT quota increase.
- Do not repeat the Free Plan diagnosis; paid-plan upgrade is complete.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`; it was an earlier incorrect assumption.
- Do not restart AWS runtime without owner approval.
- Do not leave temporary GPU resources active after future tests.

## Direct Links

- Active coordination channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47
- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- EC2 Launch page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- Approved quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en
- Runbook: `projects/reels-factory-mvp/AWS_WAN_SMOKE_TEST_RUNBOOK.md`
- Instance selection: `projects/reels-factory-mvp/AWS_INSTANCE_SELECTION.md`
- Cost template: `projects/reels-factory-mvp/COST_TRACKING_TEMPLATE.md`

## Cost-Control Rules

- Keep GPU runtime temporary only.
- Do not leave GPU instances running after a test.
- Verify disks and related resources explicitly after termination.
- Track compute time, storage cost, download/export time, and generation retries.
- Do not store secrets, payment data, API keys, or private SSH keys in the repository.
