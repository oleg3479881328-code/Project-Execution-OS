# Skill Review Standard v1

## Purpose

This standard defines how central reusable skills are reviewed before activation in `Project-Execution-OS`.

## Review Purpose

Review exists to prevent:

- prompt-dump degeneration;
- vague workflows;
- fake execution claims;
- duplicated skill scope;
- poor central-library quality;
- vendor lock-in hidden inside core skills;
- unmaintainable skill growth.

## Review Checklist

Every skill should be checked for:

- clear task boundary;
- defined inputs;
- defined outputs;
- workflow clarity;
- constraints;
- failure modes;
- source attribution;
- compatibility notes;
- validation checklist;
- lifecycle state;
- alignment with central governance.

## Failure Conditions

A skill fails review if:

- the task boundary is unclear;
- required inputs or outputs are missing;
- the workflow is too broad;
- references are missing without explanation;
- execution claims cannot be verified;
- the skill duplicates an existing active skill;
- the skill violates the central workflow or governance model.

## Approval Rules

A skill becomes `active` only if:

- review passes;
- lifecycle and review status are updated;
- references exist;
- workflow is reproducible;
- the skill is appropriate for central reuse.

## Reviewer Output

Reviewer output should include:

- strengths;
- risks;
- checklist results;
- approval or rejection;
- required corrections;
- follow-up status recommendation.
