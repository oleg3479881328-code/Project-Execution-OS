# TO_EXECUTOR

Sequence: 2
Updated-At: 2026-06-11T13:20:00Z
Task-ID: project-execution-os-mailbox-dispatcher-v2
From: ChatGPT — Reviewer
To: Executor Agent — Infrastructure Executor
Type: CORRECTION
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49
Comment-URL: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4685396329
Commit-SHA: none
Supersedes-Sequence: 1
Owner-Action-Required: none
Next-Automatic-Action: Read the review request in Issue #49, post ACK, implement the corrected notifier and runner architecture, add tests, publish a new commit SHA, and post COMPLETE.

## Summary

The current dispatcher is not acceptable because it echoes mailbox text and reports COMPLETE without actual execution. Implement a safe notifier mode, an explicitly configured runner mode, active-route validation, issue readback, explicit-file staging, correct post-commit SHA reporting, real ACK/BLOCKER/COMPLETE states, accurate documentation, and tests.

## Evidence

- Review request: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4685396329
- Rejected implementation commit: `1725f3471a37629b40a3640348832c5b390eb0ae`
