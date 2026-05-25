# Agent Module Format Standard v0.1

## Status

`candidate / bounded / not yet runtime-enforced`

## Purpose

This standard defines the smallest portable file-based format for reusable AI capability modules inside the Project Execution OS ecosystem.

It exists to support:

- Project Execution OS operating modules;
- reusable skill-library entries;
- Codex handoff-oriented capability packs;
- future Agent Network OS adoption where justified by tested need;
- Central Knowledge Library (CKL) patterns that must be easy for another AI or human to inspect and reuse.

This document does **not** create a new runtime, registry service, marketplace, router, plugin engine, backend layer, or execution framework.

## Source Pattern and Adaptation Rule

Primary reference:

- Anthropic `knowledge-work-plugins`: https://github.com/anthropics/knowledge-work-plugins

Observed Anthropic pattern:

```text
plugin-name/
├── .claude-plugin/plugin.json   # manifest
├── .mcp.json                    # connector/tool configuration
├── commands/                    # explicit user-invoked workflows
└── skills/                      # background expertise used when relevant
```

The central insight to adopt is **separation of concerns** (разделение обязанностей):

- a manifest identifies a module;
- connector configuration states what external capability the module can use;
- skills provide reusable expertise and bounded procedures;
- commands provide explicit actions/workflows;
- everything is inspectable as files rather than hidden in chat context.

Adaptation rule:

- adapt the architecture and operating discipline;
- do not blindly copy Anthropic wording, tool assumptions, product-specific behavior, or role packages;
- promote only patterns that are useful for Oleg's existing projects and validated workflows.

## Hard Constraint: No Architecture Expansion Loop

Project Execution OS is currently oriented toward MVP hardening and reuse-first delivery.

Therefore this standard is intentionally minimal:

- no new database;
- no new UI;
- no vector retrieval layer;
- no autonomous module router;
- no marketplace implementation;
- no requirement to convert existing working documents immediately;
- no Agent Network OS runtime change until a real module use case proves the need.

## Core Definitions

### Agent Module

An **agent module** is a portable folder containing instructions and optional configuration that gives an AI a bounded reusable capability.

Русское определение: **agent module** — переносимая папка с инструкциями и необязательной конфигурацией, которая даёт ИИ ограниченную повторно используемую способность.

### Skill

A **skill** is a file-based package of domain expertise, trigger conditions, constraints, and workflow guidance that an AI can apply when the current task matches its purpose.

Русское определение: **skill** — файловый пакет экспертных знаний, условий применения, ограничений и рабочего процесса, который ИИ использует, когда текущая задача соответствует назначению навыка.

### Command

A **command** is an explicit named workflow invoked for a known action or deliverable.

Русское определение: **command** — явно названный рабочий процесс, который запускается для известного действия или результата.

### Connector Map

A **connector map** is declarative information about external systems or tools that a module may need, without embedding credentials or implementation logic.

Русское определение: **connector map** — декларативное описание внешних систем или инструментов, которые могут понадобиться модулю, без хранения секретов и без встраивания исполняемой логики.

## Canonical Minimal Directory Shape

Use this shape only when a reusable capability genuinely needs both background expertise and explicit invocation. A single simple reusable pattern may remain only a CKL Markdown entry.

```text
agent-modules/<module-name>/
├── module.json                  # required manifest
├── README.md                    # required human/AI entrypoint
├── skills/                      # optional background expertise
│   └── <skill-name>/
│       └── SKILL.md
├── commands/                    # optional explicit workflows
│   └── <command-name>.md
├── connectors.json              # optional external tool declarations
├── references/                  # optional evidence and donor-source notes
│   └── sources.md
├── examples/                    # optional examples/test cases
│   └── example.md
└── handoff-contracts/           # optional Codex execution packet contracts
    └── <contract-name>.md
```

## What Belongs Where

| Artifact | Role | Required? | Must Not Contain |
| --- | --- | --- | --- |
| `module.json` | module identity, scope, lifecycle state | yes | secrets, large instructions, execution claims |
| `README.md` | front door and usage boundary | yes | duplicated full skill text |
| `skills/*/SKILL.md` | reusable expertise and bounded procedures | optional | hidden execution state, fabricated connectors |
| `commands/*.md` | explicit action workflow | optional | generic background knowledge dump |
| `connectors.json` | declared external-tool dependencies | optional | tokens, credentials, guessed access |
| `references/sources.md` | donor evidence and adaptation notes | optional | unverified claims presented as fact |
| `examples/*.md` | examples and evaluation cases | optional | production secrets |
| `handoff-contracts/*.md` | bounded Codex execution handoff schema | optional | open-ended architecture brainstorming |

