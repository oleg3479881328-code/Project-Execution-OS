# Skills — Project Index

## Purpose

This index tracks the central reusable skill layer inside `Project-Execution-OS`.

It exists to support:

- navigation;
- lifecycle visibility;
- controlled migration from incubator repositories;
- disciplined central skill growth.

For the wider external skill universe beyond the current central registry, see:

- `docs/SKILL_UNIVERSE_INVENTORY.md`

## Current Categories

```text
skills/
  registry.md
  PROJECT_INDEX.md
  analysis/
  documentation/
  graph/
  knowledge/
  research/
  design/
  review/
  implementation/
  memory/
  orchestration/
```

## Registered Skills

| Skill | Category | Status | Review Status | Version | Path |
|---|---|---|---|---|---|
| github-repository-research | research | reviewed | approved | 0.1.1 | skills/research/github-repository-research/SKILL.md |
| pre-architecture-brainstorming | design | candidate | reviewed_with_required_improvements | 0.1.0 | skills/design/pre-architecture-brainstorming/SKILL.md |
| multi-agent-design-review | review | candidate | reviewed_with_required_improvements | 0.1.0 | skills/review/multi-agent-design-review/SKILL.md |
| decision-council-pressure-test | review | candidate | not_reviewed | 0.1.0 | skills/review/decision-council-pressure-test/SKILL.md |
| codex-execution-review | review | candidate | reviewed_with_required_improvements | 0.1.0 | skills/review/codex-execution-review/SKILL.md |
| implementation-handoff-packet | implementation | candidate | reviewed_with_required_improvements | 0.1.0 | skills/implementation/implementation-handoff-packet/SKILL.md |
| repository-memory-update | memory | reviewed | approved | 0.1.0 | skills/memory/repository-memory-update/SKILL.md |
| skill-runtime-router | orchestration | candidate | reviewed_with_required_improvements | 0.1.0 | skills/orchestration/skill-runtime-router/SKILL.md |
| workflow-state-machine | orchestration | candidate | reviewed_with_required_improvements | 0.1.0 | skills/orchestration/workflow-state-machine/SKILL.md |
| graphify | graph | reviewed | approved | 0.1.0 | skills/graph/graphify/SKILL.md |
| project-experience-memory | memory | reviewed | approved | 0.1.0 | skills/memory/project-experience-memory/SKILL.md |
| project-knowledge-sync | knowledge | reviewed | approved | 0.1.0 | skills/knowledge/project-knowledge-sync/SKILL.md |
| project-documentation-architect | documentation | reviewed | approved | 0.1.0 | skills/documentation/project-documentation-architect/SKILL.md |
| logic-deconstruction | analysis | reviewed | approved | 0.1.0 | skills/analysis/logic-deconstruction/SKILL.md |

## Current Counts

```text
active: 0
candidate: 7
reviewed: 7
draft: 0
deprecated: 0
retired: 0
```

## Current Priorities

1. Review the remaining migrated candidates that still require improvements before promotion.
2. Decide which reviewed skills are ready for real central operational use.
3. Wire reviewed `graphify` into actual project bootstrap behavior.
4. Keep governance stronger than skill-count growth.

## Forbidden Expansion Areas

Do not prioritize yet:

- runtime engines;
- autonomous orchestration;
- marketplaces;
- vector databases;
- mass skill import without review.
