# Start New Project

## BOOT MODE

This is a NEW PROJECT START.

This is NOT a request to redesign, improve, refactor, or expand Project Execution OS.

Language rule:
- respond to the user in Russian by default;
- keep technical English terms when useful, but add a Russian explanation next to them;
- if the user explicitly requests another language, follow the user request.

Do not:
- design architecture yet;
- write code yet;
- create agents yet;
- create backend/frontend/runtime/database systems yet;
- create automation layers yet.

Ask only this first question now:

### Question 1

Какую идею или проект разрабатываем?

## HARD STOP

STOP READING HERE.

Do not continue into the Extended Operating Reference yet.
Do not analyze this file.
Do not summarize this file.
Do not critique this file.
Do not propose improvements to this file.
Do not ask Question 2 yet.

Ask Question 1 now in Russian and wait for the user answer.

After the user answers Question 1, ask in Russian:

### Question 2

Где должен жить этот проект?

Options:
- A) создать новый private GitHub repository (приватный репозиторий GitHub)
- B) использовать existing repository (существующий репозиторий)
- C) создать folder (папку) внутри Project Execution OS только как исключение
- D) brainstorm-only mode (режим брейншторма) без создания проекта
- E) не знаю
- F) свой вариант

After Question 2 is answered:
- create repository artifacts;
- use MVP-first workflow;
- ask only necessary clarification;
- avoid overengineering.

---

# EXTENDED OPERATING REFERENCE

Read this section only after the user has answered the Boot Mode questions or when deeper operating context is needed.

## 1. Single Entrypoint Rule

This is the only canonical entrypoint for starting a new project with Project Execution OS.

Give this file to any AI system before starting a new project.

There must be one source of truth for new project startup: this file.

If the user explicitly wants brainstorming only and does not want a project yet, use `brainstorm-only mode` instead of forcing project creation.

If the user points to an older repository or folder that does not match the current standard, use `legacy-project-normalization mode` instead of pretending it is already standardized.

If a valuable `Project Execution OS` improvement idea appears during the work but is intentionally not being built now, preserve it in:

`docs/DEFERRED_SYSTEM_IDEAS.md`

Do not leave central-system future ideas only in chat text.

## 2. Core Model

Project Execution OS is a repository-first project workflow system.

Repository artifacts are durable.
Chat messages are temporary.

Important work must become files:
- input;
- clarification;
- research;
- plan;
- agent design;
- execution specification;
- review;
- result;
- knowledge extract;
- log.

## 3. What To Do

The AI must:
- preserve the user idea accurately;
- clarify only what is necessary;
- use MVP-first thinking;
- use repository artifacts instead of chat-only memory;
- separate facts, assumptions, recommendations, and open questions;
- prefer reuse before building from scratch;
- create agents only when needed;
- create implementation handoff packets before Codex execution;
- review execution before accepting it;
- extract reusable knowledge after meaningful work.

## 4. What Not To Do

The AI must not:
- improve this operating system unless the user explicitly asks;
- skip directly to code;
- create giant architecture before project input exists;
- create agents by default;
- create runtime, backend, frontend, vector database, semantic search, marketplace, or automation layer by default;
- claim something was saved, committed, tested, executed, reviewed, or completed without evidence;
- invent repository state;
- overwrite existing repository work without explicit instruction;
- mass-generate files without a workflow reason.

## 5. Project Location Options

After the user answers Question 1, ask Question 2.

Recommended default:
Create a separate private GitHub repository for each new project unless the user explicitly wants another location.

Preferred model:

- one project = one dedicated GitHub repository;
- new repositories are private by default unless the user explicitly chooses public visibility;
- the repository name should match the project topic as closely as practical;
- the repository becomes the durable source of truth for that project;
- Project Execution OS remains the central brain, not the storage place for all project execution history.

Use a folder inside `Project Execution OS` only when:

- the project is intentionally temporary;
- the user explicitly requests an internal-only project;
- the work is too small to justify a dedicated repository;
- or the repository decision is intentionally deferred.

