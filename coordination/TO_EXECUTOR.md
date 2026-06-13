# TO_EXECUTOR

Sequence: 17
Updated-At: 2026-06-13T13:12:00Z
Task-ID: reels-factory-mvp-aws-stage-1-authorized
From: Oleg Povalyukhin — Project Owner
To: Executor Agent — Infrastructure Executor
Type: OWNER_AUTHORIZATION
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
Comment-URL: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699393768
Commit-SHA: none
Supersedes-Sequence: 16
Owner-Action-Required: none
Next-Automatic-Action: Read the Stage 1 authorization in Issue #55, post ACK, execute Stage 1 preparation automatically through STAGE_1_COMPLETE or BLOCKER, terminate the temporary GPU worker after AMI availability is verified, and stop before Stage 2.

## Summary

Stage 1 AWS preparation is authorized. Launch one temporary `g5.xlarge`, install or restore ComfyUI and WanVideoWrapper, download the full Wan model plus T5 encoder, CLIP vision, and VAE, validate the environment, create and verify a reusable AMI, record runtime and storage evidence, terminate the temporary worker, verify cleanup, publish `STAGE_1_COMPLETE` or `BLOCKER`, and stop. Do not request an image and do not run video generation.

## Evidence

- Owner authorization: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699393768
- Active issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
- Two-stage plan: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699380801
