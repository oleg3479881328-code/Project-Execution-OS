---
name: project-knowledge-sync
description: Synchronize project documentation with the central knowledge library and record exact proof of what was documented.
category: knowledge
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - implemented_or_reviewed_change
  - project_docs
  - reusable_knowledge_candidate
outputs:
  - local_doc_updates
  - knowledge_routing_decision
  - central_library_entry
  - documentation_proof
safety_level: medium
source: migrated_from_local_codex_skills
review_status: approved
version: 0.1.0
---

# Purpose

Keep project documentation and the central knowledge library in sync.

# When to Use

Use this skill when:
- implementation or review produced durable knowledge;
- a decision or troubleshooting lesson must be recorded;
- reusable project knowledge may belong in the central library;
- proof of documentation work matters.

# Workflow

1. Search the central library before implementation or direction change.
2. Update local project docs first.
3. Record decisions and troubleshooting explicitly.
4. Evaluate whether the knowledge is reusable beyond one project.
5. If reusable, add it to the central library using the correct record type.
6. Report proof, not vague claims.

# Constraints

Do not:
- treat chat-only decisions as documentation;
- skip local docs when reusable knowledge also exists;
- add project-specific noise to the central library;
- mark documentation complete without proof.

# Failure Modes

Possible failures:
- reusable knowledge lost;
- local context not documented;
- central library polluted with project noise;
- proof missing.

# Validation Checklist

Before finalizing:
- local docs were considered first;
- reusability was evaluated;
- central-library routing is explicit;
- proof of documentation changes is included.

# References

See `references.md`.
