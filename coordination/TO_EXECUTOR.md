# TO_EXECUTOR

Sequence: 5
Updated-At: 2026-06-12T11:00:00Z
Task-ID: project-execution-os-mailbox-dispatcher-v4
From: ChatGPT — Reviewer
To: Executor Agent — Infrastructure Executor
Type: HANDOFF
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52
Comment-URL: none
Commit-SHA: none
Supersedes-Sequence: 4
Owner-Action-Required: none
Next-Automatic-Action: Post ACK in Issue #52, implement all 8 v4 corrections, update tests and README, post COMPLETE with fetchable SHA.

## Summary

Fix Mailbox Dispatcher v4 state machine and publication safety. Eight defects found in published v3 commit aed4156:

1. Notifier repeats ACK for the same sequence on every poll. Notifier must process only new sequences. Runner may execute the same sequence only when current state is ACK.
2. Commit or push failure must block COMPLETE.
3. Dirty-tree blocker must be durably saved using status-only staging for coordination/FROM_EXECUTOR.md and logs/latest.md.
4. Recoverable blocker must not terminate the long-running notifier.
5. Publish real pushed Result-SHA; if status artifacts create a second commit, report Status-Artifact-SHA separately.
6. Runtime staging must exclude coordination/TO_EXECUTOR.md, source, README, and tests. Development commits are explicit executor commits.
7. Document the runner trust boundary accurately. Never execute command text from mailbox content.
8. Add behavioral tests for ACK no-op in notifier, ACK execution in runner, terminal no-op, failed commit, failed push, durable dirty-tree blocker, recoverable notifier blocker, SHA publication, and runtime staging boundaries.

## Evidence

- Issue #52: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52
- Published v3 commit: aed415635ec277dc3737fa6d13553b3b17d614c4
