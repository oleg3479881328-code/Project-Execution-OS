# Knowledge Library Portal Publishing Boundary

## Rule

Quartz receives content only from `docs/KNOWLEDGE_LIBRARY_PUBLIC_ALLOWLIST.json`.

The sync script copies only listed files into the Quartz `content/` folder.

Do not publish the whole repository by default.

## Default Exclusions

Keep these areas outside the portal unless separately reviewed:

- `docs/`
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

## Review Rule

Before adding a file to the allowlist, confirm that its content and links are appropriate for browser access.

## Rollback

Remove the file from the allowlist, run the sync script again, and rebuild Quartz.