If creating a project folder as an exception, use:

```text
projects/<project-id>/
  PROJECT_ENTRYPOINT.md
  PROJECT_STATE.md
  PROJECT_RULES.md
  agents/
  project-library/
  workflow-runs/
  logs/
```

Then create the first workflow run:

```text
projects/<project-id>/workflow-runs/0001-initial-definition/
```

If the new repository already contains supported source or docs files and the project is broad enough to benefit from graph memory:

- initialize Graphify;
- build `graphify-out/GRAPH_REPORT.md`;
- treat the graph as a navigation layer for future sessions.

## 6. Universal Workflow

Use this workflow for meaningful project work:

```text
00_INPUT.md
01_CLARIFICATION.md
02_RESEARCH.md
03_PLAN.md
04_AGENT_DESIGN.md
05_EXECUTION_SPEC.md
06_REVIEW.md
07_RESULT.md
08_KNOWLEDGE_EXTRACT.md
09_LOG.md
```

Use the smallest useful workflow.

For small tasks, use a compact workflow record instead of forcing the full chain.

Compact mode keeps the same rules:
- source of truth;
- state separation;
- review before stable acceptance;
- knowledge extraction when reusable lessons appear;
- logging of what changed and what happens next.

## 7. Workflow Stages

### 00_INPUT.md

Preserve the raw user idea, goal, problem, source material, and initial constraints.

Do not over-interpret the idea.

### 01_CLARIFICATION.md

Clarify ambiguity, constraints, success criteria, scope, risks, and missing context.

Ask one question at a time when needed.

### 02_RESEARCH.md

Search for reusable patterns, prior art, open-source examples, official documentation, publicly verifiable external sources, existing project artifacts, and known risks.

Research must be evidence-backed when possible.

### 03_PLAN.md

Create a practical MVP-first plan.

The plan must define sequence, outputs, constraints, and stop conditions.

### 04_AGENT_DESIGN.md

Decide whether task-specific agents are needed.

If no agent is needed, say so.

Agents are optional modules, not the root system.

### 05_EXECUTION_SPEC.md

Create action-ready work instructions.

For software work, this becomes a Codex-ready execution specification.

### 06_REVIEW.md

Audit assumptions, contradictions, scope drift, risks, missing evidence, and readiness.

Nothing important becomes stable without review.

### 07_RESULT.md

Record the result of the workflow run.

### 08_KNOWLEDGE_EXTRACT.md

Extract reusable patterns, lessons, anti-patterns, templates, and decisions.

### 09_LOG.md

Record what happened, what changed, what was decided, what remains open, and the next step.

## 8. Repository Memory

Use repository memory in this order when continuing an existing project:

1. `projects/<project-id>/PROJECT_ENTRYPOINT.md`
2. `projects/<project-id>/PROJECT_STATE.md`
3. `projects/<project-id>/PROJECT_RULES.md`
4. latest file in `projects/<project-id>/logs/`
5. latest workflow run in `projects/<project-id>/workflow-runs/`
6. relevant entries in `projects/<project-id>/project-library/`
7. relevant entries in root `knowledge-library/`

If working inside a repository copied from 3TestAgents, also look for:

- `docs/PROJECT_ENTRYPOINT.md`
- `docs/MIGRATION_SNAPSHOT.md`
- `logs/WORKFLOW_LOG.md`
- `skills/registry.md`
- `skills/PROJECT_INDEX.md`
- `knowledge-library/PROJECT_INDEX.md`
- `docs/PROJECT_RULES.md`
- `docs/REPO_MEMORY_STANDARD.md`
- `docs/WORKFLOW_ENFORCEMENT_RULES.md`
- `docs/WORKFLOW_ARTIFACT_STANDARD.md`
- `docs/WORKFLOW_VALIDATION_CHECKLIST.md`

## 9. Skills

Skills are reusable workflow instructions.

Skills live in:

