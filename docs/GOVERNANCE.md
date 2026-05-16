# Governance — Project Execution OS

## 1. Purpose

Governance exists to prevent:

- architectural drift;
- fake execution claims;
- premature runtime building;
- document chaos;
- uncontrolled agent growth;
- uncontrolled skill growth;
- loss of project state;
- weak knowledge promotion.

## 2. Source of Truth

The GitHub repository is the source of truth.

A project state is valid only if represented by a repository artifact.

Chat messages, generated drafts, verbal decisions, and uncommitted ideas are not final project state.

## 3. State Levels

### generated

Proposed by a user, assistant, or agent but not committed.

### committed

Written to repository with confirmed commit evidence.

### reviewed

Checked through review process.

### active

Approved for reuse after review.

Committed does not mean active.
Reviewed does not automatically mean active.

## 4. No Fake Execution Rule

No human, assistant, or agent may claim that something was:

- executed;
- saved;
- applied;
- committed;
- tested;
- reviewed;
- approved;
- activated;
- deployed;
- completed;

unless there is evidence.

Acceptable evidence:

- repository commit;
- user-provided execution result;
- reviewed artifact;
- log entry;
- explicit external system output.

## 5. Project Boundary Rule

Each project must live under:

`projects/<project-id>/`

Project-specific artifacts must not be mixed with central operating system artifacts.

## 6. Agent Governance

Agents are task-specific modules.

Agents must be created only when needed.

Forbidden:

- creating agents before project scope exists;
- creating agents as decoration;
- using agents to bypass workflow stages;
- allowing agents to claim execution without evidence;
- letting agent outputs become active without review.

## 7. Knowledge Governance

Each project has local knowledge:

`projects/<project-id>/project-library/`

The operating system has central knowledge:

`knowledge-library/`

Local knowledge may be promoted to central knowledge only if:

1. it is extracted in `08_KNOWLEDGE_EXTRACT.md`;
2. it has reusable value beyond one project;
3. it is reviewed;
4. it is stored as a clear central library artifact.

## 8. Reuse-First Rule

Before designing from scratch, the relevant stage must search for:

- existing open-source patterns;
- official documentation;
- known workflows;
- reusable templates;
- prior project artifacts;
- central knowledge-library entries;
- local project-library entries.

Reuse does not mean blind copying.

Reusable ideas must be adapted, attributed when needed, and reviewed before becoming active.

## 9. Anti-Overbuilding Rule

Do not build infrastructure before the workflow proves it needs infrastructure.

Correct sequence:

```text
manual workflow
→ review
→ repeatable project templates
→ task-specific agents
→ knowledge promotion
→ adapters
→ automation only if justified
```

Wrong sequence:

```text
runtime
→ dashboard
→ database
→ automation
→ unclear workflow
```

## 10. Review Requirement

Artifacts that affect future behavior require review before active status.

Review-required artifacts:

- workflow contracts;
- governance rules;
- project templates;
- agent definitions;
- knowledge entries;
- execution specifications for important projects;
- central library patterns;
- lifecycle rules.

## 11. Logging Requirement

Every important repository change or workflow milestone must be logged.

A valid log entry should include:

- date or workflow reference;
- action taken;
- affected files;
- purpose;
- resulting state;
- risks or lessons;
- next action.

## 12. Current Foundation Status

Status:

`foundation_candidate`

This governance is committed project state after creation, but it requires future review before becoming active governance.
