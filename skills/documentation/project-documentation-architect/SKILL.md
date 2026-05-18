---
name: project-documentation-architect
description: Build or normalize repository documentation from source evidence so a new engineer or AI can understand, run, and safely change the project.
category: documentation
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - repository_or_module
  - documentation_goal
outputs:
  - documentation_audit
  - confirmed_facts
  - unknowns
  - recommended_doc_set
  - drafted_or_updated_docs
safety_level: medium
source: migrated_from_local_codex_skills
review_status: approved
version: 0.1.0
---

# Purpose

Turn a repo, module, or feature into documentation that a new engineer or AI can understand, run, change, and hand off.

# When to Use

Use this skill when:
- documentation needs to be built, updated, audited, or normalized;
- a legacy project needs to be brought into the current operating model;
- a repo has contradictions between code and docs;
- onboarding or handoff quality matters.

# Workflow

1. Inspect before writing.
2. Classify the project.
3. Map the documentation set the repo actually needs.
4. Run a documentation gap analysis.
5. Draft evidence-backed docs only.
6. Report confirmed facts, unknowns, risks, and open questions explicitly.

# Constraints

Do not:
- invent architecture, commands, or deployment steps;
- trust stale docs over stronger repository evidence;
- create redundant docs without a clear need;
- hide unknowns or contradictions.

# Failure Modes

Possible failures:
- documentation based on assumptions;
- bloated doc sets;
- missing setup or deployment gaps;
- outdated README accepted as truth.

# Validation Checklist

Before finalizing:
- repo evidence was inspected first;
- confirmed facts are separated from unknowns;
- documentation recommendations match repo size and risk;
- blocking questions are explicit.

# References

See `references.md`.
