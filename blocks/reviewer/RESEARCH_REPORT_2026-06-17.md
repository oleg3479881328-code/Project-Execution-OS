# Research Report — Reviewer Block — 2026-06-17

## Why This Block Exists

`Project Execution OS` already had `docs/REVIEW_STANDARD.md`, but that standard is intentionally short.

The owner requested a dedicated reviewer block for hard expert review.

The new block fills the gap between lightweight acceptance review and full domain-specific review.

## Method

The block was created using `skills/orchestration/domain-block-creation/SKILL.md`.

Research path:

1. inspect existing Project Execution OS review assets;
2. check current internal review standards;
3. check donor review practices from software review, AI risk review, application review, and evaluation frameworks;
4. create a small reusable block instead of a large document set.

## Internal Findings

Existing internal assets already cover:

- basic review scope and verdicts in `docs/REVIEW_STANDARD.md`;
- agent outcome and reliability metrics in `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`;
- donor-first behavior in `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`;
- block creation rules in `skills/orchestration/domain-block-creation/SKILL.md`.

Gap found:

There was no reusable `blocks/reviewer/` entrypoint for hard expert review, artifact critique, or acceptance-gate behavior across project types.

## External Donor Findings

### Google Engineering Practices

Google's code-review guidance treats review as a structured discipline with specific reviewer responsibilities, not a vague opinion pass.

Adapted principle:

- reviewer comments must be concrete and tied to artifact quality.

### NIST AI Risk Management Framework

NIST frames AI risk management as a lifecycle activity covering design, development, use, and evaluation.

Adapted principle:

- AI and agent reviews should inspect the workflow, not only the final answer.

### OWASP GenAI Top 10

OWASP's 2025 GenAI list is useful as a donor checklist for reviewing AI application behavior.

Adapted principle:

- reviews of AI-agent workflows must include tool, external-content, and information-handling checks.

### OpenAI Simple Evals

OpenAI's `simple-evals` repository demonstrates transparent benchmark-style evaluation for model-backed work.

Adapted principle:

- repeated AI workflows need representative task checks, not one impressive sample.

### Technical Peer Review Tradition

Technical peer review emphasizes early defect detection and structured inspection.

Adapted principle:

- reviewer output should expose defects early and require a clear next action.

## Design Decision

Created a compact block with:

- `BLOCK.md` — entrypoint and routing behavior;
- `REVIEWER_FRAMEWORK.md` — core review method;
- `REVIEW_OUTPUT_FORMAT.md` — reusable output formats;
- `REVIEW_PATTERNS.md` — object-specific checklists;
- `REFERENCES.md` — internal and external sources;
- `VALIDATION_BACKLOG.md` — assumptions to validate through real use.

## Deliberate Non-Goals

The block does not replace:

- narrow domain blocks;
- external expert judgment when required;
- actual testing, source verification, or user validation.

The block does not store project-specific review results.

## Current Status

Status: `candidate_v1`.

Ready for manual use.

Needs real review tasks before promotion.

## Next Validation Step

Use the block on the next real plan, prompt, agent, artifact, or project proposal and record whether the verdict and required fixes improved the next decision.