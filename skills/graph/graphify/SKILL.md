---
name: graphify
description: Build and use a persistent knowledge graph for a repository or document corpus to support broad navigation, architecture understanding, and repeated follow-up work.
category: graph
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - project_path
  - graph_goal
outputs:
  - graph_report
  - graph_json
  - graph_navigation_findings
  - graph_refresh_status
safety_level: medium
source: migrated_from_local_agents_skills
review_status: approved
version: 0.1.0
---

# Purpose

Turn a folder of files into a navigable knowledge graph with a persistent repository-memory layer.

# When to Use

Use this skill when:
- broad repository or corpus understanding is needed;
- cross-file relationships matter;
- the relevant files are unknown or too many to read directly;
- the project will likely receive repeated follow-up questions;
- a legacy project needs structural orientation before normalization.

# Core Outputs

Standard outputs:
- `graphify-out/GRAPH_REPORT.md`
- `graphify-out/graph.json`

# Workflow

1. Estimate scope cheaply first.
2. Skip Graphify for narrow tasks that fit direct context.
3. Initialize Graphify for broad repositories or document corpora.
4. Read `graphify-out/GRAPH_REPORT.md` before broad raw-file exploration.
5. Refresh Graphify after structural changes when feasible.

# Constraints

Do not:
- force Graphify on small known-file tasks;
- present graph outputs as source-of-truth architecture;
- pretend the graph is current if it has not been refreshed;
- transliterate non-ASCII source text.

# Failure Modes

Possible failures:
- unnecessary Graphify use on small tasks;
- stale graph trusted as current truth;
- graph memory confused with repository source of truth;
- missing refresh after major structural changes.

# Validation Checklist

Before finalizing:
- Graphify use was justified by context cost;
- graph outputs are present or their absence is reported honestly;
- graph findings are treated as navigation aids, not blind truth;
- refresh needs are stated when relevant.

# References

See `references.md`.