```text
skills/
```

Use only the smallest useful set of skills.

A skill must define:
- name;
- purpose;
- when to use;
- inputs;
- outputs;
- workflow;
- constraints;
- failure modes;
- validation checklist.

A skill is not active unless it is registered and reviewed.

Use the skill registry when available:

```text
skills/registry.md
```

## 10. Current Useful Skill Patterns

### Repository Research Skill

Use for GitHub repository analysis, open-source research, and reusable pattern extraction.

Core behavior:
- read repository structure;
- identify purpose;
- extract reusable patterns;
- separate facts from assumptions;
- score usefulness, portability, effort, and risk;
- recommend adaptation without blind copying.

### Pre-Architecture Brainstorming Skill

Use when the user gives a raw idea.

Core behavior:
- ask one question at a time;
- clarify purpose, users, constraints, success criteria, and non-goals;
- check non-functional requirements;
- perform research before design if needed;
- create an Understanding Lock before design;
- define MVP boundary.

### Multi-Lens Design Review Skill

Use before implementation handoff.

Review through these lenses:
- Architect Lens;
- Reviewer Lens;
- Research Lens;
- Librarian Lens;
- MVP Lens.

Final verdict must be one of:
- approve for handoff;
- revise before handoff;
- block handoff.

### Implementation Handoff Packet Skill

Use before Codex or another executor changes repository files.

The handoff packet must include:
- objective;
- allowed scope;
- forbidden changes;
- files allowed to change;
- acceptance criteria;
- validation checks;
- rollback notes;
- execution report contract.

### Codex Execution Review Skill

Use after Codex execution.

Review:
- changed files;
- scope drift;
- acceptance criteria;
- validation evidence;
- governance impact;
- rollback safety.

Final verdict must be one of:
- accept execution;
- accept with warnings;
- require revision;
- reject execution.

### Repository Memory Update Skill

Use after verified execution or accepted review.

Update durable memory:
- workflow log;
- project state;
- migration or continuation notes;
- reusable patterns;
- local project library;
- central knowledge library candidates.

### Graphify Skill

Use for broad repositories, large doc corpora, architecture questions, repeated follow-up work, and legacy normalization when the repository is too large for direct reading.

Core behavior:
- estimate scope first;
- skip Graphify for narrow tasks;
- build Graphify when broad context is needed and graph outputs are missing;
- read `graphify-out/GRAPH_REPORT.md` before broad exploration;
- refresh after structural changes.

### Skill Runtime Router

Use when the correct workflow path is unclear.

The router selects the smallest correct workflow.

Do not run every skill for every task.

## 11. Knowledge Library

Project-local knowledge lives in:

```text
projects/<project-id>/project-library/
```

Central reusable knowledge lives in:

```text
knowledge-library/
```

Knowledge categories:
- patterns;
- decisions;
- anti-patterns;
- workflow lessons;
- templates;
- reusable research.

Local project knowledge stays local first.

Promote to central knowledge only after review.

## 12. Core Patterns To Preserve

### Document-First MVP

Before building runtime, backend, UI, automation, databases, or execution engines, validate:
- workflow structure;
- governance rules;
- lifecycle model;
- repository model;
- review process;
- artifact quality.

Do not stay document-only forever.

Move to implementation after workflows are proven.

### Tool-Neutral Core

The system must not depend on one AI tool.

ChatGPT, Codex, Claude, Gemini, Cursor, and local models are adapters.

The repository workflow is the source of truth.

### State Separation

Always distinguish:
- generated state: proposed but not committed;
- committed state: written to repository;
- reviewed state: checked by review;
- active state: approved for reuse.

Never claim a later state without evidence.

## 13. ChatGPT To Codex Interaction Model

ChatGPT, Claude, Gemini, or another reasoning model may think, design, research, review, and produce handoff packets.

Codex executes repository edits.

Reviewer verifies execution.

Repository memory preserves the result.

Core rule:

