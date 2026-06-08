# AI Coordination State

## Project
Project Execution OS

## Purpose
Compact operational snapshot for multi-agent coordination. Read this file before processing shorthand command `02`.

## Active Channel
https://github.com/oleg3479881328-code/Project-Execution-OS/pull/30

## Previous Channels
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/27 — implementation issue and execution-report history
- https://github.com/oleg3479881328-code/Project-Execution-OS/issues/28 — completed executor start-now standard fix

## Current Task
Complete review corrections for the clean hybrid local-model preprocessing prototype in PR #30.

## Current Repository State
- Clean branch: `codex/issue-27-hybrid-agent-clean`
- Current head before correction: `cce2e18506f86d256054cfacb77be57e4acec5ac`
- PR #30 is open and mergeable but checks fail.
- Review thread identified a traceability gap: local compact-context references must be validated against bounded input evidence before trust.
- Integrity workflow fails in `Validate system context manifest` because `docs/CONTEXT_ASSEMBLY_STANDARD.md` changed without the corresponding `SYSTEM_CONTEXT_MANIFEST.md` refresh.
- Reviewer posted an in-scope correction request in PR #30. No owner confirmation is required.

## Open Review Items
- Validate local excerpt paths and line ranges.
- Validate suspected module paths or reject unsupported references.
- Add regression tests for invented paths and invalid ranges.
- Refresh `SYSTEM_CONTEXT_MANIFEST.md`.
- Re-run unit tests, benchmark, and manifest validator.
- Inspect new PR head and workflow result.

## Next Step
When `02` is received:
1. open PR #30 directly;
2. read latest executor reply and current head SHA;
3. inspect changed files and workflow status;
4. continue review immediately;
5. do not return to Issue #27 unless historical context is required.

## Reading Rule
For `02`, read this file first, then PR #30, then repository evidence. Read `AI_COORDINATION_LOG.md` only when history is required.
