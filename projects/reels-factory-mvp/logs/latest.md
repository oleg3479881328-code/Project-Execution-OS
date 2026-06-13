# Latest Log — Reels Factory MVP

Date: 2026-06-13
Checkpoint: revised 200 GB Stage 1 completed and cleaned up in issue #55

## Current Status

Reels Factory AWS execution remains split into two separately authorized stages.

Stage 1 is complete on the revised `200 GB gp3` route:

- custom AMI created and verified: `ami-029a49547615ab978`
- backing snapshot created and verified: `snap-000de430fb8b81a2b`
- temporary worker terminated
- root volume deleted automatically
- no active Reels Factory AWS runtime remains

Stage 2 is not authorized yet.

## Active Reply Surface

- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55

## Direct Comment URLs

- ACK: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698558728
- PREFLIGHT_READY: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4698565224
- Two-stage plan ACK: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699388289
- Stage 1 launch ACK: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699399516
- Stage 1 heartbeat: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699419024
- Stage 1 blocker: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699483930
- Revised Stage 1 retry ACK: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699570581
- Revised Stage 1 retry heartbeat: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699590406
- Revised Stage 1 AMI wait heartbeat: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699653754
- Revised Stage 1 slow-finalization heartbeat: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699775135

## Stage 1 Summary

First `100 GB gp3` attempt:

- blocked by insufficient root-volume capacity after partial model download
- blocker evidence preserved in issue and project state

Revised `200 GB gp3` retry:

- source instance: `i-0389c71655647d968`
- source AMI: `ami-0ebb24e0f251b0442`
- instance type: `g5.xlarge`
- availability zone: `us-east-2a`
- root volume: `vol-03915da0f636d5676`

Validated during Stage 1:

- SSH worked
- GPU visible: NVIDIA A10G
- ComfyUI cloned and Python venv created
- ComfyUI dependencies installed
- WanVideoWrapper cloned and dependencies installed
- custom AMI created and verified: `ami-029a49547615ab978`
- backing snapshot created and verified: `snap-000de430fb8b81a2b`
- snapshot completion time: `2026-06-13T21:14:04.772Z`
- snapshot logical stored size reported by AWS: `138882842624` bytes (`138.88 GB` decimal, about `129.34 GiB`)
- current snapshot-storage estimate at `$0.05/GB-month`: about `$6.94/month`

Cleanup after revised success:

- source instance `i-0389c71655647d968` terminated
- root volume `vol-03915da0f636d5676` deleted automatically
- no Reels Factory EBS volume remains
- no Reels-specific Elastic IP remained allocated

## Runtime And Cost

- first blocked `100 GB` attempt total estimate: about `$0.47`
- revised `200 GB` compute runtime from launch `2026-06-13T19:20:31Z` to stop `2026-06-13T19:42:39Z`: about `22m 08s`
- revised `200 GB` compute estimate: about `$0.37`
- revised temporary gp3 + IPv4 estimate before stop: under `$0.01`
- revised ongoing snapshot-storage estimate: about `$6.94/month`
- Stage 1 combined estimate so far: about `$0.84` one-time runtime cost plus about `$6.94/month` passive snapshot storage while the AMI is retained

## Next Safe Reels Factory Action

Wait for separate Stage 2 owner approval and an owner-provided start image in issue `#55`.

On an approved Stage 2 run:

1. launch fresh `g5.xlarge`;
2. boot from AMI `ami-029a49547615ab978`;
3. validate local-only ComfyUI startup if needed;
4. load the owner-provided image;
5. run one `3-second`, `480p`, low-quality clip;
6. download the MP4 and record timing, quality, and cost;
7. terminate the GPU worker and verify cleanup.

Do not request a start image proactively and do not run generation until Stage 2 is explicitly authorized.

## Do-Not-Repeat Work

- Do not re-request GPU quota.
- Do not repeat Free Plan diagnosis.
- Do not use `g4dn.xlarge` as the canonical route.
- Do not refer to `Wan2.1-I2V-1.3B`.
- Do not expose ComfyUI port `8188` publicly.
- Do not restart AWS runtime without explicit owner approval.
