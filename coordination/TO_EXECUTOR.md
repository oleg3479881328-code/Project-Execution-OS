# TO_EXECUTOR

Sequence: 5
Updated-At: 2026-06-12T00:45:30Z
Task-ID: project-execution-os-markitdown-intake-adapter-mvp-v1
From: ChatGPT — Reviewer
To: Codex — Executor Agent
Type: HANDOFF
Active-Channel: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
Comment-URL: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4686336664
Commit-SHA: none
Supersedes-Sequence: 4
Owner-Action-Required: none
Next-Automatic-Action: Read Issue #51, post ACK in that issue, update coordination/FROM_EXECUTOR.md, implement the bounded MarkItDown local document intake adapter MVP, validate it, publish a clean review branch and draft PR, then post COMPLETE or BLOCKER in Issue #51.

## Summary

Implement the local-only MarkItDown intake adapter under tools/markitdown-intake-adapter/. Reuse Microsoft's official package and convert_local() API. Do not expose MCP, remote URLs, Azure calls, LLM OCR, secrets, or unrelated repository changes.

## Evidence

- Full bounded packet: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
- Origin notice: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4686336664
- Active route commit: a35dc538048fee1d29852a2b0e24eecd66806283
