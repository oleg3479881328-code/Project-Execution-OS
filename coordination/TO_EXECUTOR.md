# TO_EXECUTOR

Sequence: 16
Updated-At: 2026-06-13T13:05:00Z
Task-ID: reels-factory-mvp-aws-stage-1-preparation
From: ChatGPT — Reviewer
To: Executor Agent — Infrastructure Executor
Type: PLAN_AMENDMENT
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
Comment-URL: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699380801
Commit-SHA: none
Supersedes-Sequence: 15
Owner-Action-Required: Authorize Stage 1 preparation or decline.
Next-Automatic-Action: Read the two-stage plan amendment in Issue #55, acknowledge it, and wait. Do not launch any billable AWS resource until the owner explicitly authorizes Stage 1 preparation.

## Summary

Split the AWS path into two separately authorized stages. Stage 1 prepares ComfyUI, WanVideoWrapper, the full Wan model and support files, validates the environment, creates a reusable AMI, terminates the temporary worker, and stops. Stage 2 later launches from that AMI only after separate owner authorization and provision of the input image, then generates one 3-second 480p clip.

## Evidence

- Plan amendment: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55#issuecomment-4699380801
- Active issue: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/55
