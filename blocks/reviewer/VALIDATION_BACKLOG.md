# Reviewer Block Validation Backlog

## Purpose

Keep assumptions separate from proven behavior.

The block starts as `candidate_v1`.

## Checks To Run

### V1 — Verdict usefulness

Run the block on five real reviews.

Record whether the explicit verdict helped choose the next action.

Status: `not_checked`

### V2 — Severity usefulness

Run reviews with issue priority labels.

Record whether the labels helped separate blockers from improvements.

Status: `not_checked`

### V3 — Small-task fit

Use the micro review format on small artifacts.

Record whether the output stayed short and actionable.

Status: `not_checked`

### V4 — Pattern coverage

Use at least two patterns from `REVIEW_PATTERNS.md`.

Record whether the pattern caught issues the generic format would miss.

Status: `not_checked`

### V5 — Tone fit

Track whether the owner accepts the tone as direct and useful.

Status: `not_checked`

## Known Risks

- Too much process for small tasks.
- Too much focus on defects.
- Too many requests for evidence when a fast test would be better.
- Overlap with narrower domain blocks.
- Verdict too confident when evidence is thin.

## Candidate Improvements

- Russian short format.
- Concise hard-review mode.
- Option-comparison scorecard.
- Repository promotion checklist.
- Extra patterns after repeated use.

## Promotion Criteria

Promote to `candidate_v2` when:

- five real reviews are completed;
- two review patterns are used;
- verdicts lead to clear next actions;
- at least one improvement is made from real use.

## Final Rule

Stability requires repeated useful reviews.