## Required Manifest: `module.json`

Minimal schema:

```json
{
  "name": "module-name",
  "version": "0.1.0",
  "status": "candidate",
  "description": "One-sentence bounded purpose of this module.",
  "source_patterns": [
    "https://github.com/anthropics/knowledge-work-plugins"
  ],
  "owners": ["Oleg Povalyukhin"],
  "applies_to": ["Project Execution OS"],
  "skills": [],
  "commands": [],
  "connectors_file": null,
  "handoff_contracts": []
}
```

### Allowed Lifecycle Status Values

Use only:

- `candidate` — captured and draftable, not yet validated in work;
- `tested` — used successfully in a real bounded case;
- `promoted` — approved for reuse as a standard module;
- `deprecated` — retained for traceability, no longer preferred.

No module may be described as `tested` or `promoted` without a recorded real-use result.

## Required Entrypoint: `README.md`

Every module `README.md` must contain:

1. **Purpose** — one bounded result the module helps produce.
2. **When To Use** — concrete matching situations.
3. **When Not To Use** — scope boundary and anti-overreach rule.
4. **Available Skills** — only those that actually exist in the folder.
5. **Available Commands** — only those that actually exist in the folder.
6. **Connector Requirements** — available, absent, or optional; never assumed.
7. **Evidence / Source Pattern** — where the structural idea came from, when borrowed.
8. **Status** — candidate/tested/promoted/deprecated.
9. **Validation Record** — link or note only after a real test exists.

## Skill Standard: `skills/<skill-name>/SKILL.md`

### Role of a Skill

A skill is not a giant system prompt and not an autonomous agent. It is a focused reusable capability description.

Each skill must be narrow enough to answer:

- what problem does this skill address;
- what signals mean it applies;
- what inputs it needs;
- what result it produces;
- what it must not do.

### Required YAML Frontmatter

```yaml
---
name: <skill-name>
description: <what the skill does and concrete task signals that should trigger its use>
status: candidate
version: 0.1.0
scope: <bounded domain or workflow>
---
```

The `description` must contain trigger conditions in plain language. It must not be vague, such as “helps with projects” or “expert assistant.”

### Required Sections

```markdown
# <Skill Name>

## Purpose

## Use When

## Do Not Use When

## Inputs Required

## Workflow

## Output Contract

## Constraints and Stop Conditions

## Evidence / References

## Validation Status
```

### Skill Rules

1. A skill must produce a bounded output or decision, not promise broad intelligence.
2. A skill must state when not to use it.
3. A skill must distinguish facts, assumptions, and recommendations when research or judgment is involved.
4. A skill requiring external evidence must route through current research rules rather than relying on old memory.
5. A skill may reference tools, but it must not assume those tools are connected or writable.
6. A skill that triggers code or repository changes must hand off through the existing Codex/GitHub execution standard where required; it must not silently become a new execution system.
7. A skill remains `candidate` until used successfully in a real task.

## Command Standard: `commands/<command-name>.md`

### Role of a Command

A command is for an explicit action. It is not automatically applied background expertise.

Examples of legitimate command classes:

- `/review` — produce a bounded review artifact;
- `/research` — run a scoped research investigation;
- `/write-spec` — turn an agreed concept into a specification;
- `/codex-handoff` — produce an approved bounded execution packet.

### Required YAML Frontmatter

```yaml
---
description: <explicit action this command performs>
argument-hint: "<expected input>"
status: candidate
version: 0.1.0
---
```

### Required Sections

```markdown
# /<command-name>

## Purpose

## Usage

## Preconditions

## Workflow

## Output Contract

## Stop Conditions

## Related Skills

## Validation Status
```

### Command Rules

1. Commands must be invoked explicitly or clearly requested by equivalent natural language.
2. Commands may use skills, but must list which skills they depend on.
3. A command may generate a draft artifact; it may not claim that a repo, project, task, or standard was updated unless execution actually happened and is confirmed.
4. Commands must stop when required source material, authority, or execution confirmation is missing.
5. Commands must not duplicate canonical lifecycle or storage logic from Project Execution OS; they must route to it.

