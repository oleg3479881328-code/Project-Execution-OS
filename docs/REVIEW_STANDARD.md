# Review Standard v2

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
- whether an existing solution was checked before custom work;
- whether reuse was rejected with a real reason;
- whether custom architecture was created unnecessarily;
- whether donor search continued after a sufficiently good solution was already found;
- next-step clarity.

## Acceptance Rule

Nothing important becomes stable without review.

Possible outcomes:
- accept;
- accept with warnings;
- blocked;
- reject.

## Blocking API-Model Rule

An API-based AI model integration is not acceptable if the `API Model Runtime Check` is:

- missing;
- present but not filled in;
- contradicted by the implementation evidence;
- bypassed while available provider usage or cache fields are silently ignored.

Ordinary non-model APIs such as Azure Translator do not fall under this mandatory gate unless they expose comparable AI model runtime usage or cache fields and the task is explicitly operating as an API-based AI model integration.

## Review Evidence

Review must distinguish:
- claimed state;
- committed state;
- validated state;
- reviewed state.

A commit alone is not enough.

Validation and artifact inspection still matter.

For API-based AI model integrations, review must also check:

- whether the `API Model Runtime Check` was included in the handoff and execution report;
- whether official provider documentation was checked when runtime or cache support was unknown;
- whether exposed usage, cost, cache-hit, or cache-miss fields were logged instead of silently discarded.

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
