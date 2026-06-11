# Pimenov.ai — reusable system patterns for Project Execution OS

Date captured: 2026-06-11
Source: https://pimenov.ai/

## Purpose

Preserve reusable engineering patterns extracted from a targeted review of `pimenov.ai` for future use across Project Execution OS projects.

## Core patterns worth adopting

### 1. Agent-ready systems

A useful system for agents must provide predictable routes, clean data, stable entrypoints, explicit relationships, and machine-readable rules. Human-friendly presentation alone is insufficient.

Application to Project Execution OS:

- keep `START_HERE.md` minimal and stable;
- route through `docs/ROUTER.md`;
- use the narrowest relevant route for the active request;
- keep project entrypoints explicit;
- avoid forcing an agent to read the whole repository by default.

Potential future standard:

- create `AGENT_READY_PROJECT_STANDARD.md` with the minimum project structure: entrypoint, current state, next action, constraints, active files, and permissions boundary.

### 2. Separate design from execution

Use an agent to understand a problem, design a workflow, document it, and improve it. Once a repeated workflow stabilizes, move routine execution into a deterministic layer such as a script, skill, pipeline, or orchestrator.

Rule:

- first run: agent-led design and debugging;
- after stabilization: deterministic execution;
- agent remains for exceptions, review, and optimization.

Relevant projects:

- reels factory;
- content processing;
- publishing workflows;
- server operations;
- future personal secretary workflows;
- QuizLight video-card extraction;
- bulk file operations.

### 3. Use eval loops instead of endlessly expanding prompts

A good result should pass explicit quality checks before moving forward.

Minimal loop:

1. generate;
2. evaluate against predefined criteria;
3. reject below-threshold output;
4. repair;
5. re-evaluate;
6. approve only passed output.

Use real failures as future regression tests.

Recommended first applications:

- reels quality checklist;
- website design review;
- research quality checks;
- important letters;
- code review;
- legal and immigration document review.

### 4. Separate generator and reviewer roles

For non-trivial work, do not let generation and approval collapse into one undifferentiated pass.

Recommended pattern:

1. executor creates draft;
2. independent reviewer checks against rules;
3. executor fixes issues;
4. human approves external or high-risk actions.

### 5. Read-only infrastructure audit before changes

Before changing servers, first inspect and document the current state.

Audit outputs:

- server passport for each machine;
- overall operating state for the infrastructure.

Suggested server passport fields:

- provider;
- region;
- cost;
- purpose;
- IP addresses and domains;
- running services;
- containers;
- open ports;
- disks;
- backups;
- last checked date;
- allowed changes;
- rollback instructions;
- status: active, test, paused, removable.

### 6. Human approval gates for external actions

Agents should operate with permission boundaries comparable to employees.

For the future personal secretary:

- reading email: separate permission;
- drafting email: separate permission;
- sending email: explicit owner approval;
- viewing calendar: separate permission;
- creating events: separate permission;
- deletion: restricted;
- passwords, tokens, bank-card data, and similar secrets: never store in project files.

### 7. Knowledge systems must be machine-readable and maintained

The tool is secondary. The important properties are:

- one source of truth;
- machine-readable structure;
- explicit links;
- update process;
- retirement of stale knowledge;
- detection of gaps and orphan materials.

A future graph should be operational, not decorative. It should reveal:

- recurring topic without a formal knowledge entry;
- isolated high-value material;
- stale blocks;
- orphan references;
- weak or accidental connections.

## Project-specific applications

### Website design block

Adopt an iterative visual review loop:

1. build minimum version;
2. run locally;
3. capture screenshots;
4. inspect via vision;
5. click through user flows;
6. fix issues;
7. repeat screenshots;
8. compare variants;
9. generate assets where necessary;
10. preserve extracted design rules.

### Reels factory

Use a manual quality checklist before automation:

- first frame captures attention;
- theme is understandable without sound;
- subtitles are readable;
- no visual clutter;
- duration fits the platform;
- no obvious copyright issue;
- output matches the target platform;
- publishable without manual repair.

### Personal secretary

Stay in manual validation mode until at least 10 real intake batches are processed. Do not add Telegram, Notion, n8n, durable storage, or broad automation prematurely.

## Explicit non-actions for now

Do not implement merely because the patterns are interesting:

- Notion migration;
- knowledge graph;
- Telegram bot;
- n8n layer;
- broad multi-agent architecture;
- complex RBAC;
- audio layer;
- full-stack copy of another person's tooling.

## Immediate recommended next step

Create a simple manual reels-quality checklist and use it on real outputs before automating anything.
