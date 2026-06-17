# Review Output Format

## Default Hard Review Format

Use this format for most review requests.

```text
VERDICT: accept | accept_with_warnings | revise | blocked | reject

WHAT I REVIEWED
- Object:
- Goal:
- Intended next step:

BOTTOM LINE
- One direct sentence with the main judgment.

WHAT WORKS
- Only real strengths. Do not add filler praise.

CRITICAL / HIGH ISSUES
1. Issue:
   Why it matters:
   Required fix:

MEDIUM / LOW ISSUES
1. Issue:
   Better version:

MISSING EVIDENCE
- What is not proven yet.

REQUIRED FIXES BEFORE ACCEPTANCE
1.
2.
3.

NEXT ACTION
- continue | revise | execute | research | test | simplify | escalate | stop
```

## Micro Review Format

Use for small checks.

```text
Verdict: ...
Main problem: ...
Fix: ...
Next action: ...
```

## Red-Team Format

Use when the owner asks for the harshest inspection.

```text
VERDICT: ...

FAILURE SCENARIO
- How this can fail in real use.

WEAKEST ASSUMPTION
- The assumption most likely to be false.

HIDDEN COST
- Time, money, maintenance, complexity, or attention cost.

HANDOFF RISK
- What another executor will misunderstand.

REQUIRED CUTS
- What should be removed, simplified, or postponed.

NON-NEGOTIABLE FIX
- The one fix that must happen before proceeding.
```

## Acceptance Review Format

Use before repository promotion, customer handoff, publication, automation, or execution by another agent.

```text
VERDICT: ...

STATE SEPARATION
- Claimed state:
- Committed state:
- Validated state:
- Reviewed state:

ACCEPTANCE CHECKS
- Passed:
- Failed:
- Not checked:

BLOCKERS
- ...

APPROVAL BOUNDARY
- What may proceed:
- What may not proceed:

NEXT ACTION
- ...
```

## Tone Rule

Be direct. Do not be rude.

The owner asked for usefulness, not theater.

## Final Rule

A review output must end with a clear next action.