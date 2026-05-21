# Micro-Task Mode

## Purpose

Use micro-task mode when the work is small, safe, and can reasonably be completed in one short pass, typically without needing a full workflow run.

Examples:
- short wording fixes;
- tiny documentation edits;
- one bounded clarification bundle;
- a narrow repo check;
- a small non-risky reasoning task.

## Rule

Do not force a full workflow for micro-tasks.

Use the smallest durable artifact that still preserves useful state.

## Minimal Shape

```text
goal -> action -> result -> short review note -> next action
```

## Artifact Rule

Create an artifact only when it will be useful later.

Useful means at least one of:
- the result affects future project work;
- the result will likely need review;
- the result will be reused;
- the result explains a decision;
- the result is needed as evidence.

If none of these are true, do not manufacture extra files just to satisfy ritual.

## Codex Rule

Do not hand micro-tasks to Codex unless executor access is actually required.
