# AI Coordination State

## Project
Project Execution OS / MarkItDown Intake Adapter

## Purpose
Implement and validate a local-only Windows-first MarkItDown document intake adapter for agent and knowledge-pipeline use without exposing remote fetching, paid OCR, Azure calls, or MCP services.

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51

## Review Surface
https://github.com/oleg3479881328-code/Project-Execution-OS/pull/53

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Previous Channels
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52 — queued Mailbox Dispatcher v5 correction; do not activate until Issue #51 review completes
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49 — previous mailbox dispatcher review thread
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48 — Reels Factory persistence-strategy correction completed
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47 — Reels Factory AWS smoke-test execution and first persistence draft
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/46 — execution-kit preparation and review iterations

## Active Participants
- Oleg Povalyukhin — Project Owner
- ChatGPT — Reviewer
- Codex — Executor Agent

## Current Task
Review the bounded MarkItDown local intake adapter MVP published in Draft PR #53.

## Current Repository State
- Active outbound mailbox sequence on `main`: `6`
- Active handoff packet: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
- Recovery notice: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4690906540
- Completion report: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4691080594
- Review receipt: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4691203230
- Draft PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/53
- Review branch: `codex/issue-51-markitdown-adapter`
- Review branch head SHA: `1daacf39abbcc5558ae6ddcbb5461a38e09a714a`
- PR state: open / draft / mergeable
- Root inbound mailbox on `main` is stale at sequence `5`; the sequence `6` COMPLETE mirror exists in Draft PR #53 branch diff and the authoritative completion report is in Issue #51.
- Mailbox Dispatcher v4 report commit `b893038c222a4926ac37ae55d67254b0dc14e683` is published but rejected in review.
- Mailbox Dispatcher v5 correction remains queued in Issue #52: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52#issuecomment-4690902781
- No paid cloud services or external runtime resources are authorized for the MarkItDown task.

## Accepted Changes
- Reuse Microsoft's official `microsoft/markitdown` package instead of building a parser from scratch.
- Use the narrow local-only `convert_local()` API for the MVP.
- Keep implementation isolated under `tools/markitdown-intake-adapter/`.
- Reject URL-like inputs.
- Treat OCR, Azure, MCP, external URL fetching, and paid services as out of scope.
- Use Issue #51 as the active coordination surface until PR review feedback is posted.
- Keep Mailbox Dispatcher v5 queued separately until Issue #51 review completes.

## Open Review Items
- Review Draft PR #53 diff and validation evidence.
- Verify official package metadata and pinned version.
- Verify clean adapter-only implementation scope.
- Verify URL rejection and local-only conversion path.
- Verify smoke-test results for seven ordinary formats plus one `NEEDS_OCR` scan.
- Verify native Windows PowerShell validation disclosure.
- Decide whether to accept PR #53 or post bounded correction feedback.

## Queued Follow-Up
Mailbox Dispatcher v5 remains queued in Issue #52 after Issue #51 review completes. Required fixes include strict git return-code handling, route preservation, structured adapter result semantics, explicit `Result-SHA` and `Status-Artifact-SHA`, runtime-only dirty-tree policy, accurate trust-boundary documentation, and isolated behavioral tests.

## Next Step
Review Draft PR #53. Do not ask the owner to relay anything unless review finds a correction that must be sent to Codex.

## Required Validation
- Verify `MarkItDown().convert_local(...)` is used, not permissive `convert(...)`.
- Verify remote URL-like inputs are rejected.
- Verify Python `>=3.10` requirement and pinned official dependency.
- Verify PowerShell scripts resolve relative to their own location.
- Verify no network conversion, Azure, OCR plugin, MCP exposure, or secrets are introduced.
- Verify smoke tests cover PDF text, PDF scan, DOCX, PPTX, XLSX, HTML, CSV, and ZIP.
- Verify ordinary samples pass and scan yields `NEEDS_OCR` or a documented official-library equivalent.
- Verify repository diff contains only allowed adapter and coordination files.

## Update Rule
Update this snapshot only after meaningful state transitions.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #51, then Draft PR #53 and repository evidence.
