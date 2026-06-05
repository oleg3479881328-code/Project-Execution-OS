# Knowledge Library Access Architecture

## Status

Approved implementation direction for the first repository-backed access layer.

## Decision Summary

Use this stack:

`GitHub -> Obsidian -> Quartz`

- `GitHub` remains the canonical source of truth for versioned Markdown content.
- `Obsidian` opens the local `Project-Execution-OS` folder directly as a vault instead of maintaining a second note copy.
- `Quartz` runs as a separate local portal scaffold fed only by an explicit allowlist sync step.

## Why This Architecture

- It preserves one editable Markdown source instead of splitting authoring across tools.
- It gives the owner a rich local reading and editing interface through Obsidian.
- It gives the owner a browser-readable publication layer without exposing the whole repository.
- It keeps public release optional and deferred.

## Boundary

The Quartz portal must never publish the entire `Project-Execution-OS` repository by default.

Publication input must come from a controlled copy step or an equivalent explicit allowlist.

The following classes of material are out of bounds for default publication:

- internal standards not explicitly reviewed for release;
- logs and workflow traces;
- project-private notes;
- secrets, credentials, tokens, or machine-specific paths that are not required for public reading;
- any repository area not named in the active allowlist.

## First Implementation Shape

The first implementation is local-preview-first:

1. clone or update the main repository locally;
2. open the local repository folder as an Obsidian vault;
3. sync only approved files into the Quartz portal `content/` folder;
4. preview the portal locally;
5. publish later only after a separate review step.

## Source Files

- `docs/KNOWLEDGE_LIBRARY_ACCESS_SETUP_WINDOWS.md`
- `docs/KNOWLEDGE_LIBRARY_PORTAL_PUBLISHING_BOUNDARY.md`
- `docs/KNOWLEDGE_LIBRARY_PUBLIC_ALLOWLIST.json`
- `knowledge-library/architecture-decisions/github-obsidian-quartz-knowledge-access.md`
- `scripts/sync-public-library-to-quartz.ps1`
