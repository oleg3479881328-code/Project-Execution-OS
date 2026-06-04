# Knowledge Library Access Architecture

Status: Approved system direction
Date: 2026-06-04

## Purpose

Define how the owner should access and use the Project Execution OS knowledge library without building a custom interface from scratch.

## Decision

Use the following architecture:

`GitHub -> Obsidian -> Quartz`

## Roles

### GitHub

GitHub remains the canonical source of truth for durable knowledge files.

It is the storage and version-history layer used by agents and system automation.

### Obsidian

Obsidian is the owner's personal working interface for the same Markdown files.

The local clone of the Project Execution OS repository can be opened as an Obsidian vault.

This provides:

- folder navigation;
- full-text search;
- tags;
- internal links;
- graph view;
- manual editing when needed.

### Quartz

Quartz is the read-oriented web interface for the same Markdown knowledge base.

It should publish the library as a browser-accessible site with:

- navigation;
- search;
- backlinks;
- graph-style exploration;
- mobile-friendly access.

## Operating Model

1. Agents write durable knowledge into GitHub.
2. The owner opens the repository in Obsidian for personal work.
3. Quartz publishes the readable browser version.
4. GitHub remains the source of truth.
5. Do not create a custom knowledge-library application unless this stack proves insufficient.

## Mobile Rule

Use Quartz first for reading and search from a phone.

Do not rely on mobile Git workflows as the primary capture path.

The owner can ask an agent to capture knowledge through the GitHub connector.

## Deferred Alternatives

Do not implement now:

- a custom web app;
- Wiki.js;
- heavy database-backed knowledge management;
- complex mobile Git synchronization.

These may be reconsidered only if the approved lightweight stack becomes insufficient.

## Trigger For Reconsideration

Revisit this architecture only if one of the following becomes a real blocker:

- browser editing is required;
- private authenticated publishing becomes necessary;
- mobile editing becomes a daily need;
- Quartz search or navigation is insufficient;
- knowledge scale requires a database-backed layer.

## Related Standards

- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/RESEARCH_STANDARD.md`