## Connector Standard: `connectors.json`

The connector file is optional and declarative only.

Minimal shape:

```json
{
  "connectors": [
    {
      "name": "github",
      "purpose": "Read or write versioned technical artifacts when authorized.",
      "required": false,
      "access_assumption": "must_be_verified_at_runtime"
    }
  ]
}
```

Rules:

1. Never store tokens, API keys, credentials, or private URLs containing access secrets.
2. Never claim a connector exists merely because a module names it.
3. Tool access must be checked when a real action needs it.
4. A module must still describe a no-connector fallback when reasonable; otherwise it must state that execution is blocked without the connector.

## References and Evidence

When an external pattern materially influenced a module, create `references/sources.md` containing:

- source URL;
- date inspected;
- exact structural pattern borrowed;
- what was deliberately not copied;
- adaptation decision;
- future review triggers, such as commercialization, redistribution, or security-sensitive execution.

## Codex Handoff Integration

`handoff-contracts/` is optional. Use it only when a module produces an already-decided execution packet for Codex.

A handoff contract must:

- define the bounded action;
- name files or scope affected;
- list forbidden changes;
- define verification requirements;
- require the coder to report generated state versus executed state;
- route through `docs/CODEX_HANDOFF_STANDARD.md` rather than replacing it.

## Relationship to Existing System Layers

### Project Execution OS

This standard lives here because it defines a reusable operating format for file-based AI capabilities.

### Central Knowledge Library (CKL)

A small reusable lesson or proven pattern may remain a CKL entry. Do **not** create a full module when one Markdown knowledge entry is enough.

Create an agent module only when the capability needs one or more of:

- a reusable skill with trigger logic;
- an explicit command workflow;
- connector declarations;
- test examples;
- a Codex handoff contract.

### Agent Network OS

Agent Network OS may later consume promoted modules, but this document does not authorize runtime integration or database schema changes. Adoption requires a real MVP need and a separate approved execution decision.

### Reference-Idea-Library

Unreviewed donor links and promising external patterns belong first in `Reference-Idea-Library`. Only selected patterns promoted for reusable internal use belong in Project Execution OS.

## Candidate First Module Targets

The first modules should come from existing real workflows, not abstract architecture:

1. `external-pattern-research` — research and evaluate donor repositories or tools for reuse in an existing project.
2. `codex-execution-handoff` — package a decided bounded action for Codex without using Codex for open-ended reasoning.
3. `project-review` — review an existing project against its own entrypoint, state, constraints, and logs.

Do not create all three immediately. Create one only when the next real task requires it.

## Adoption Procedure

Use this procedure when introducing a module:

1. Identify a real recurring task that cannot be served cleanly by an existing document or CKL entry.
2. Inspect existing Project Execution OS artifacts and central reusable knowledge first.
3. Check external donor patterns only when useful.
4. Draft the smallest module that covers the task.
5. Mark it `candidate`.
6. Use it in one real bounded task.
7. Record what worked, failed, or was unnecessary.
8. Promote it only after the evidence justifies reuse.

## Anti-Patterns

Do not:

- create modules for every conversation;
- rewrite Project Execution OS into a plugin platform prematurely;
- invent a runtime marketplace before real tested modules exist;
- duplicate skills across multiple projects when one central module will do;
- call a draft file a validated skill;
- bury operational facts in chat instead of versioned artifacts when a module is actually adopted;
- automatically grant a module external tool permissions;
- use skill format as an excuse to make broad, bloated system prompts.

## Initial Validation Target

The first validation of this standard should be narrow:

- select one repeated workflow already present in Oleg's work;
- create one candidate module using this standard;
- use it on one actual task;
- review whether the separation between skill, command, reference evidence, and handoff contract reduced confusion or duplication.

## Source Record

The donor repository was previously captured in:

- `Reference-Idea-Library/references/anthropic-knowledge-work-plugins.md`

This document is the promoted candidate standard derived from that reference.

## Final Rule

Use Anthropic's file-based module discipline as a proven structural reference, not as a reason to overbuild.

The system gains value only when a small module solves a repeated real task more clearly than existing documentation already does.
