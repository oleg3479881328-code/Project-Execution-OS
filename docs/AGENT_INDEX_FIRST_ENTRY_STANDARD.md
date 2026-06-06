# Agent Index-First Entry Standard

## Purpose

This standard makes selective, index-first repository entry mandatory for project-related agents.

Its goal is to reduce unnecessary scanning, token cost, and wrong-file drift while preserving canonical-file verification.

## Core Rule

Use this order before broad scanning:

```text
START_HERE.md
-> docs/ROUTER.md
-> routed standard or project entrypoint
-> curated indexes
-> generated indexes under indexes/ when relevant
-> semantic retrieval when wording is uncertain or the right files are not obvious
-> canonical files for selected hits
```

Semantic hits are navigation leads, not truth.

Open the canonical files before relying on a retrieved hit.

## Mandatory Behavior

For project-related work, an agent must:

1. enter through `START_HERE.md`;
2. follow `docs/ROUTER.md`;
3. read the specific project's `PROJECT.md` when a project is involved;
4. inspect curated indexes before broad scanning;
5. inspect generated indexes under `indexes/` when they are relevant to the task;
6. use semantic retrieval when wording is uncertain, repository size makes direct scanning wasteful, or correct files are not obvious;
7. open canonical files for promising hits before using them as evidence;
8. load only the minimum sufficient evidence for the active action.

## Curated Indexes

Examples of curated indexes include:

- `PROJECT_INDEX.md`
- `blocks/PROJECT_INDEX.md`
- `knowledge-library/PROJECT_INDEX.md`
- project-specific indexes created by the project itself

## Generated Indexes

Generated indexes may exist under `indexes/`.

Treat them as discovery aids.

They narrow candidate files, but they do not replace canonical documents.

## Semantic Retrieval Rule

Use semantic retrieval when:

- the user description does not match exact repository wording;
- multiple plausible files might contain the answer;
- the repository is large enough that manual scanning is inefficient;
- cross-lingual wording may hide the correct file.

Do not use semantic retrieval as an excuse to skip canonical-file verification.

## Anti-Scan Rule

Do not full-scan a repository by default when indexes or semantic retrieval can narrow the candidate set first.

Mass scanning is allowed only when:

- no adequate index exists;
- retrieval is unavailable or clearly insufficient;
- the task genuinely requires whole-repository evidence.

## Related Nodes

- `docs/CONTEXT_ASSEMBLY_STANDARD.md`
- `docs/INDEXING_STANDARD.md`
- `docs/SEMANTIC_SEARCH_RUNTIME.md`
- `workflow-templates/project-bootstrap/AGENTS_TEMPLATE.md`
