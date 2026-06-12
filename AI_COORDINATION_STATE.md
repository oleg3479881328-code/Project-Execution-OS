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
Apply bounded review fixes for the MarkItDown local intake adapter MVP in Draft PR #53.

## Current Repository State
- Active outbound mailbox sequence on `main`: `7`
- Active handoff packet: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
- Draft PR: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/53
- Review packet: https://github.com/oleg3479881328-code/Project-Execution-OS/pull/53#issuecomment-4691237811
- Issue #51 continuation notice: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4691239320
- Review branch: `codex/issue-51-markitdown-adapter`
- Previous review branch head SHA: `1daacf39abbcc5558ae6ddcbb5461a38e09a714a`
- PR state: open / draft / mergeable
- Root inbound mailbox on `main` remains stale at sequence `5`; authoritative replies are read from Issue #51 and Draft PR #53 until Codex publishes the next update.
- Reels Factory project-state validation frontmatter was repaired separately on `main` in commit `0ac785e5560bc59e5bec22288a29d5cbf08f4f3d`.
- Mailbox Dispatcher v5 correction remains queued in Issue #52: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/52#issuecomment-4690902781
- No paid cloud services or external runtime resources are authorized for the MarkItDown task.

## Accepted Changes
- Reuse Microsoft's official `microsoft/markitdown` package instead of building a parser from scratch.
- Pin verified `markitdown 0.1.6`.
- Use the narrow local-only `convert_local()` API.
- Keep implementation isolated under `tools/markitdown-intake-adapter/`.
- Treat OCR, Azure, MCP, external URL fetching, and paid services as out of scope.
- Use Issue #51 as the active coordination surface and Draft PR #53 as the review surface.
- Keep Mailbox Dispatcher v5 queued separately until Issue #51 review completes.

## Open Review Items
- Wait for Codex `ACK` for mailbox sequence `7` in Draft PR #53.
- Fix `bootstrap.ps1` interpreter selection so installed Python `>=3.10` works without unsafe array slicing or 3.12-only behavior.
- Force deterministic `PYTHON_DOTENV_DISABLED=1` before importing `markitdown`.
- Reject Windows network-share and device-namespace paths in both wrappers.
- Add automated rejection checks to the validation report.
- Update the branch from current `main` and rerun CI.
- Verify corrected diff remains bounded and excludes Mailbox Dispatcher files.

## Queued Follow-Up
Mailbox Dispatcher v5 remains queued in Issue #52 after Issue #51 review completes. Required fixes include strict git return-code handling, route preservation, structured adapter result semantics, explicit `Result-SHA` and `Status-Artifact-SHA`, runtime-only dirty-tree policy, accurate trust-boundary documentation, and isolated behavioral tests.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #51 and Draft PR #53 comments;
4. inspect the newly reported branch SHA and workflow result;
5. continue review from mailbox sequence `7`.

## Required Validation
- Verify robust Python `>=3.10` PowerShell selection.
- Verify `MarkItDown().convert_local(...)` remains the only conversion API used.
- Verify URL-like, Windows network-share, and device-namespace inputs are rejected.
- Verify deterministic `.env` suppression before `markitdown` import.
- Verify PowerShell scripts resolve paths relative to their own location.
- Verify no network conversion, Azure, OCR plugin, MCP exposure, or secrets are introduced.
- Verify smoke tests cover PDF text, PDF scan, DOCX, PPTX, XLSX, HTML, CSV, ZIP, and rejection cases.
- Verify ordinary samples pass and scan yields `NEEDS_OCR`.
- Verify repository diff contains only allowed adapter and coordination files.
- Verify CI passes after branch update.

## Update Rule
Update this snapshot only after meaningful state transitions.

## Reading Rule
Read the active route, then the inbound mailbox, then Issue #51, then Draft PR #53 and repository evidence.
