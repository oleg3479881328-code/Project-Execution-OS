---
name: multi-agent-design-review
description: Review a proposed design or pre-architecture specification through multiple specialist review lenses before implementation handoff.
category: review
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - design_or_pre_architecture_specification
  - user_goal
outputs:
  - review_summary
  - specialist_reviews
  - contradictions
  - risks
  - reusable_patterns
  - required_changes
  - final_recommendation
safety_level: low
source: migrated_from_3TestAgents
review_status: reviewed_with_required_improvements
version: 0.1.0
---

# Purpose

Review a proposed design or pre-architecture specification before it is handed to an Architect Agent, Coder-Spec Agent, Codex, or any implementation workflow.

# When to Use

Use this skill after:
- `pre-architecture-brainstorming` has produced a draft specification;
- an Architect Agent has produced a design;
- a workflow is about to move toward implementation;
- a design affects repository governance, skill lifecycle, agent behavior, or system architecture.

# Operating Mode

The agent runs a structured review using multiple review lenses.

Each lens reviews the same artifact from a different responsibility boundary.

# Review Lenses

1. Architect Lens
2. Reviewer Lens
3. Research Lens
4. Librarian Lens
5. MVP Lens

# Workflow

1. Validate the input artifact.
2. Check central and project context when relevant.
3. Run each review lens separately.
4. Scan contradictions.
5. Build a risk register.
6. Separate required changes from optional improvements.
7. Return one final recommendation.

# Constraints

Do not:
- produce implementation code;
- rewrite the whole design unless explicitly requested;
- create new scope as a hidden requirement;
- mark speculative findings as confirmed;
- approve a handoff with unresolved blockers.

# Failure Modes

Possible failures:
- reviewing too generally;
- missing governance violations;
- approving vague specs;
- blocking MVP due to unnecessary perfectionism;
- failing to identify reusable knowledge.

# Validation Checklist

Before finalizing:
- all five lenses were applied;
- blockers were explicit;
- optional improvements were separated;
- MVP boundary was protected;
- final recommendation is clear.

# References

See `references.md`.
