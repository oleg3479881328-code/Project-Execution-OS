# OSINT Validation Backlog

## Purpose

This file separates assumptions from validated workflows for the `OSINT Block`.

Research is not validation. The block must be tested on real tasks before it becomes mature.

## Validation Hypotheses

### H1 — Decision-first framing improves OSINT quality

Hypothesis: OSINT outputs become more useful when every task starts with a decision question instead of a broad search request.

Test with:

- vendor check;
- domain/site check;
- AI tool credibility check.

Success signal:

- output has a clear bottom line;
- sources directly support the decision;
- less irrelevant material is collected.

### H2 — Evidence labels reduce false confidence

Hypothesis: labels such as `CONFIRMED`, `LIKELY`, `WEAK`, `UNVERIFIED`, `CONTRADICTED`, and `RED_FLAG` make outputs safer and easier to act on.

Success signal:

- owner can quickly see what is proven vs assumed;
- later reviewer can verify the reasoning;
- unsupported claims are reduced.

### H3 — OSINT needs a reusable evidence-log template

Hypothesis: repeated tasks will require a standard table for evidence.

Candidate columns:

- finding;
- source;
- URL;
- access date;
- source type;
- evidence label;
- reliability note;
- implication;
- follow-up needed.

Success signal:

- easier attorney/CPA/operator handoff;
- easier continuation by another agent;
- fewer lost links and unsupported conclusions.

### H4 — Tool matrix should be use-case based, not tool-name based

Hypothesis: a tool matrix organized by investigation type is more useful than a generic list of OSINT tools.

Candidate categories:

- company/vendor;
- domain/site;
- public reputation;
- public cyber exposure;
- litigation/regulatory;
- marketplace/seller;
- AI tool/startup;
- public profile/person-related lawful review.

Success signal:

- future agents pick the right source category faster;
- less tool-chasing;
- better outputs for owner decisions.

### H5 — Storage boundary must be explicit

Hypothesis: OSINT outputs can contain sensitive information and should not automatically be saved into GitHub.

Success signal:

- sensitive reports stay in the appropriate private layer;
- GitHub stores reusable rules, not raw sensitive dossiers;
- owner gets a clear storage recommendation per investigation.

## Validation Tasks

- [ ] Run OSINT block on a company/vendor due diligence task.
- [ ] Run OSINT block on a domain/site credibility check.
- [ ] Run OSINT block on an AI tool/platform credibility check.
- [ ] Run OSINT block on a scam/fraud risk review.
- [ ] Run OSINT block on a timeline reconstruction task.
- [ ] Decide whether to add `PATTERNS.md`.
- [ ] Decide whether to add `TOOL_SELECTION_MATRIX.md`.
- [ ] Decide whether to add `REVIEW.md`.
- [ ] Decide whether to add `SECURITY_AND_COMPLIANCE.md` or keep safety rules inside `BLOCK.md`.

## Known Risks

- Turning OSINT into unsafe surveillance.
- Over-collecting irrelevant information.
- Treating search results as evidence.
- Confusing allegations with facts.
- Losing source dates and links.
- Saving sensitive investigation material to the wrong storage layer.
- Creating a tool list instead of a workflow.

## Current Status

Status: `candidate_v0`

The block is ready for controlled use on real tasks, but not yet mature.
