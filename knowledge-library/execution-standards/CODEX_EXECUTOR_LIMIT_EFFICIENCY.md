# Codex Executor Limit Efficiency

Type: execution-standard
Lifecycle status: active for the current environment
Captured: 2026-07-31
Owner decision: approved in conversation
Review status: operating decision approved; donor tools still require project-level trials

## Purpose

Reduce Codex subscription-limit consumption without reducing delivery quality by separating reasoning from execution.

## Core Architecture

Use the following division of responsibility:

- ChatGPT is the brain: it researches, analyzes, chooses the solution, decomposes the task, writes the execution packet, and reviews the result.
- Codex is the hands: it performs the already-decided changes, runs the specified checks, and returns evidence.
- The executor must not independently redesign the solution when a complete execution packet is available.

The practical objective is not to choose the strongest possible executor model. It is to provide a sufficiently precise task so that a cheaper executor can complete it reliably.

## Current Model Policy

Current default for Codex execution:

1. GPT-5.6 Luna Medium — default executor.
2. GPT-5.6 Luna High — use only after a demonstrated Medium failure or when the packet contains materially higher execution risk.
3. GPT-5.6 Luna Max — exception for large, tightly coupled multi-file changes where additional reasoning is justified.
4. Stronger general-purpose models — use for architecture, unresolved ambiguity, root-cause analysis, or when the task has not yet been fully decided.

Do not use Max merely because a task is important. Importance should be handled by better decomposition, explicit verification, and review.

Model names, availability, rate cards, and recommended replacements are time-sensitive. Revalidate them against current official OpenAI documentation before changing this policy.

## Execution Packet Standard

Every already-decided Codex handoff should contain:

```text
GOAL
One measurable result.

ALLOWED FILES
Exact file list or directory boundary.

CHANGE POINTS
Named classes, functions, symbols, or precise regions.

DO NOT
Do not redesign architecture.
Do not install dependencies unless explicitly authorized.
Do not edit unrelated files.
Do not explore alternative implementations.

VERIFY
Exact commands and expected success conditions.

RETURN ONLY
- changed files;
- verification results;
- blocking error, if any.
```

If the executor fails, first improve the packet or reduce its scope. Do not automatically escalate the model.

## Context-Minimization Policy

### AGENTS.md

- Keep the root `AGENTS.md` short and limited to stable global rules.
- Place module-specific instructions in nested `AGENTS.md` files near the relevant code.
- Do not store project history, completed plans, long explanations, or full error logs in `AGENTS.md`.

### Repository Context

- Give the executor exact paths and symbols whenever possible.
- Do not send the entire repository when a map or targeted file set is sufficient.
- Keep automatic IDE context disabled when the execution packet already identifies the required files.
- Connect only the tools required for the current task.
- Avoid loading multiple MCP servers by default because tool definitions and results also consume context.

### Command Output

Save full command output to files, for example:

```text
logs/test-full.log
```

Return to the model only:

- exit code;
- pass/fail counts;
- first meaningful error;
- a short tail when necessary.

Do not return complete installation logs, verbose test traces, huge file lists, or large JSON payloads unless the exact content is required for diagnosis.

## Thread And Cache Policy

- One Issue or execution packet, including its corrections, should normally stay in one Codex thread.
- Keep the stable beginning of the context unchanged so automatic prompt caching can reuse it.
- Do not create a new thread for every small correction.
- Do not keep one endless thread for an entire project.
- At a logical boundary, create a short `HANDOFF.md`, preserve the current diff and verification state, and start a clean thread.
- Use context compaction only at meaningful boundaries, not as a substitute for controlled context.

Prompt caching is an automatic optimization, not the primary strategy. The main savings must come from smaller context, fewer model passes, and less executor reasoning.

## Execution Routing Ladder

Use the cheapest reliable mechanism:

1. Deterministic script or native tool — copying, renaming, formatting, test execution, generated changes, and other mechanical work.
2. Structural automation such as `ast-grep` — repetitive syntax-aware transformations.
3. Local model through Ollama or another local provider — bounded low-risk edits that can be verified automatically.
4. Luna Medium — normal Codex executor work.
5. Luna High or Max — only after justified escalation.
6. Strong architecture model — unresolved design, ambiguity, or root-cause reasoning.

