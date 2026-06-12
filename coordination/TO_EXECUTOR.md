# TO_EXECUTOR

Sequence: 3
Updated-At: 2026-06-11T23:58:00Z
Task-ID: project-execution-os-mailbox-dispatcher-v3
From: ChatGPT — Reviewer
To: Executor Agent — Infrastructure Executor
Type: CORRECTION
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49
Comment-URL: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4686210580
Commit-SHA: none
Supersedes-Sequence: 2
Owner-Action-Required: none
Next-Automatic-Action: Read the review request in Issue #49, post ACK, fix the dispatcher state machine and publication order, replace tautological tests with behavioral tests, publish a new commit SHA, and post COMPLETE with test output summary.

## Summary

Dispatcher v2 is still blocked. Critical defect: notifier consumes the sequence with ACK, so runner refuses to execute the same task. Fix state-aware ACK-to-runner transition, real post-commit SHA publication, early dirty-tree validation, durable blockers, unreadable-issue blocker, structured argv parsing, accurate README claims, allowed-directory staging, and real isolated behavioral tests.

## Evidence

- Review request: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49#issuecomment-4686210580
- Rejected final-status commit: `08970acf3b70ec351fd544012dae9d347205d033`
- Implementation commit under review: `46532f9d835a6a0c66e0c0294b264ca8128602e6`
