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
  audio/
  coordination/
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
| domain-block-creation | orchestration | candidate | reviewed_with_required_improvements | 0.1.0 | skills/orchestration/domain-block-creation/SKILL.md |
| graphify | graph | reviewed | approved | 0.1.0 | skills/graph/graphify/SKILL.md |
| chatgpt-codex-github-communication | coordination | reviewed | approved | 0.1.0 | skills/coordination/chatgpt-codex-github-communication/SKILL.md |
| project-experience-memory | memory | reviewed | approved | 0.1.0 | skills/memory/project-experience-memory/SKILL.md |
| project-knowledge-sync | knowledge | reviewed | approved | 0.1.0 | skills/knowledge/project-knowledge-sync/SKILL.md |
| project-documentation-architect | documentation | reviewed | approved | 0.1.0 | skills/documentation/project-documentation-architect/SKILL.md |
| chrome-web-store-publication-readiness | documentation | candidate | not_reviewed | 0.1.0 | skills/documentation/chrome-web-store-publication-readiness/SKILL.md |
| logic-deconstruction | analysis | reviewed | approved | 0.1.0 | skills/analysis/logic-deconstruction/SKILL.md |
| gemini-tts-speech-generation | audio | candidate | not_reviewed | 0.1.0 | skills/audio/gemini-tts-speech-generation/SKILL.md |
| audio-verbatim-clip-extraction | audio | candidate | not_reviewed | unversioned | skills/audio-verbatim-clip-extraction/SKILL.md |

## Current Counts

```text
active: 0
candidate: 11
reviewed: 8
draft: 0
deprecated: 0
retired: 0
total registered: 19
```

## Current Priorities

1. Review candidate skills before promotion.
2. Use `domain-block-creation` on the next real domain-block request and review the proving run before promotion.
3. Use `chrome-web-store-publication-readiness` on Voice Button as its first proving project, while keeping it in candidate status.
4. Decide which reviewed skills are ready for real central operational use.
5. Wire reviewed `graphify` into actual project bootstrap behavior.
6. Review the two audio candidates before operational promotion.
7. Keep governance stronger than skill-count growth.

## Forbidden Expansion Areas

Do not prioritize yet:

- runtime engines;
- autonomous orchestration;
- marketplaces;
- vector databases;
- mass skill import without review.

## Maintenance Rule

Every central `skills/**/SKILL.md` should be represented in this registry unless it is explicitly documented as an incubator, deprecated artifact, or external-only compatibility copy.