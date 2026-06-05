# Knowledge Library Portal Publishing Boundary

## Purpose

This file defines what the Quartz portal is allowed to expose from `Project-Execution-OS`.

## Default Rule

Only files named in `docs/KNOWLEDGE_LIBRARY_PUBLIC_ALLOWLIST.json` may be copied into the Quartz portal.

No other repository path is publishable by default.

## Safe Starter Scope

The starter allowlist is intentionally small:

- `knowledge-library/README.md`
- `knowledge-library/PROJECT_INDEX.md`
- selected entries under `knowledge-library/patterns/`
- the architecture decision for the access layer itself

## Explicitly Forbidden By Default

Do not publish these areas unless they are separately reviewed and added to the allowlist:

- `docs/` in general;
- `logs/`
- `projects/`
- `project-library/`
- `agent-library/`
- `agent-modules/`
- `blocks/`
- `skills/`
- `workflow-templates/`
- `.github/`
- `.obsidian/`
- any future folder that has not been explicitly reviewed

## Safety Model

The safety control is structural rather than trust-based:

1. the main repository stays the authoring source;
2. the Quartz portal reads from its own `content/` folder only;
3. the sync script rebuilds that `content/` folder from the reviewed allowlist;
4. anything not copied cannot be published by Quartz.

## Review Rule

Before adding a new file or folder to the allowlist, confirm:

- the content is safe for browser publication;
- the file does not contain internal-only operating details that should stay private;
- linked files are also safe, or links are removed or rewritten;
- the destination path in Quartz is intentional.

## Rollback

Rollback is straightforward:

- remove the file from `docs/KNOWLEDGE_LIBRARY_PUBLIC_ALLOWLIST.json`;
- run `scripts/sync-public-library-to-quartz.ps1` again;
- rebuild the Quartz portal.
