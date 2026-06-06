# Agent Creation Standard v1

## 1. Purpose

This standard defines how Project Execution OS creates task-specific agents inside projects.

Agents exist to improve execution quality for a specific project need.

Agents are not the root system.
The workflow is the root system.

## 2. When To Create An Agent

Create an agent only when at least one condition is true:

- a workflow stage needs repeated specialized judgment;
- a domain requires expert handling;
- quality improves with a dedicated role;
- the same task will recur inside the project;
- separating the role reduces confusion or hallucination drift.

Do not create agents for simple one-off tasks.

## 3. Agent Location

Project-specific agents live here:

`projects/<project-id>/agents/<agent-name>/AGENT.md`

Optional supporting files:

```text
README.md
examples.md
validation/REVIEW.md
references.md
```

## 4. Required Agent Contract

Every agent must define:

```text
name:
purpose:
project_scope:
when_to_use:
when_not_to_use:
inputs:
outputs:
workflow_stage:
constraints:
evidence_rules:
failure_modes:
review_requirements:
state:
version:
```

## 4A. Required Entry Inheritance

Every project-related agent must inherit the repository entry protocol instead of inventing its own:

1. enter through `START_HERE.md`;
2. follow `docs/ROUTER.md`;
3. inspect useful curated indexes and generated indexes before broad scanning;
4. use semantic retrieval when wording is uncertain, the repository is large, or the right files are not obvious;
5. open canonical files for selected hits before relying on them;
6. load only the minimum sufficient evidence.

If an agent works in a repository that exposes a local index-first standard, the agent should reference that standard briefly instead of duplicating detailed search workflow in every agent file.

## 5. Agent Lifecycle States

Allowed states:

- draft;
- candidate;
- reviewed_with_required_improvements;
- reviewed_passed;
- active;
- deprecated;
- rejected.

No agent starts as active.

## 6. Agent Output Rule

Every agent output must be stored as a project artifact if it affects the project.

Examples:

- brief;
- research report;
- plan;
- architecture decision;
- execution spec;
- review report;
- knowledge extraction.

## 7. Evidence Rule

Agents must separate:

- confirmed facts;
- assumptions;
- recommendations;
- open questions.

If an agent relies on repository content, it must cite or name the file path.

If an agent relies on web research, it must preserve source links in the artifact.

If an agent relies on index hits or semantic retrieval, it must still name the canonical files that were opened and used as evidence.

## 8. No Fake Execution Rule

Agents must not claim:

- saved;
- committed;
- tested;
- deployed;
- reviewed;
- active;
- completed;

unless there is evidence.

## 9. Standard Agent Types

Common project agents may include:

- Pre-Architect;
- Research Agent;
- Architect;
- Coder-Spec Agent;
- Reviewer;
- Librarian;
- OSINT Agent;
- Market Research Agent;
- UX Reviewer;
- Documentation Agent;
- QA Agent.

These are optional templates, not mandatory agents.

## 10. Agent Creation Workflow

Agent creation must happen through `04_AGENT_DESIGN.md` in a project workflow run.

That file must answer:

1. Is an agent needed?
2. Which stage requires it?
3. What exact problem does it solve?
4. What artifact will it produce?
5. How will it be reviewed?

## 11. Activation Rule

An agent becomes active only after:

1. its `AGENT.md` exists;
2. it is used in at least one workflow run or reviewed against expected use;
3. review passes;
4. status is explicitly changed to `active`;
5. the change is logged.
