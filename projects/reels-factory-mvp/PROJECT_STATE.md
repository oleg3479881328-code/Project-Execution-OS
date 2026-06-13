---
status: active
project_mode: lightweight
---

# PROJECT STATE — Reels Factory MVP

Date: 2026-06-13
Status: active / Stage 1 complete on revised 200 GB route / awaiting separate Stage 2 approval
Transfer readiness: yes

## Current Phase

Stage 1 was retried on the revised `200 GB gp3` route and completed through environment preparation, required downloads, AMI creation, cleanup, and evidence capture. Wait for separate owner authorization and an owner-provided image before any Stage 2 generation run.

## Current Goal

Stage 1 is complete on the revised `200 GB gp3` route.

Stage 2 later goal after separate authorization:

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
- Stage 1 and Stage 2 are separately authorized gates and must not be merged into one live run without a new issue instruction.

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
- AWS preflight in issue `#55` is complete.
- Active reply surface: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55`
- ACK comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698558728`
- PREFLIGHT_READY comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224`
- Two-stage plan ACK comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699388289`
- Stage 1 launch ACK comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699399516`
- Stage 1 heartbeat comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699419024`
- Stage 1 blocker comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699483930`
- Revised Stage 1 retry ACK comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699570581`
- Revised Stage 1 retry heartbeat comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699590406`
- Revised Stage 1 AMI wait heartbeat comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699653754`
- Revised Stage 1 slow-finalization heartbeat comment: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699775135`
- Reusable security group confirmed: `sg-080153ad3af390911` / `reels-factory-smoke-sg`
- Reusable key pair confirmed: `reels-factory-smoke-key`
- Local private key confirmed: `C:\Users\oleg3\Desktop\reels-factory-smoke-key.pem`
- Current owner source IP matches existing security-group rule: `147.0.42.138/32`
- Stage 1 first attempt on `100 GB gp3` remains useful blocker evidence only; do not retry that route.
- Revised Stage 1 retry instance `i-0389c71655647d968` was launched in `us-east-2a` from `ami-0ebb24e0f251b0442`, then stopped for AMI creation and terminated after AMI availability was verified.
- Revised Stage 1 root volume `vol-03915da0f636d5676` auto-deleted successfully on termination.
- Custom AMI created and verified: `ami-029a49547615ab978`
- Backing snapshot created and verified: `snap-000de430fb8b81a2b`
- Snapshot completion time: `2026-06-13T21:14:04.772Z`
- Snapshot logical stored size reported by AWS: `138882842624` bytes (`138.88 GB` decimal, about `129.34 GiB`)
- Current snapshot-storage estimate at `$0.05/GB-month`: about `$6.94/month`
- No active Reels Factory runtime, no Reels Factory EBS volume, and no Reels-specific Elastic IP remain after cleanup.

## Still Pending

1. Owner authorization for Stage 2.
2. Owner-provided start image for Stage 2.
3. Launch a temporary `g5.xlarge` from AMI `ami-029a49547615ab978`.
4. Start ComfyUI through SSH tunnel only.
5. Load the owner-provided image.
6. Run one `3-second`, `480p`, low-quality clip generation.
7. Download the MP4, record runtime/cost/quality, terminate the worker, and verify cleanup.

## Validated

- AWS paid-plan upgrade completed.
- AWS GPU quota increase approved.
- `g5.xlarge` launch works.
- `g5.xlarge` offering is currently visible in `us-east-2a`, `us-east-2b`, and `us-east-2c`.
- A10G GPU is visible.
- SSH works.
- ComfyUI install works.
- WanVideoWrapper install works.
- Controlled termination and EBS cleanup work.
- Persistence research supports custom AMI as the primary route.
- Read-only AWS account access works from the current executor session.
- No active or stopped Reels Factory smoke-test EC2 instance exists now.
- Stage 1 blocker on the old `100 GB gp3` route was confirmed and preserved as do-not-repeat evidence.
- Revised `200 GB gp3` Stage 1 retry completed:
  - instance `i-0389c71655647d968` final state `terminated`
  - root volume `vol-03915da0f636d5676` deleted
  - AMI `ami-029a49547615ab978` final state `available`
  - snapshot `snap-000de430fb8b81a2b` final state `completed`

## Not Yet Validated

- Completed Wan model and support-file download.
- Actual generation runtime and output quality.
- Actual cost of a completed generation.
- Actual AMI launch time on a fresh restore run.

## Next Safe Action

Wait for separate Stage 2 owner approval and an owner-provided start image in issue `#55`.

Do not request a start image proactively and do not run generation until Stage 2 is explicitly authorized.

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