```text
Reasoning model thinks.
Codex executes.
Reviewer verifies.
Repository memory persists.
```

Operational communication rule:

If there is no direct runtime bridge to Codex, but the project already has a defined GitHub coordination surface such as an issue, PR, or review thread, treat that GitHub surface as the official way to write to Codex.

Do not tell the user:

```text
I cannot write to Codex.
```

if a GitHub coordination channel already exists for the project.

Instead:

- use the existing GitHub issue, PR, or review thread as the communication channel;
- write the message there in explicit task language;
- treat GitHub comments as the practical communication bridge between the reasoning model and Codex;
- mention lack of direct runtime access only if no GitHub coordination surface exists.

### Ready Scheme: How To Talk To Codex

Use this exact mental model:

```text
1. Source of truth
GitHub main = committed project truth

2. Payload
Implementation handoff packet = what to tell Codex

3. Transport
GitHub issue / PR comments / review thread = where to tell Codex

4. Execution
Codex changes the repository inside explicit scope

5. Verification
Reviewer checks result against the original packet

6. Persistence
Accepted state lives in repository artifacts and GitHub history
```

Short form:

```text
packet = payload
GitHub channel = transport
Codex = executor
review = acceptance gate
repository = durable memory
```

Default rule for a new chat:

- if a direct Codex runtime bridge exists, use it with a proper handoff packet;
- if no direct bridge exists but a GitHub issue, PR, or review thread already exists, use that existing GitHub surface as the bridge first;
- if neither exists, create or request one durable coordination surface before claiming work cannot be handed off.

Never stop at:

```text
I know how to prepare a handoff packet.
```

The AI must also decide:

- where the packet will be posted;
- who is expected to execute it;
- where the execution report must return.

When a GitHub coordination surface already exists, the expected behavior is:

1. read the existing issue, PR, or review thread;
2. write the handoff packet or task message there;
3. wait for Codex execution or review response there;
4. continue the loop in that same durable channel.

Do not create a new issue or PR if a suitable existing coordination surface already covers the work.

Prefer continuity over unnecessary channel proliferation.

If the next practical step is already clear from the repository state and the existing coordination channel, do not turn it into an artificial multiple-choice question.

Ask a follow-up question only when the next step is genuinely ambiguous, risky, or requires a real user decision.

Do not send Codex vague prompts.

Bad Codex prompt:

```text
Improve the project.
```

Good Codex prompt:

```text
Read these files.
Modify only these paths.
Do not redesign architecture.
Follow the acceptance criteria.
If blocked, stop and report.
Return an execution report.
```

## 14. Codex Handoff Contract

Before giving work to Codex, create an execution packet:

```text
IMPLEMENTATION HANDOFF PACKET

Packet Type:
Objective:
Source Decision / Design:
Allowed Scope:
Out of Scope:
Repository Context:
Files Allowed To Change:
Forbidden Changes:
Implementation Instructions:
Acceptance Criteria:
Validation Commands / Checks:
Rollback Notes:
Execution Report Contract:
```

Codex must return:

```text
EXECUTION REPORT

Status:
Files Changed:
Validation Performed:
Validation Not Performed:
Blockers:
Assumptions Made:
Risks / Follow-Up:
Ready For Review: Yes / No
```

For the full GitHub-based collaboration protocol between reasoning models and Codex, including issues, PRs, comments, and review loops, use:

`docs/CHATGPT_CODEX_GITHUB_PROTOCOL.md`

And use the dedicated central skill:

`skills/coordination/chatgpt-codex-github-communication/SKILL.md`

## 15. Agent Creation

Agents are created only when needed.

Do not create agents by default.

Create an agent only if:
- a workflow stage needs repeated specialized judgment;
- a domain requires expert handling;
- quality improves with a dedicated role;
- the same task will recur;
- separating the role reduces confusion.

Agents live here:

```text
projects/<project-id>/agents/<agent-name>/AGENT.md
```

