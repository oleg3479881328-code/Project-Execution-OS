# Skill Creator Block

## Purpose

This block gives `Project Execution OS` one reusable workflow for creating, reviewing, registering, and maintaining central skills.

It does not replace the central skill standards. It routes agents through them in the correct order.

## Status

`candidate`

## When To Use

Use this block when the owner or an agent asks to:

- create a new reusable skill;
- check whether a proposed skill already exists;
- convert a repeated workflow into a skill;
- migrate an external skill into the central system;
- review a draft skill before activation;
- update, deprecate, or retire an existing skill.

## When Not To Use

Do not use this block for:

- one-off instructions that do not deserve reuse;
- project-only prompts with no cross-project value;
- broad agent personas;
- random notes or references;
- creating a skill before checking whether an existing solution already covers the need.

## Core Rule

Do not create a new skill by reflex.

First check whether the need is real, recurring, narrow enough, and not already covered by an existing skill, block, standard, or external reusable solution.

## Workflow

```text
1. Capture the requested capability.
2. Define the exact recurring task.
3. Check for duplicates in skills/, blocks/, docs/, and relevant external references.
4. Decide whether the result should be a skill, block, standard, project artifact, or no new artifact.
5. If a skill is justified, generate a draft from the template.
6. Run the creation checklist.
7. Apply skill review rules.
8. Record lifecycle state.
9. Register the skill only after the artifact exists.
10. Activate only after review passes.
```

## Artifact Classification Rule

Use:

- `skill` for one narrow reusable workflow;
- `block` for a broader reusable domain layer containing multiple assets or skills;
- `standard` for a mandatory system rule;
- `project artifact` for a project-specific file;
- `reference` for material that should be preserved but is not yet accepted.

## Required Inputs

Typical inputs:

- requested capability;
- intended users or agents;
- recurring task boundary;
- expected inputs;
- expected outputs;
- known references or donor solutions;
- compatibility requirements;
- risks and validation method.

## Outputs

Typical outputs:

- draft `SKILL.md`;
- supporting `references.md`;
- review findings;
- lifecycle recommendation;
- registry update after creation;
- explicit decision not to create a skill when another artifact type is better.

## Depends On

This block depends on:

- `docs/SKILL_SPEC.md`
- `docs/SKILL_LIFECYCLE.md`
- `docs/SKILL_REVIEW_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `docs/REVIEW_STANDARD.md`
- `skills/registry.md`

## MVP Files

```text
blocks/skill-creator/
  BLOCK.md
  templates/SKILL_TEMPLATE.md
  checklists/SKILL_CREATION_CHECKLIST.md
  references/EXISTING_STANDARDS.md
```

## Boundary

This block does not automatically approve or activate skills.

Generated, committed, reviewed, and active are different states.

## Final Rule

Create the smallest reusable skill that solves one recurring task.

Do not create duplicates, giant catch-all prompts, or fake active skills.