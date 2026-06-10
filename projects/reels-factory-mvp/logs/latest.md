# Latest Log — Reels Factory MVP

Date: 2026-06-10

## Session Summary

The owner completed the infrastructure-access phase for the first Reels Factory MVP smoke test.

## RunPod

- Opened RunPod onboarding.
- Selected `Pods` as the relevant product.
- Confirmed that GPU deployment requires prepaid credits.
- Verified preset funding packages: `$150`, `$200`, `$250`, `$500`.
- Verified that `Other` allows a custom funding amount.
- Verified minimum custom funding amount: `$10`.
- No payment was made.

Decision:

- Keep RunPod as fallback only.
- Do not fund RunPod while AWS credits are available and AWS GPU quota is enabled.

## AWS

The owner reported an existing AWS account with:

- Account ID: `102885960265`
- Plan: `AWS Free Plan`
- Remaining credits: `$74.57`
- Credit expiration: `2026-10-04`

AWS EC2 was opened in region:

- `United States (Ohio)` / `us-east-2`

Quota checked:

- Name: `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Initial value: `0`
- Utilization: `0`

Quota increase request submitted:

- Requested value: `4` vCPU
- AWS Support case: `178112387200526`
- Initial request status: `Case Opened`

AWS Support email received and read:

- Result: approved
- Approved limit: `4`
- Applied account-level quota value later confirmed in console: `4`

## First Smoke Test Scope

The first execution test was intentionally narrowed:

`ChatGPT-generated start image -> Wan Image-to-Video -> 3-second 480p low-quality clip -> download result -> record cost and runtime -> terminate GPU`

First concept:

- one simple vehicle-motion scene;
- objective: confirm that the car moves and a video file is produced;
- no Flux test yet;
- no 15-second reel yet;
- no multi-scene storyboard yet.

## Current Decision

Proceed with AWS first because promotional credits already exist and the G-family quota blocker is resolved.

## Next Safe Action

Open the AWS EC2 launch page in Ohio, inspect available G-family GPU instances, and review hourly pricing before launching anything.

## Do-Not-Repeat Work

- Do not re-request AWS G/VT quota.
- Do not pay RunPod yet.
- Do not start with 15 seconds.
- Do not add Flux to the first smoke test.

## Re-entry Links

- EC2 Launch Instance page: https://console.aws.amazon.com/ec2/home?region=us-east-2#LaunchInstances:
- Approved quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
- AWS Support case: https://console.aws.amazon.com/support/home#/case/?displayId=178112387200526&language=en