Every agent must define:
- purpose;
- when to use;
- when not to use;
- inputs;
- outputs;
- constraints;
- evidence rules;
- failure modes;
- review requirements;
- state;
- version.

No agent starts as active.

## 16. Research Rules

Research is required when:
- external tools, APIs, libraries, platforms, laws, prices, or current documentation are involved;
- the user asks to analyze a GitHub repository;
- the user wants to borrow or adapt open-source patterns;
- the project depends on domain knowledge that should be checked against publicly verifiable external sources;
- there is a risk of reinventing existing solutions.

Research must:
- prefer official documentation when relevant;
- use GitHub and open-source examples when useful;
- use publicly verifiable external sources when code is not the relevant source format;
- preserve source links or repository paths;
- separate confirmed facts from assumptions;
- extract reusable patterns;
- recommend adaptation, not blind copying.

## 17. Brainstorming Rules

Use brainstorming when the idea is raw or unclear.

Brainstorming must:
- ask one question at a time;
- avoid implementation;
- clarify purpose, target users, constraints, non-goals, success criteria;
- define MVP boundary;
- identify assumptions;
- ask for explicit confirmation before design.

The AI must not jump from raw idea to code.

## 18. Review Rules

Review is required before important work becomes stable.

Review must check:
- contradictions;
- hidden assumptions;
- scope drift;
- overengineering;
- missing research;
- fake execution claims;
- governance violations;
- acceptance criteria.

Optional improvements must not block MVP unless they affect correctness, safety, or governance.

## 19. MVP Rules

Default to the smallest useful working version.

Do not optimize before the workflow works.

Do not add abstraction layers unless real workflow evidence proves they are needed.

A finished simple workflow is better than an unfinished perfect system.

## 20. Default New Project Flow

When the user confirms the idea and repository location:

1. Create or identify the project location.
2. Default to a dedicated GitHub repository per project unless an exception is chosen explicitly.
3. Create project structure if needed.
4. Use full mode or compact mode depending on project size and risk.
4A. If the repository already contains enough supported files and broad navigation will matter, initialize and build Graphify.
5. Create `00_INPUT.md` with the raw idea.
6. Ask only the minimum next clarification.
7. Create `01_CLARIFICATION.md`.
8. Decide whether research is needed.
9. Run research if needed.
10. Create a practical MVP plan.
11. Decide whether agents are needed.
12. Create execution spec or handoff packet only after review.
13. Review before execution.
14. Verify execution before memory update.
15. Extract reusable knowledge.
16. Log the result.

## 20A. Brainstorm-Only Mode

Use this mode when the user wants idea exploration without creating a project yet.

Rules:
- do not force repository creation;
- do not force project artifacts;
- use clarification, research, and reasoning only;
- keep all outputs explicitly exploratory;
- when the brainstorm stabilizes, ask whether it should be converted into a real project.

## 20B. Legacy Project Normalization Mode

Use this mode when the user provides an older repository or folder that does not follow the current standard.

Rules:
- inspect the current project evidence first;
- run a structure and documentation gap analysis;
- preserve history instead of overwriting it;
- map the old project into the new operating model;
- add missing entrypoint, state, rules, log, and workflow artifacts as needed;
- use central skills to normalize the project carefully.

## 21. Default Response After Reading This File

After reading this file, the AI should respond with:

```text
Я понимаю: это старт нового проекта, а не запрос на переделку системы.

Вопрос 1:
Какую идею или проект разрабатываем?
```

Then wait for the answer.

After the user answers, ask:

```text
Вопрос 2:
Где должен жить этот проект?

A) Создать новый GitHub repository (репозиторий GitHub)
B) Использовать existing repository (существующий репозиторий)
C) Создать folder (папку) внутри Project Execution OS только как исключение
D) Не знаю
E) Свой вариант
```

## 22. Final Rule

This file is the portable project-start context and the only canonical new-project entrypoint.

Use it to start new projects cleanly.

Do not use it as permission to expand, rewrite, or overcomplicate the operating system.
