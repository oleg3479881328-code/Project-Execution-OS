# PROJECT STATE — Reels Factory MVP

Date: 2026-06-10
Status: active / MVP validation

## Current Goal

Produce one original 15-second vertical animated reel using temporary rented GPU compute only, with three storyboard-controlled scenes of five seconds each.

## Current Infrastructure Decision

Do not pay RunPod yet. Prefer AWS first because the existing AWS account already has promotional credit balance available.

AWS account details provided by owner:

- AWS Account ID: `102885960265`
- Plan: `AWS Free Plan`
- Confirmed remaining credits: `$74.57`
- Credit expiration: `2026-10-04`

## AWS EC2 GPU Quota Check

Region checked:

- `United States (Ohio)` / `us-east-2`

Quota checked:

- `Running On-Demand G and VT instances`
- Quota code: `L-DB2E81BA`
- Current applied account-level quota value: `0`
- Current utilization: `0`

Interpretation:

- AWS account has credits, but GPU EC2 instances in the G and VT family cannot be launched yet because the quota is zero.

Quota increase request submitted:

- Requested quota value: `4` vCPU
- Request date: `2026-06-10`
- Current visible status: `Case Opened`
- Meaning: AWS Support case has been created and the request is awaiting review.

## Direct Links

- EC2 Console: https://console.aws.amazon.com/ec2/home?region=us-east-2
- EC2 Service Quotas: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas?region=us-east-2
- Specific G and VT quota page: https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-DB2E81BA?region=us-east-2

## RunPod Check

RunPod account setup was inspected but no payment was made.

Confirmed from the RunPod UI:

- RunPod uses prepaid credits for GPU deployment.
- Preset amounts shown: `$150`, `$200`, `$250`, `$500`.
- There is also an `Other` option with a custom amount field.
- Minimum custom credit amount: `$10`.
- No RunPod credits were purchased.

Decision:

- Do not pay RunPod while AWS GPU access is still being evaluated.
- Revisit RunPod only if AWS quota approval is denied, delayed too long, or operationally inconvenient.

## Next Step

Wait for AWS quota request status to change from `Case Opened` to an approval or denial state.

If approved:

1. choose a suitable EC2 GPU instance;
2. launch a temporary instance only;
3. install or deploy the ComfyUI + Wan test environment;
4. generate the first three five-second clips;
5. download outputs;
6. terminate the GPU instance and remove unnecessary storage;
7. record real cost, runtime, and quality outcome.

If denied or delayed materially:

1. return to RunPod;
2. fund only the minimum `$10`;
3. select a temporary ComfyUI/Wan-compatible Pod;
4. complete the same tracked MVP test.

## Cost-Control Rules

- Keep GPU runtime temporary only.
- Do not leave GPU instances running after the test.
- Check for paid persistent disks after stopping or terminating any instance.
- Track compute time, storage cost, download/export time, and generation retries.
- Do not store account secrets, payment card information, API keys, or credentials in the repository.
