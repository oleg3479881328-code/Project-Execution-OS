# PROJECT STATE — Reels Factory MVP

Date: 2026-06-10
Status: active / MVP validation
Transfer readiness: yes

## Current Phase

Prepare the first AWS GPU execution step for a minimal Image-to-Video smoke test.

## Current Goal

Validate the narrowest possible working pipeline:

`generated start image -> Wan Image-to-Video -> 3-second 480p low-quality test clip -> download result -> record runtime and cost -> terminate GPU runtime`

This is intentionally narrower than the eventual 15-second reel. The purpose is to verify the infrastructure and video-generation path before testing quality, multi-scene storyboards, or factory automation.

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

- Do not pay RunPod yet.
- Keep RunPod as fallback if AWS becomes inconvenient or blocked.

### AWS Account And Credits

AWS account details provided by owner:

- AWS Account ID: `102885960265`
- Plan: `AWS Free Plan`
- Confirmed remaining credits: `$74.57`
- Credit expiration: `2026-10-04`

### AWS EC2 GPU Quota

Region checked:

- `United States (Ohio)` / `us-east-2`

Quota checked:

- Name: `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Initial applied account-level quota value: `0`
- Requested increase: `4` vCPU
- AWS Support case: `178112387200526`
- Support response: approved
- Current applied account-level quota value: `4`
- Current utilization: `0`

Interpretation:

- AWS GPU access for G and VT families is now enabled in Ohio for one small 4-vCPU instance.

### AWS Instance Selection (NEW)

- **Recommended instance:** `g4dn.xlarge` (4 vCPU, 16 GB VRAM T4, 16 GB RAM, 125 GB NVMe)
- **Hourly price:** $0.526/hr (On-Demand, Linux, us-east-2)
- **Why:** Cheapest G-family instance that fits the 4 vCPU quota and has sufficient VRAM for Wan I2V 1.3B (~6-8 GB)
- **Alternatives considered:** g5.xlarge ($1.006/hr), g6.xlarge (~$0.70/hr)
- **Wan model:** Wan2.1-I2V-1.3B (smallest practical I2V variant, ~3 GB download)
- **Deployment route:** Deep Learning AMI GPU PyTorch 2.x + manual ComfyUI install + ComfyUI-WanVideoWrapper custom node
- **Existing solutions checked:** ComfyUI official, ComfyUI-WanVideoWrapper (kijai), Wan2.1 official repo
- **Solution reused:** ComfyUI + ComfyUI-WanVideoWrapper (established community route, no custom scripting needed)

### Execution Kit Created (NEW)

The following artifacts are now available under `projects/reels-factory-mvp/`:

1. `AWS_INSTANCE_SELECTION.md` — justified instance recommendation with pricing and quota validation
2. `AWS_WAN_SMOKE_TEST_RUNBOOK.md` — complete step-by-step runbook with copy-ready commands
3. `COST_TRACKING_TEMPLATE.md` — measurement template for setup time, generation time, runtime, and cost

## In Progress

- Ready for owner to execute the first smoke test using the runbook.

## Still Pending

1. ~~Choose a specific EC2 GPU instance.~~ ✅ Done
2. Launch one temporary GPU instance only.
3. Deploy or install ComfyUI and the Wan model path.
4. Generate one start image in ChatGPT.
5. Run one `3-second`, low-quality, `480p` Image-to-Video test.
6. Download the result.
7. Record:
   - setup time;
   - model download time;
   - generation time;
   - total GPU runtime;
   - AWS cost;
   - storage cost;
   - output quality;
   - any failures or retries.
8. Terminate the GPU instance.
9. Remove or verify all paid storage and related resources that are not intentionally retained.

## Measured Interim Results

- RunPod minimum custom preload: `$10`.
- AWS promotional credit balance available: `$74.57`.
- AWS GPU quota successfully raised from `0` to `4` vCPU.
- Recommended instance: g4dn.xlarge at $0.526/hr.
- Estimated test cost: ~$0.53-1.60 (1-3 hours).

## Known Failures Or Fallbacks

- RunPod is not blocked, but it requires a minimum `$10` prepaid credit purchase.
- AWS initially blocked G-family GPU execution because quota was `0`; this blocker is resolved.
- If AWS GPU setup becomes operationally inefficient, return to RunPod and fund only the `$10` minimum.

## Validated

- AWS account has credits.
- AWS EC2 GPU quota increase request was approved.
- Applied quota now shows `4`.
- RunPod custom minimum was verified from the UI.
- g4dn.xlarge fits the 4 vCPU quota.
- g4dn.xlarge has sufficient VRAM (16 GB) for Wan I2V 1.3B.

## Not Yet Validated

- ~~Exact AWS instance type to use.~~ ✅ Done
- Actual AWS GPU runtime cost for Wan.
- Actual Wan install path and model download time on AWS.
- Actual generation time for a 3-second 480p clip.
- Output quality.
- Whether AWS credits cover all selected EC2 GPU and storage charges in practice.

## Next Safe Action

Execute the first smoke test using the runbook in `AWS_WAN_SMOKE_TEST_RUNBOOK.md`. Launch a g4dn.xlarge instance, install ComfyUI + Wan, generate one 3-second 480p clip, record results, and terminate.

## Do-Not-Repeat Work

- Do not re-open the RunPod onboarding research unless AWS is rejected as the execution path.
- Do not re-request AWS G and VT quota increase; it is already approved and applied.
- Do not pay RunPod while AWS credits are still the preferred first route.
- Do not test Flux during the first smoke test; ChatGPT supplies the input image.
- Do not start with 15 seconds or multi-scene output; first test is one 3-second low-quality clip.
- Do not re-research instance selection; g4dn.xlarge is already selected and justified.

## Direct Links

- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- EC2 Launch Instance page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- EC2 Service Quotas: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas?region=us-east-2
- Specific G and VT quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en
- Runbook: `projects/reels-factory-mvp/AWS_WAN_SMOKE_TEST_RUNBOOK.md`
- Instance selection: `projects/reels-factory-mvp/AWS_INSTANCE_SELECTION.md`
- Cost template: `projects/reels-factory-mvp/COST_TRACKING_TEMPLATE.md`

## Cost-Control Rules

- Keep GPU runtime temporary only.
- Do not leave GPU instances running after the test.
- Do not assume `Stop` removes every charge; verify disks and related resources explicitly.
- Check for paid EBS volumes after stopping or terminating any instance.
- Track compute time, storage cost, download/export time, and generation retries.
- Do not store account secrets, payment card information, API keys, or credentials in the repository.
