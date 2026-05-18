---
name: github-repository-research
description: Research a GitHub repository and extract reusable architecture and workflow patterns.
category: research
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - repository_url
  - user_goal
outputs:
  - research_summary
  - reusable_patterns
  - risks
  - recommended_next_step
safety_level: low
source: migrated_from_3TestAgents
review_status: approved
version: 0.1.1
---

# Purpose

Research a GitHub repository and extract reusable architecture, workflow, and operational patterns.

# When to Use

Use this skill when:
- analyzing open-source repositories;
- extracting reusable ideas;
- comparing workflow structures;
- reviewing AI agent systems;
- adapting strong external patterns.

# Inputs

Required inputs:
- `repository_url`
- `user_goal`

Optional inputs:
- `focus_area`
- `comparison_target`
- `depth_level`

# Outputs

Expected outputs:
- repository summary;
- evidence-backed findings;
- reusable patterns;
- pattern scoring table;
- risks;
- adaptation recommendations;
- recommended next step.

# Workflow

1. Read the repository README and visible structure.
2. Identify the project purpose.
3. Identify relevant files, folders, docs, workflows, examples, and conventions.
4. Separate confirmed facts from assumptions.
5. Extract reusable architecture or workflow patterns.
6. Score each reusable pattern.
7. Define how each pattern can be adapted without blind copying.
8. Produce a concise recommendation.

# Evidence Rules

Every major claim must include evidence.

Acceptable evidence:
- repository file path;
- README section;
- documentation file;
- config file;
- example file;
- issue, release, or commit link if relevant.

Do not claim that a repository does something unless the repository content supports it.

If evidence is missing, mark the claim as assumption.

# Pattern Scoring Model

Each reusable pattern must be scored using four fields:

| Field | Meaning | Scale |
|---|---|---|
| usefulness | How valuable this pattern is for the user's system | low / medium / high |
| portability | How easily the pattern can move into another project | low / medium / high |
| implementation_effort | How hard it is to implement | low / medium / high |
| risk | How much damage it can cause if adapted badly | low / medium / high |

# Adaptation Rules

When adapting external patterns:
- do not copy blindly;
- preserve the useful mechanism, not necessarily the exact structure;
- remove parts that do not fit the user's project;
- keep attribution in `references.md` or the final report;
- explain why the pattern fits the user's system;
- explain what must be changed before reuse.

# Constraints

Do not:
- invent repository functionality;
- claim execution without evidence;
- confuse assumptions with facts;
- recommend copying without adaptation;
- mark unreviewed patterns as proven.

# Failure Modes

Possible failures:
- shallow repository reading;
- overgeneralization;
- copying patterns blindly;
- missing repository constraints;
- treating popularity as proof of quality;
- failing to separate evidence from inference.

# Validation Checklist

Before finalizing:
- repository purpose identified;
- evidence attached to major claims;
- assumptions marked;
- reusable patterns extracted;
- patterns scored;
- adaptation recommendations included;
- risks identified;
- one recommended next step included.

# References

See `references.md`.