Every lower-cost route must still use explicit verification and diff review.

## Donor Patterns And Candidate Tools

### Aider Architect/Editor

Reusable donor pattern: separate solution design from code editing. The architect decides; the editor applies the decision.

Source:
- https://aider.chat/2024/09/26/architect.html

Adoption decision:
- use the architectural principle;
- do not replace the current Codex workflow merely to copy the tool.

### Aider Repo Map

Reusable donor pattern: provide a compact ranked map of files, symbols, and relationships rather than the whole repository.

Source:
- https://aider.chat/docs/repomap.html

Candidate implementation:
- maintain a compact `PROJECT_MAP.md` or generate an equivalent map on demand;
- include paths, key classes/functions, and critical relationships;
- open full files only after the map identifies them as relevant.

### Serena MCP

Candidate use: symbol-level navigation and editing in large repositories.

Source:
- https://github.com/oraios/serena

Trial rule:
- test Serena as the only additional MCP on a large repository;
- measure context use, task success, and unnecessary file reads;
- do not enable it globally until the trial shows a net benefit.

### Repomix

Candidate use: generate a repository inventory, token report, or compressed structural snapshot.

Source:
- https://github.com/yamadashy/repomix

Boundary:
- do not automatically feed the full Repomix output to Codex;
- use it to identify heavy files and generate a compact map or selected context package.

### ast-grep

Candidate use: deterministic syntax-aware bulk changes, import rewrites, API migrations, and repetitive refactors.

Source:
- https://github.com/ast-grep/ast-grep

Boundary:
- preview and verify every bulk transformation;
- use the model to define or review the transformation, not to manually repeat it across many files.

### Local Models

Current available local candidates include `qwen2.5-coder:7b` and `deepseek-coder:6.7b` through Ollama.

Candidate use:
- bounded edits with strong automated verification;
- diagnostics, summaries, and low-risk transformations;
- zero subscription-limit consumption for successful local work.

Boundary:
- escalate when verification fails or the task requires broader reasoning.

## Measurement

Evaluate the system by cost per successful verified outcome, not by raw token count alone.

For trials, record:

- selected execution route and model;
- task scope;
- number of model turns;
- files read and changed;
- verification result;
- rework required;
- context or limit consumption when visible;
- whether escalation was necessary.

A cheaper attempt that repeatedly fails may cost more than one correctly scoped higher-level attempt.

## Applies To

- Codex CLI and Codex IDE execution;
- GitHub-backed technical projects;
- already-decided coding handoffs;
- repetitive verified development work;
- projects where subscription limits are a material constraint.

## Triggers

Load this entry when:

- preparing an already-decided Codex handoff;
- choosing a Codex executor model;
- reducing token, context, or subscription-limit use;
- designing repository maps or selective context;
- considering Serena, Repomix, Aider patterns, ast-grep, or local-model routing;
- reviewing why an executor consumed excessive limits.

## Do Not Load When

- the request is not technical execution;
- the current task is pure research, writing, or casual discussion;
- architecture has not yet been decided and the executor must genuinely reason about the solution;
- the work does not use Codex or a comparable code executor.

## Risks And Boundaries

- Over-restricting the executor can hide missing assumptions; verification must expose them.
- A compact repository map can become stale; regenerate or validate it after major structural changes.
- MCP tools may save file-reading tokens but add tool-schema and result context.
- Local models can produce plausible but incorrect edits; automatic checks and diff review are mandatory.
- Model rate cards and product behavior can change; time-sensitive policy must be rechecked.

## Related Standards

- `docs/CODEX_HANDOFF_ENTRYPOINT.md`
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/API_RUNTIME_COST_CACHE_LOGGING_STANDARD.md`
- `docs/AGENT_QUALITY_SCORECARD_STANDARD.md`
- `docs/ALWAYS_TRANSFER_READY_STATE_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`

## Final Rule

The brain solves the problem once. The hands execute the decided solution with the smallest reliable model, the smallest sufficient context, and explicit verification.
