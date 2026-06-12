# Navigable Summary Linking Standard

## Purpose

Ensure that project summaries, registries, project cards, handoff documents, document indexes, and secretary-mode navigation pages are useful as navigation surfaces, not just as prose.

## Core Rule

Whenever an accessible source can be linked, use a clickable link instead of a bare repository name, file path, project name, or document title.

A summary is incomplete when it mentions a source but does not provide the available navigation link.

## Required Link Set For Project Summaries

For each project, include the available subset of:

- GitHub repository URL;
- `START_HERE.md` or project entrypoint URL;
- `PROJECT.md` URL;
- `PROJECT_STATE.md` URL;
- `logs/latest.md` URL;
- linked Notion project page;
- linked Google Drive folder or file when safe and available;
- linked related project pages;
- linked official external sources when they are part of the project truth map;
- linked issue or PR thread when it is the active execution channel.

Do not invent links. Include only verified URLs.

## Local Paths

When a source is local-only and cannot be represented by a safe clickable link, include the exact path in a separate code block.

Example:

```text
C:\Users\<user>\Documents\Project
```

## Related Documents

When a project has related pages or documents, add a short linked section such as:

```text
Related:
- [Project state](...)
- [Latest log](...)
- [Notion project card](...)
- [Active execution issue](...)
```

## Master Index Rule

A master project registry must function as a clickable navigation index. It should allow direct movement to the project repository, entrypoint, current state, latest log, and related management page whenever those sources exist.

## Boundary

Do not expose secrets, private tokens, sensitive banking identifiers, private document contents, or unsafe local paths merely to increase link density.

## Final Rule

Prefer navigable documents over descriptive-only documents. Every summary should minimize the number of clicks needed to reach the source of truth.