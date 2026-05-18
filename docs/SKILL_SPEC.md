# Skill Specification Standard v1

## Purpose

This standard defines the canonical format for central reusable skills inside `Project-Execution-OS`.

Skills are reusable operating units for humans and AI agents.

They are not the root system.

The workflow and governance remain the root system.

## Definition

A skill is a focused reusable workflow stored as a folder with a primary `SKILL.md` file and supporting references.

A skill must define:

- when to use it;
- when not to use it;
- required inputs;
- expected outputs;
- workflow or review logic;
- constraints;
- failure modes;
- validation rules;
- compatibility boundaries.

## Central Skill Location

Central reusable skills live under:

`skills/<category>/<skill-name>/`

Project-specific agents do not belong here.

Project-specific agents belong under:

`projects/<project-id>/agents/`

## Required Skill Structure

```text
skills/<category>/<skill-name>/
  SKILL.md
  references.md
```

Optional files:

```text
validation/REVIEW.md
examples/
assets/
scripts/
```

## Required Metadata

Every `SKILL.md` must begin with YAML frontmatter.

Minimum fields:

```yaml
---
name: example-skill-name
description: Short description of what the skill does.
category: research
status: draft
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - input_name
outputs:
  - output_name
safety_level: low
source: internal
review_status: not_reviewed
version: 0.1.0
---
```

## Required Sections

Every skill must include:

1. Purpose
2. When to Use
3. Inputs or Required Inputs
4. Outputs
5. Workflow or Review Logic
6. Constraints
7. Failure Modes
8. Validation Checklist
9. References

## Naming Rules

Skill names must:

- use lowercase;
- use hyphen-separated words;
- describe one task clearly;
- avoid vague names such as `helper`, `general`, or `super-agent`.

## Quality Rules

A central skill must:

- have a narrow task boundary;
- fit the central workflow and governance model;
- avoid fake execution claims;
- preserve evidence rules;
- stay tool-neutral unless intentionally adapter-specific;
- define review state explicitly;
- avoid project-only assumptions.

## What Is Not a Central Skill

Not a central skill:

- a random prompt;
- a project-only instruction file;
- a one-off chat answer;
- an undocumented persona;
- a broad catch-all assistant blob.

## Migration Rule

Skills migrated from experimental repositories must enter `Project-Execution-OS` as `candidate` unless they have been explicitly re-reviewed here.
