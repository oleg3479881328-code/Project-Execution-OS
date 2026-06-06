# Agent Index-First Adoption Status

Updated: 2026-06-06
Status: `partially_committed_pending_executor`

## Committed

- `docs/AGENT_INDEX_FIRST_ENTRY_STANDARD.md`
- `docs/SEMANTIC_SEARCH_RUNTIME.md`
- GitHub implementation handoff: `https://github.com/oleg3479881328-code/Project-Execution-OS/issues/21`

## Protected Changes Pending Codex

Direct connector writes were blocked for protected executable and agent-entry files. Issue `#21` requires Codex to update:

- `AGENTS.md`;
- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`;
- `docs/CONTEXT_ASSEMBLY_STANDARD.md`;
- `docs/AGENT_CREATION_STANDARD.md`;
- `docs/integrations/chatgpt/CORE_SYSTEM_PROMPT.md`;
- `docs/ROUTER.md` when needed for the narrow route;
- semantic runtime scripts;
- semantic pilot workflow;
- stable context manifest.

## Intended Mandatory Rule

For project-related work:

`START_HERE -> ROUTER -> narrow route -> indexes -> semantic retrieval when needed -> canonical files -> minimum sufficient context`

## Boundary

Structural indexing is already operational. Local embeddings and vector-store retrieval become operational only after Codex implementation and validation evidence are posted in issue `#21`.
