# Latest Log — Reels Factory MVP

Date: 2026-06-10

## Session Summary

The owner explored two temporary GPU execution routes for the first Reels Factory MVP test.

### RunPod

- Opened RunPod onboarding.
- Selected `Pods` as the relevant product.
- Confirmed that GPU deployment requires prepaid credits.
- Verified that RunPod shows preset funding packages `$150`, `$200`, `$250`, `$500`.
- Verified that `Other` allows a custom funding amount.
- Verified that the minimum custom funding amount is `$10`.
- No payment was made.

### AWS

The owner reported an existing AWS account with:

- Account ID: `102885960265`
- Plan: `AWS Free Plan`
- Remaining credits: `$74.57`
- Credit expiration: `2026-10-04`

AWS EC2 was opened in region `United States (Ohio)` / `us-east-2`.

The quota `Running On-Demand G and VT instances` was checked:

- Quota code: `L-DB2E81BA`
- Applied account-level quota value: `0`
- Utilization: `0`

A quota increase request was submitted:

- Requested value: `4` vCPU
- Current status visible in request history: `Case Opened`

## Current Decision

Wait for AWS Support to process the quota request before spending money on RunPod.

## Next Re-entry Link

https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2
