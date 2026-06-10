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

## In Progress

- Select the concrete EC2 GPU instance for the first smoke test.
- Confirm the cheapest practical AWS instance profile that fits Wan Image-to-Video with the current `4 vCPU` quota.

## Still Pending

1. Choose a specific EC2 GPU instance.
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

## Known Failures Or Fallbacks

- RunPod is not blocked, but it requires a minimum `$10` prepaid credit purchase.
- AWS initially blocked G-family GPU execution because quota was `0`; this blocker is resolved.
- If AWS GPU setup becomes operationally inefficient, return to RunPod and fund only the `$10` minimum.

## Validated

- AWS account has credits.
- AWS EC2 GPU quota increase request was approved.
- Applied quota now shows `4`.
- RunPod custom minimum was verified from the UI.

## Not Yet Validated

- Exact AWS instance type to use.
- Actual AWS GPU runtime cost for Wan.
- Actual Wan install path and model download time on AWS.
- Actual generation time for a 3-second 480p clip.
- Output quality.
- Whether AWS credits cover all selected EC2 GPU and storage charges in practice.

## Next Safe Action

Open AWS EC2 in `us-east-2`, inspect launch options, and select the cheapest practical GPU instance that fits within the approved `4 vCPU` G-family quota. Do not launch anything until the instance type and estimated hourly cost are reviewed.

## Do-Not-Repeat Work

- Do not re-open the RunPod onboarding research unless AWS is rejected as the execution path.
- Do not re-request AWS G and VT quota increase; it is already approved and applied.
- Do not pay RunPod while AWS credits are still the preferred first route.
- Do not test Flux during the first smoke test; ChatGPT supplies the input image.
- Do not start with 15 seconds or multi-scene output; first test is one 3-second low-quality clip.

## Direct Links

- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- EC2 Launch Instance page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- EC2 Service Quotas: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas?region=us-east-2
- Specific G and VT quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en

## Cost-Control Rules

- Keep GPU runtime temporary only.
- Do not leave GPU instances running after the test.
- Do not assume `Stop` removes every charge; verify disks and related resources explicitly.
- Check for paid EBS volumes after stopping or terminating any instance.
- Track compute time, storage cost, download/export time, and generation retries.
- Do not store account secrets, payment card information, API keys, or credentials in the repository.
