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
Complete the remaining bounded corrections for the clean hybrid local-model preprocessing prototype in PR #30.

## Current Repository State
- Clean branch: `codex/issue-27-hybrid-agent-clean`
- Current head before correction: `cce2e18506f86d256054cfacb77be57e4acec5ac`
- PR #30 is open and mergeable but checks fail.
- Traceability gap remains: local compact-context references must be validated against bounded input evidence before trust.
- Integrity workflow fails because `docs/CONTEXT_ASSEMBLY_STANDARD.md` changed without refreshing `SYSTEM_CONTEXT_MANIFEST.md`.
- Additional scope finding: `docs/CONTEXT_ASSEMBLY_STANDARD.md` still carries unrelated semantic-index/context-entry additions that must be removed from the clean Issue #27 branch.
- Additional runtime-hygiene finding: default CLI runtime logs go under `logs/api-runtime/`, but repository ignore rules do not currently prevent untracked log noise.
- Reviewer posted a consolidated in-scope correction request in PR #30 and triggered Codex with `@codex address that feedback`.

## Open Review Items
- Remove unrelated semantic-index/context-entry additions from `docs/CONTEXT_ASSEMBLY_STANDARD.md`.
- Keep only the narrow hybrid local-preprocessing extension.
- Validate local excerpt paths and line ranges.
- Validate suspected module paths or reject unsupported references.
- Add regression tests for invented paths and invalid ranges.
- Prevent runtime-log repository noise through ignore rule or safer default path.
- Refresh `SYSTEM_CONTEXT_MANIFEST.md` after final context-standard content settles.
- Re-run unit tests, benchmark, and manifest validator.
- Inspect new PR head and workflow result.

## Next Step
When `02` is received:
1. open PR #30 directly;
2. read latest executor reply and current head SHA;
3. inspect changed files and workflow status;
4. verify unrelated semantic-index additions are gone;
5. verify runtime-log hygiene fix and traceability tests;
6. continue review immediately;
7. do not return to Issue #27 unless historical context is required.

## Reading Rule
For `02`, read this file first, then PR #30, then repository evidence. Read `AI_COORDINATION_LOG.md` only when history is required.
