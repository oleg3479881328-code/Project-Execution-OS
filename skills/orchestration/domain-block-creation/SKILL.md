---
name: domain-block-creation
description: Convert a recurring cross-project domain into a reusable Project Execution OS block using research-first, donor-first, stack-aware block construction.
category: orchestration
status: candidate_v2
target_agent: tool-neutral
review_status: upgraded_after_chrome_extension_and_design_block_validation
version: 0.2.0
---

# Domain Block Creation V2

## Core Principle

Build blocks the same way strong products are built:

Research -> Donors -> Patterns -> Ready Solutions -> Review -> Validation.

Do not start with file creation.

Start by understanding the domain.

## New Mandatory Rules

### Existing Solutions First

Before designing a block:

- search official documentation;
- search mature open-source projects;
- search donor solutions;
- search industry best practices;
- search existing Project Execution OS assets.

A block should preserve proven knowledge before inventing new structure.

### Ready Solutions Layer

If the domain includes implementation decisions, create a ready-solutions layer.

Examples:

- READY_SOLUTIONS.md
- TOOL_SELECTION_MATRIX.md
- READY_SITE_STACKS.md
- READY_SAAS_STACKS.md

The goal is reducing future architectural rework.

### Pattern Library Layer

If the domain contains repeatable structures, capture patterns.

Examples:

- landing page patterns;
- SaaS patterns;
- extension architecture patterns;
- onboarding patterns;
- review patterns.

### Monetization Layer

If the domain can generate revenue, evaluate whether the block should contain:

- monetization models;
- payment providers;
- licensing approaches;
- subscription approaches.

### Review Layer

A mature block should support both:

- creation;
- review.

A block that can only generate outputs but cannot evaluate them is incomplete.

### Research Artifact Rule

Every major block should create:

RESEARCH_REPORT_<date>.md

Purpose:

- explain why the block exists;
- preserve research conclusions;
- separate reasoning from permanent block structure.

### Validation Rule

Research is not validation.

Every non-trivial block should include:

VALIDATION_BACKLOG.md

Hypotheses, recommendations, and assumptions must be separated from verified workflows.

## Preferred Full Block Structure

blocks/<domain>/

- BLOCK.md
- READY_SOLUTIONS.md
- TOOL_SELECTION_MATRIX.md
- PATTERNS.md or pattern files
- REVIEW.md or review framework
- SECURITY_AND_COMPLIANCE.md when relevant
- MONETIZATION_AND_PAYMENTS.md when relevant
- REFERENCES.md
- VALIDATION_BACKLOG.md
- RESEARCH_REPORT_<date>.md

Add files only when justified.

## Lessons Captured

Chrome Extension Block contributed:

- ready stacks;
- monetization architecture;
- implementation-first thinking;
- validation separation.

Design Block V2 contributed:

- donor-first workflow;
- pattern libraries;
- section libraries;
- conversion-aware design;
- implementation handoff.

These are now part of the canonical block-building process.

## Final Rule

A great block is not a document collection.

A great block becomes the shortest reliable route from a future question to a high-quality decision.