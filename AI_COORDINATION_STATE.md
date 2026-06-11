# AI Coordination State

## Project
Reels Factory MVP

## Purpose
Coordinate the AWS ComfyUI + Wan Image-to-Video smoke-test execution through one durable channel.

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47

## Previous Channels
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/46 — completed execution-kit preparation and review iterations
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/35 — previous unrelated Project Execution OS coordination channel
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/43 — previous unrelated server-rental coordination route

## Active Participants
- Oleg Povalyukhin — Project Owner
- ChatGPT — Reviewer
- Executor Agent — Infrastructure Executor

## Current Task
Confirm executor AWS access state, then continue only the already-approved Reels Factory MVP AWS smoke-test workflow after explicit owner authorization.

## Current Repository State
- Canonical execution kit commit: `3f7a245605a3afed5f7cd0c6c3758e68d3a8f282`
- Accepted route: `g5.xlarge` + `Wan2.1-I2V-14B-480P` FP16 Diffusers + `wanvideo_2_1_14B_I2V_example_03.json`
- Root volume: `100 GB gp3`
- Security: source-IP only; SSH tunneling preferred
- AWS GPU quota: `4 vCPU` approved in `us-east-2`
- AWS credits: `$74.57`, expire `2026-10-04`

## Accepted Changes
- Final preflight kit accepted for the next phase.
- Issue #47 is the only active durable reply surface for this phase.

## Open Review Items
- Await executor acknowledgement in Issue #47.
- Await explicit AWS access status: `AWS_ACCESS_READY`, `AWS_ACCESS_NOT_AVAILABLE`, or `AWS_ACCESS_NEEDS_IAM_SETUP`.
- Do not launch AWS resources until owner explicitly authorizes runtime execution.

## Next Step
When `02` is received:
1. read Issue #47;
2. inspect the latest executor acknowledgement and AWS access status;
3. continue from actual evidence;
4. ask the owner only for a real blocker or explicit launch approval.

## Required Validation
- Verify executor acknowledgement in Issue #47.
- Verify no AWS resource has been launched before owner authorization.
- After any runtime execution, require cost, runtime, output, and cleanup evidence in Issue #47.

## Update Rule
Update this snapshot only after a meaningful state transition.

## Reading Rule
Read this file first, then Issue #47, then inspect latest repository state if required.
