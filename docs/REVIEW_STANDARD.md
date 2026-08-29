# Review Standard v4

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
- whether user-facing behavior was actually exercised when behavioral verification was possible and relevant;
- whether the final affecting change happened before the evidence being used to claim validation;
- whether unrelated files or behavior entered a bounded implementation change;
- whether a rollback path or safe checkpoint exists when the task can damage working state;
- next-step clarity;
- whether meaningful reusable knowledge was left only in chat or transient execution state;
- whether a new standard, runbook, knowledge entry, ADR, checklist, or skill was created when an existing canonical artifact should have been updated instead;
- whether one-off behavior was prematurely promoted into a mandatory standard.

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

## Verification Invalidation Rule

A validation result applies only to the version and behavior actually checked.

```text
If a later change could affect previously validated behavior, that validation is stale until the relevant checks pass again.
```

During review, compare evidence timing with the final affecting change. Do not accept an earlier successful test, browser pass, screenshot, or deployment check as proof for a later modified state.

For user-facing changes, machine checks alone are not sufficient when the actual behavior can reasonably be exercised. Use the behavioral verification guidance in `docs/HARNESS_ENGINEERING_STANDARD.md`.

## Bounded Change Review

For non-trivial implementation work, review the actual changed surface against the task boundary.

Prefer evidence that makes these questions answerable:

```text
What was supposed to change?
What was explicitly not supposed to change?
What actually changed?
How was the final state verified?
How can it be rolled back?
```

Undefined “improvements” outside the accepted contract are scope drift, even when they appear beneficial. Record them as separate candidate work unless they are necessary to satisfy the current contract.

## Micro-Task Mode

If the task is truly small and can reasonably be completed in one short pass, use a minimal review shape:

```text
goal -> action -> result -> short review note -> next action
```

Do not force a heavyweight review ritual for micro-tasks.

## Post-Review Promotion Gate

At the end of a meaningful review, run the promotion gate from `docs/KNOWLEDGE_SYSTEM.md`.

The review should answer:

```text
Did this work create a durable fact, decision, verified fix,
repeatable procedure, reusable pattern, mandatory rule,
or reusable capability that future work should not rediscover?
```

If no, stop without creating documentation ceremony.

If yes:

1. classify the result;
2. update the narrowest correct existing canonical artifact first;
3. create a new artifact only when no existing artifact owns the responsibility;
4. do not promote a one-off result into a standard merely because it was useful;
5. leave the project transfer-ready after the promotion.

Typical routing:

- state / blocker / next action -> project state or current log;
- decision -> project decision / ADR-style record;
- verified failure + fix -> verified technical solution / known-fix entry / runbook;
- repeatable procedure -> SOP / checklist / runbook / playbook;
- reusable cross-project lesson -> central knowledge candidate, then review;
- mandatory cross-task rule -> existing standard, or a new standard only when necessary;
- reusable executable behavior -> skill / capability path.

## Logging Rule

Every review should leave one concrete next action:
- continue;
- revise;
- execute;
- extract knowledge;
- stop.
