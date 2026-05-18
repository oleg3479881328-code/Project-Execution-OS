---
name: project-experience-memory
description: Build and use lightweight project memory in a repository so future sessions do not repeat mistakes or re-derive stable context.
category: memory
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - repository_context
  - current_task
outputs:
  - project_memory_structure
  - current_state_notes
  - decisions
  - pitfalls
  - checkpoints
safety_level: medium
source: migrated_from_local_codex_skills
review_status: approved
version: 0.1.0
---

# Purpose

Make project knowledge durable across sessions and tasks.

# When to Use

Use this skill when:
- a repository has weak or missing durable project memory;
- multiple future sessions or agents may touch the same project;
- architecture, regressions, or validated behavior should not be rediscovered repeatedly;
- a legacy project needs normalization into the current operating model.

# Default Layout

Use repo-local project memory when no equivalent system already exists:

```text
skills/project-memory/
  SKILL.md
  references/
    current-state.md
    decisions.md
    fixes.md
    pitfalls.md
    checkpoints.md
    skill-candidates.md
    review-log.md
```

# Workflow

1. Read project instructions first.
2. Reuse existing durable memory if the repo already has a healthy equivalent.
3. Read only the memory files relevant to the task.
4. Read the repository itself.
5. Record only durable, reusable, evidence-backed project knowledge.
6. Update memory after meaningful validated work.

# Constraints

Do not:
- duplicate healthy existing memory systems;
- store chat transcripts as project memory;
- overwrite validated notes with guesses;
- promote every useful note into a central skill.

# Failure Modes

Possible failures:
- noisy memory;
- duplicated memory layers;
- speculative notes treated as facts;
- missing fragile-zone documentation.

# Validation Checklist

Before finalizing:
- the repo actually needs added or updated project memory;
- only durable information was recorded;
- notes are evidence-backed;
- current-state and fragile areas are explicit.

# References

See `references.md`.
