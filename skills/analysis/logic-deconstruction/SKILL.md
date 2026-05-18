---
name: logic-deconstruction
description: Analyze claims, arguments, narratives, decisions, and source material by separating facts from opinions, surfacing assumptions, testing falsifiability, checking for cognitive bias, and generating competing hypotheses.
category: analysis
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - claim_or_decision
  - source_material
outputs:
  - fact_map
  - assumptions
  - weak_points
  - competing_hypotheses
  - confidence_summary
safety_level: medium
source: migrated_from_local_codex_skills
review_status: approved
version: 0.1.0
---

# Purpose

Turn a claim, decision, or narrative into a structured analysis instead of a surface-level reaction.

# When to Use

Use this skill when:
- reasoning quality matters more than speed;
- the request involves persuasion, interpretation, or source credibility;
- a design decision needs stress-testing;
- a brainstorm needs competing hypotheses instead of one confident story.

# Workflow

1. Restate the target claim precisely.
2. Extract facts only.
3. Separate interpretations and opinions.
4. Surface hidden assumptions.
5. Test falsifiability.
6. Apply parsimony.
7. Generate competing hypotheses.

# Constraints

Do not:
- accept the framing of the input as neutral by default;
- collapse uncertainty into false certainty;
- confuse correlation with causation;
- rely on generic skepticism without tying it to evidence gaps.

# Failure Modes

Possible failures:
- overconfident single-story analysis;
- weak distinction between facts and interpretations;
- missing alternative explanations;
- performative skepticism without structure.

# Validation Checklist

Before finalizing:
- facts are separated from opinions;
- assumptions are explicit;
- weak points are tied to evidence gaps;
- alternative explanations are present;
- unknowns are stated clearly.

# References

See `references.md`.
