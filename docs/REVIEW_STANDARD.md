# Review Standard v1

## Purpose

This standard defines how Project Execution OS reviews decisions, plans, execution artifacts, and results before stable acceptance.

## Review Scope

Review should check:
- contradictions;
- missing evidence;
- scope drift;
- risky assumptions;
- acceptance-criteria gaps;
- unvalidated claims;
- next-step clarity.

## Acceptance Rule

Nothing important becomes stable without review.

Possible outcomes:
- accept;
- accept with warnings;
- blocked;
- reject.

## Review Evidence

Review must distinguish:
- claimed state;
- committed state;
- validated state;
- reviewed state.

A commit alone is not enough.

Validation and artifact inspection still matter.

## Micro-Task Mode

If the task is truly small and can reasonably be completed in one short pass, use a minimal review shape:

```text
goal -> action -> result -> short review note -> next action
```

Do not force a heavyweight review ritual for micro-tasks.

## Logging Rule

Every review should leave one concrete next action:
- continue;
- revise;
- execute;
- extract knowledge;
- stop.
