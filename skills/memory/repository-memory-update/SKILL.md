---
name: repository-memory-update
description: Synchronize durable repository memory after verified execution, review, or architectural decisions.
category: memory
status: reviewed
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - verified_execution_or_review
  - repository_context
  - workflow_artifacts
outputs:
  - workflow_log_updates
  - project_or_index_updates
  - reusable_patterns
  - central_knowledge_candidates
  - locked_decisions
  - repository_memory_changes
safety_level: medium
source: migrated_from_3TestAgents
review_status: approved
version: 0.1.0
---

# Purpose

Synchronize durable repository memory after verified work is completed.

# Core Principle

Verified work must become durable repository memory.

# When to Use

Use this skill after:
- verified implementation execution;
- architecture approval;
- workflow completion;
- major review outcome;
- reusable pattern discovery;
- important governance decisions;
- migration preparation.

# Repository Memory Layers

1. `logs/WORKFLOW_LOG.md`
2. `PROJECT_INDEX.md` or relevant project state artifact
3. `knowledge-library/`
4. `skills/registry.md` when skill state changes

# Hard Rules

The memory update process must distinguish verified facts from assumptions and avoid duplicate memory noise.

# Workflow

1. Validate the verified source artifact.
2. Extract durable information.
3. Update `logs/WORKFLOW_LOG.md`.
4. Update the current-state artifact when needed.
5. Extract central knowledge candidates.
6. Synchronize locked decisions.
7. Update skill lifecycle state when relevant.

# Failure Modes

Possible failures:
- memory becomes noisy;
- duplicate memory entries;
- execution recorded before verification;
- reusable patterns lost;
- governance decisions undocumented.

# Validation Checklist

Before finalizing:
- source artifact verified;
- durable information extracted;
- workflow log updates identified;
- reusable patterns extracted;
- locked decisions synchronized;
- speculative information excluded.

# References

See `references.md`.
