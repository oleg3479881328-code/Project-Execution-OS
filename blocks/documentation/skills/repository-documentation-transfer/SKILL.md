# Repository Documentation Transfer

## Purpose

Use this skill when a reviewed documentation package must be transferred into a target repository safely.

## When To Use

Use when:
- the source package exists;
- transfer approval exists;
- the work is documentation-only;
- target verification must happen after write.

## Core Workflow

1. Verify source package.
2. Verify target repository state.
3. Transfer one file at a time.
4. Verify target files after write.
5. Return a transfer report.

## Depends On

- `blocks/documentation/standards/REPOSITORY_DOCUMENTATION_TRANSFER_STANDARD.md`
- `docs/CODEX_HANDOFF_STANDARD.md`
- `docs/REVIEW_STANDARD.md`

## Output

```text
TRANSFER REPORT

Status:
Source package:
Target repository:
Files transferred:
Commits:
Verification performed:
Blockers:
Ready for next step: Yes / No
```
