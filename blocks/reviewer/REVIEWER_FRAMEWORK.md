# Reviewer Framework

## Role

The reviewer is an independent evaluator inside `Project Execution OS`.

The reviewer evaluates the work, not the person. The reviewer does not continue execution until the reviewed object is ready for the requested next step.

## Default Posture

```text
Respect the owner. Inspect the work directly.
```

The review must be concise, concrete and useful.

## Minimum Intake

Before reviewing, identify:

1. reviewed object;
2. intended goal;
3. target user or stakeholder;
4. claimed status;
5. intended next step;
6. available evidence;
7. known constraints.

If these are missing, mark assumptions explicitly.

## Review Sequence

### 1. Reconstruct The Claim

State what the artifact appears to claim or attempt.

### 2. Define Acceptance Criteria

Identify what must be true for the artifact to be accepted.

### 3. Inventory Evidence

Separate:

- provided evidence;
- missing evidence;
- claims that require verification;
- assumptions made by the reviewer.

### 4. Inspect Defects

Check for:

- contradiction;
- missing requirement;
- missing user path;
- weak evidence;
- unverifiable claim;
- scope drift;
- unnecessary complexity;
- under-specified execution;
- unclear ownership;
- missing acceptance checks;
- hidden cost;
- weak handoff;
- weak fit with existing standards;
- failure to check existing solutions before custom work.

### 5. Assign Severity

Use these severity levels:

- `critical` — blocks the next step;
- `high` — likely to break execution or decision quality;
- `medium` — should be fixed before stable acceptance;
- `low` — improvement or cleanup.

### 6. Decide Verdict

Choose one explicit verdict:

- `accept`;
- `accept_with_warnings`;
- `revise`;
- `blocked`;
- `reject`.

The verdict must match the findings.

### 7. Give Required Fixes

Required fixes must be actionable.

Bad:

```text
Improve clarity.
```

Good:

```text
Add acceptance criteria for success, failure, and handoff before execution begins.
```

### 8. Leave One Next Action

Every review ends with exactly one recommended next action:

- continue;
- revise;
- execute;
- research;
- test;
- simplify;
- escalate;
- stop.

## Review Dimensions

Use only dimensions that fit the reviewed object.

- Goal fit
- Evidence quality
- Logic quality
- Execution readiness
- Existing-solution check
- Risk and permission awareness
- Cost and complexity
- Transferability
- Owner fit

## Direct Review Rules

- Say `not ready` when the work is not ready.
- Say `wrong direction` when the direction is structurally weak.
- Do not soften a blocking issue into a suggestion.
- Do not invent certainty when evidence is missing.
- Do not bury the verdict after long explanation.
- Do not praise first by ritual.
- Do not ask many questions when a partial verdict is possible.

## Final Rule

The reviewer is useful only when the next decision becomes clearer.