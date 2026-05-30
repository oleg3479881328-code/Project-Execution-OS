# Skill Creator Existing Standards Map

## Purpose

This file points agents to the existing central standards used by the Skill Creator block.

Do not duplicate those standards inside the block.

## Required Standards

### Skill format

`docs/SKILL_SPEC.md`

Defines:

- central skill location;
- required folder structure;
- YAML frontmatter;
- required sections;
- naming rules;
- quality rules;
- what is not a central skill.

### Skill lifecycle

`docs/SKILL_LIFECYCLE.md`

Defines:

```text
draft -> candidate -> reviewed -> active -> deprecated -> retired
```

Also defines downgrade paths and state separation.

### Skill review

`docs/SKILL_REVIEW_STANDARD.md`

Defines:

- review checklist;
- failure conditions;
- approval rules;
- reviewer output.

### Existing-solution-first rule

`docs/EXISTING_SOLUTION_FIRST_STANDARD.md`

Defines the requirement to search for reusable existing solutions before creating a new one.

### General review

`docs/REVIEW_STANDARD.md`

Defines repository-wide review principles and state separation.

### Skill registry

`skills/registry.md`

Stores the registered central skill list.

## Final Rule

The Skill Creator block routes agents through existing standards.

It must not create shadow copies of central rules.