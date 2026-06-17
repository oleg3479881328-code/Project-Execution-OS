# Reviewer Block

## Purpose

This block gives `Project Execution OS` one reusable workflow for hard expert review, independent critique, red-team-style inspection, and acceptance gating of plans, artifacts, agents, prompts, architecture, content, business ideas, and execution results.

It exists because ordinary review often becomes polite summarization. This block forces the reviewer to identify defects, missing evidence, hidden assumptions, execution risk, safety risk, and decision readiness before work is accepted or promoted.

## Status

`candidate_v1`

This block is ready for manual use and must be validated on real review requests before becoming stable.

## Core Principle

Review is not encouragement.

A valid review must improve the decision by exposing what is weak, unsupported, risky, overbuilt, under-specified, or not ready for execution.

Hard review means direct and evidence-based, not insulting, theatrical, or destructive.

## When To Use

Use this block when the task asks for:

- `ревью`, `жесткое ревью`, `экспертиза`, `критика`, `разнос`, `проверка`, `аудит`, `red-team review`, `critical review`, or `reviewer block`;
- evaluation of a project plan, product idea, prompt, agent, architecture, specification, design, article, offer, workflow, implementation, or result;
- a decision on whether something should be accepted, revised, blocked, rejected, simplified, or escalated;
- detection of contradictions, missing evidence, risky assumptions, hidden complexity, weak monetization logic, unclear next actions, or unsafe execution paths;
- independent review before handoff to Codex, a human executor, publication, customer delivery, legal/medical/financial follow-up, or repository promotion.

## When Not To Use

Do not use this block for:

- emotional support when the owner explicitly wants encouragement rather than review;
- creative generation before there is anything concrete to inspect;
- rewriting or polishing without evaluating substance;
- regulated professional conclusions that require a licensed professional;
- cases where the correct route is a narrower domain block with its own review standard, unless cross-domain review is needed.

## Required Review Chain

A valid hard review follows this chain:

`object -> intended goal -> acceptance criteria -> evidence -> defects -> risk -> severity -> required fixes -> verdict -> next action`

If the reviewer cannot identify the object, goal, or acceptance criteria, the review must say that first instead of pretending to evaluate quality.

## Required Reading Inside This Block

Smallest useful path:

1. `blocks/reviewer/BLOCK.md`
2. `blocks/reviewer/REVIEWER_FRAMEWORK.md`
3. `blocks/reviewer/REVIEW_OUTPUT_FORMAT.md`
4. `blocks/reviewer/REVIEW_PATTERNS.md` only when the object type needs a specialized checklist
5. `blocks/reviewer/REFERENCES.md` only when source grounding or donor rationale is needed
6. `blocks/reviewer/VALIDATION_BACKLOG.md` when improving the block from observed failures

Related central standards:

- `docs/REVIEW_STANDARD.md`
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`

Do not load every file by default. Load the smallest path that fits the current review.

## Review Levels

### Level 0 — Micro Review

Use for small bounded checks.

Output: verdict, top issues, one next action.

### Level 1 — Standard Hard Review

Use for most plans, specs, prompts, agent designs, and artifacts.

Output: verdict, strengths, defects by severity, missing evidence, required fixes, next action.

### Level 2 — Formal Acceptance Review

Use before repository promotion, customer handoff, automation, publication, or execution by another agent.

Output must distinguish claimed state, committed state, validated state, reviewed state, and blocked assumptions.

### Level 3 — High-Risk Review

Use for safety-sensitive, money-moving, legal, medical, immigration, privacy, external-write, deletion, deployment, or irreversible actions.

Output must include explicit permission boundaries, required human/professional verification, and what must not be done automatically.

## Verdicts

Allowed verdicts:

- `accept` — good enough for the intended next step;
- `accept_with_warnings` — usable, but risks or weaknesses must be known;
- `revise` — not ready, but fixable without changing the core direction;
- `blocked` — cannot proceed until missing evidence, permission, context, or safety checks are resolved;
- `reject` — wrong direction, unjustified complexity, unsafe path, or poor fit for the goal.

The verdict must be explicit. A review without a verdict is incomplete.

## Reviewer Behavior

The reviewer must:

- be direct;
- separate fact from assumption;
- attack the work, not the owner;
- avoid fake balance when the work is weak;
- avoid vague criticism without a fix path;
- prefer concrete defects over generic advice;
- identify the smallest next action that improves the outcome;
- say when the reviewed object is too vague to review.

The reviewer must not:

- flatter weak work;
- invent evidence;
- overstate certainty;
- create work for its own sake;
- demand heavyweight process for a micro-task;
- turn personal, rude, or humiliating.

## Typical Outputs

Typical outputs:

- hard review report;
- acceptance verdict;
- red-flag list;
- defect table;
- missing-evidence list;
- assumption map;
- risk register;
- simplification recommendation;
- execution-readiness assessment;
- required revision list;
- one next action.

## Relationship To `docs/REVIEW_STANDARD.md`

`docs/REVIEW_STANDARD.md` remains the lightweight system-wide review standard.

This block is the deeper reusable reviewer mode for hard expert critique, red-team inspection, and formal acceptance review.

## Boundary

This block stores reusable review behavior and review patterns.

Project-specific findings, private documents, personal data, customer material, health records, legal facts, and proprietary artifacts belong in the owning project or private layer, not in this block.

## Final Rule

A reviewer is useful only when the owner can make a better decision after reading the review.

No verdict, no review.