# Agent Index-First Entry Standard

Updated: 2026-06-06
Status: `active`

## Purpose

Require every project-related agent to use repository indexes before broad scanning.

## Mandatory Entry Order

For project-related work:

1. read `START_HERE.md`;
2. open `docs/ROUTER.md`;
3. open the narrowest routed standard or block;
4. read the relevant project entrypoint when a specific project is involved;
5. inspect existing curated and generated indexes before broad file reads;
6. use semantic retrieval when the repository is large, the wording is uncertain, or the correct files are not obvious;
7. open canonical source files for the selected hits;
8. load only the minimum evidence needed for the active task.

## Mandatory Rule

Do not scan an entire repository, block tree, or knowledge library by default.

Before broad scanning, use:

- `PROJECT_INDEX.md`;
- section indexes;
- `indexes/system-index.json`;
- `indexes/BLOCK_CATALOG.generated.md`;
- `indexes/KNOWLEDGE_CATALOG.generated.md`;
- semantic retrieval when available.

## Semantic Retrieval Boundary

Semantic results are navigation leads. They do not replace canonical files.

After retrieval, verify:

- source path;
- lifecycle status;
- freshness;
- task applicability;
- minimum excerpts needed.

## Executor Rule

Codex and other execution agents should receive a bounded context package. They should not rediscover the whole repository unless the task explicitly requires repository-wide analysis.

## Final Rule

Index first. Retrieve narrowly. Verify canonical sources. Load the minimum sufficient context.