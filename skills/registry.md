# Central Skill Registry

## Purpose

This registry tracks all central reusable skills inside `Project-Execution-OS`.

The registry exists to prevent:

- duplicate skills;
- unclear lifecycle state;
- lost migration artifacts;
- uncontrolled skill growth;
- fake activation claims.

## Registry Rules

Every central skill must:

- appear in this registry;
- have a unique name;
- define category;
- define lifecycle status;
- define review status;
- define compatibility;
- define source attribution.

A skill that is not in this registry is not part of the central active system.

## Lifecycle States

Allowed statuses:

- draft
- candidate
- reviewed
- active
- deprecated
- retired

## Review States

Allowed review states:

- not_reviewed
- reviewed_with_required_improvements
- approved
- rejected

## Registered Skills

| Skill Name | Category | Status | Review Status | Compatibility | Version | Source | Path |
|---|---|---|---|---|---|---|---|
| github-repository-research | research | reviewed | approved | chatgpt, codex, claude | 0.1.1 | migrated_from_3TestAgents | skills/research/github-repository-research/SKILL.md |
| pre-architecture-brainstorming | design | candidate | reviewed_with_required_improvements | chatgpt, codex, claude | 0.1.0 | migrated_from_3TestAgents | skills/design/pre-architecture-brainstorming/SKILL.md |
| multi-agent-design-review | review | candidate | reviewed_with_required_improvements | chatgpt, codex, claude | 0.1.0 | migrated_from_3TestAgents | skills/review/multi-agent-design-review/SKILL.md |
| decision-council-pressure-test | review | candidate | not_reviewed | chatgpt, codex, claude | 0.1.0 | adapted_from_tenfoldmarc_llm_council_skill | skills/review/decision-council-pressure-test/SKILL.md |
| codex-execution-review | review | candidate | reviewed_with_required_improvements | codex, chatgpt, claude | 0.1.0 | migrated_from_3TestAgents | skills/review/codex-execution-review/SKILL.md |
| implementation-handoff-packet | implementation | candidate | reviewed_with_required_improvements | codex, chatgpt, claude | 0.1.0 | migrated_from_3TestAgents | skills/implementation/implementation-handoff-packet/SKILL.md |
| repository-memory-update | memory | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_3TestAgents | skills/memory/repository-memory-update/SKILL.md |
| skill-runtime-router | orchestration | candidate | reviewed_with_required_improvements | chatgpt, codex, claude | 0.1.0 | migrated_from_3TestAgents | skills/orchestration/skill-runtime-router/SKILL.md |
| workflow-state-machine | orchestration | candidate | reviewed_with_required_improvements | chatgpt, codex, claude | 0.1.0 | migrated_from_3TestAgents | skills/orchestration/workflow-state-machine/SKILL.md |
| graphify | graph | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_local_agents_skills | skills/graph/graphify/SKILL.md |
| project-experience-memory | memory | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_local_codex_skills | skills/memory/project-experience-memory/SKILL.md |
| project-knowledge-sync | knowledge | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_local_codex_skills | skills/knowledge/project-knowledge-sync/SKILL.md |
| project-documentation-architect | documentation | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_local_codex_skills | skills/documentation/project-documentation-architect/SKILL.md |
| chrome-web-store-publication-readiness | documentation | candidate | not_reviewed | chatgpt, codex, claude | 0.1.0 | extracted_from_Voice-Button_issue_2 | skills/documentation/chrome-web-store-publication-readiness/SKILL.md |
| logic-deconstruction | analysis | reviewed | approved | chatgpt, codex, claude | 0.1.0 | migrated_from_local_codex_skills | skills/analysis/logic-deconstruction/SKILL.md |

## Governance Notes

- Migrated skills keep their central lifecycle state only after explicit review inside `Project-Execution-OS`.
- No migrated skill should be treated as `active` based only on its incubator history.
- Project-specific agents must not be added to this central registry.