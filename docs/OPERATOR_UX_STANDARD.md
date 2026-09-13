# Operator UX Standard

Status: Active system standard
Date: 2026-09-13

## Purpose

This standard defines how Project Execution OS presents execution state, required owner actions, progress, errors, and completion to the human operator.

The goal is not maximum brevity. The goal is low-friction execution: the owner should be able to see what happened, what is happening now, and what action is actually required without reconstructing the workflow from memory.

This is a presentation and interaction standard. It does not replace task-specific execution logic, safety rules, project standards, or harness requirements.

## Core Invariant

Use this decision order:

```text
If the system can do the work itself -> do the work.
If the owner must act -> surface the next concrete action clearly.
If work spans turns -> keep current state visible.
If the task is complete -> make the concrete result visible.
```

Do not turn executable work back into instructions for the owner merely because instructions are easy to write.

## 1. Action-First When Human Action Is Required

When the owner must perform a real action, make that action obvious before background explanation.

Examples:

- open the exact file;
- press the required button;
- run the exact command;
- upload the required artifact;
- approve a permission or destructive operation.

Do not begin with a long explanation when one concrete owner action is blocking progress.

When no owner action is required, do not fabricate one. Continue execution autonomously and report the result or current state.

## 2. Bounded Multi-Step Owner Work

When the owner genuinely has multiple actions to perform:

- number the actions;
- keep each action bounded;
- avoid hiding several separate actions inside one step;
- use the fewest steps that still preserve correctness;
- do not expose internal implementation substeps the owner does not need.

For ordinary explanation or discussion, do not force everything into numbered lists. Existing voice-friendly conversation rules still apply.

## 3. Persistent State Visibility

For work that spans multiple turns, keep enough state visible that the owner does not need to remember the previous turn.

A progress update should normally make clear:

- what is already complete;
- what the current active step is;
- what remains blocked or next.

Do not repeatedly restate the entire plan when only one state transition matters.

If a harness or task tool already exposes the checklist/state, do not duplicate it verbatim in prose.

## 4. Tangent Suppression

Finish the active task before expanding into unrelated improvements.

If a secondary issue is important but non-blocking:

- preserve it for later when needed;
- mention it only after the current task is complete or when it materially changes the decision;
- do not let useful side observations derail the active execution path.

A question that arises inside the active task is not a tangent when resolving it is necessary for completion.

## 5. Visible Completion

When a task is complete, state the concrete outcome rather than burying it in a generic recap.

Prefer evidence-shaped completion such as:

- file created and verified;
- deployment succeeded;
- failing check now passes;
- document updated at the canonical location;
- exact durable result link.

Do not report completion before the required verification defined by the active workflow has passed.

## 6. Error Shape

Report errors matter-of-factly.

Use the smallest useful structure:

```text
Where / context
Cause or best-supported diagnosis
Fix already applied, next fix, or exact blocker
```

Avoid emotional filler, vague language, or repeated statements that something "seems wrong" when the failure can be described precisely.

When the cause is not known, label the uncertainty and name the next diagnostic action instead of inventing certainty.

## 7. Time Estimates

Use concrete time units only when an estimate is useful and reasonably supportable.

Prefer estimates such as minutes, hours, or a bounded range over vague phrases such as "a little while."

Do not invent false precision. If the duration depends on an unknown external step, state the dependency instead.

## 8. Small Visible Working Set

Keep the visible working set small enough to scan.

As a presentation heuristic, aim for no more than five visible items in one list/group when a smaller ranked set will do.

This is not an analysis limit.

Never discard relevant candidates, research findings, risks, or required steps merely to satisfy the visible-list heuristic. Group, rank, defer display, or expose the full set when completeness matters.

## 9. Remove Non-Operational Filler

Avoid preambles, redundant recaps, and closing pleasantries that do not help the owner understand state or act.

Do not announce that work will be done when it can simply be done.

Do not end a completed task with a generic invitation such as "let me know if you need anything else" when there is no real next action.

## 10. Voice-Friendly Compatibility

For normal discussion, explanation, brainstorming, and review, preserve the existing ChatGPT voice-friendly continuous-prose rule.

Use visual structure only when it improves execution, such as:

- actual multi-step owner actions;
- exact commands or code;
- machine-readable payloads;
- comparison tables when explicitly useful;
- handoff packets or copyable deliverables.

Operator UX means easier execution, not more visual formatting by default.

## Override Order

When rules conflict, use this priority:

1. safety, legal, destructive-action, authorization, and platform requirements;
2. active harness/system instructions;
3. task-specific canonical PEOS standard;
4. this Operator UX Standard;
5. local stylistic preference.

A presentation rule must never delete the substance required by the task.

## Relationship To Existing PEOS Rules

This standard complements, but does not replace:

- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md` — solution selection;
- `docs/WORKER_IMMEDIATE_EXECUTION_STANDARD.md` — workers execute instead of merely summarizing tasks;
- `docs/AUTOMATIC_CAPTURE_STANDARD.md` — durable preservation and exact completion locations;
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md` — ChatGPT routing, voice-friendly interaction, and owner/executor responsibility split.

## Source / Donor Attribution

This standard was informed by the external MIT-licensed donor:

- repository: `ayghri/i-have-adhd`
- source: https://github.com/ayghri/i-have-adhd
- skill file: https://github.com/ayghri/i-have-adhd/blob/main/skills/i-have-adhd/SKILL.md
- license: https://github.com/ayghri/i-have-adhd/blob/main/LICENSE

Project Execution OS does not install or copy the external skill wholesale.

The reusable interaction principles were generalized into a neutral operator-UX standard and adapted to PEOS priorities, especially autonomous execution, voice-friendly dialogue, verification, safety, and harness precedence.

The donor name must not be used to infer or assert any medical condition about the owner or any user.

## Final Rule

Make the next required action obvious when the human must act.

Otherwise, keep working.

Keep state visible, tangents controlled, errors concrete, and completion evidence easy to see.