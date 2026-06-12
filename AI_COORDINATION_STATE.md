# AI Coordination State

## Project
Project Execution OS / MarkItDown Intake Adapter

## Purpose
Implement and validate a local-only Windows-first MarkItDown document intake adapter for agent and knowledge-pipeline use without exposing remote fetching, paid OCR, Azure calls, or MCP services.

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51

## Mailboxes
- Reviewer to executor: `coordination/TO_EXECUTOR.md`
- Executor to reviewer: `coordination/FROM_EXECUTOR.md`

## Previous Channels
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/49 — mailbox dispatcher v3 publication checkpoint reached; reported SHA `aed415635ec277dc3737fa6d13553b3b17d614c4`
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/48 — Reels Factory persistence-strategy correction completed
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/47 — Reels Factory AWS smoke-test execution and first persistence draft
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/46 — execution-kit preparation and review iterations

## Active Participants
- Oleg Povalyukhin — Project Owner
- ChatGPT — Reviewer
- Codex — Executor Agent

## Current Task
Implement the bounded internal MarkItDown intake adapter MVP under `tools/markitdown-intake-adapter/` according to Issue #51.

## Current Repository State
- Active outbound mailbox sequence: `5`
- Active handoff packet: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51
- Active origin notice: https://github.com/oleg3479881328-code/Project-Execution-OS/issues/51#issuecomment-4686336664
- Active route commit: `a35dc538048fee1d29852a2b0e24eecd66806283`
- Outbound mailbox commit: `4a9ffa8b5f7f2c493745a5771c8c83fda6fd9abc`
- Prior mailbox dispatcher v3 report: `aed415635ec277dc3737fa6d13553b3b17d614c4`
- No paid cloud services or external runtime resources are authorized for the MarkItDown task.

## Accepted Changes
- Reuse Microsoft's official `microsoft/markitdown` package instead of building a parser from scratch.
- Use the narrow local-only `convert_local()` API for the MVP.
- Keep implementation isolated under `tools/markitdown-intake-adapter/`.
- Reject URL-like inputs.
- Treat OCR, Azure, MCP, external URL fetching, and paid services as out of scope.
- Use one dedicated reply surface: Issue #51.

## Open Review Items
- Wait for executor `ACK` in Issue #51 and matching `coordination/FROM_EXECUTOR.md` update.
- Verify official package metadata and pinned version.
- Verify clean adapter-only implementation scope.
- Verify URL rejection and local-only conversion path.
- Verify smoke-test results for seven ordinary formats plus one `NEEDS_OCR` scan.
- Verify native Windows PowerShell validation or explicit disclosure that it was not performed.
- Review draft PR and commit evidence.

## Next Step
When `02` is received:
1. read `blocks/communication-channel/ACTIVE_CHANNEL_ROUTE.md`;
2. read `coordination/FROM_EXECUTOR.md`;
3. read Issue #51 for supporting evidence;
4. inspect the reported commit and draft PR when available;
5. continue review from mailbox sequence `5`.

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
Read the active route, then the inbound mailbox, then the active issue and repository evidence.
