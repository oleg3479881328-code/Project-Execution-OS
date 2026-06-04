# GitHub + Obsidian + Quartz Knowledge Access Pattern

Type: architecture-decision
Lifecycle status: active
Review status: approved for reuse
Date: 2026-06-04

## Problem

Markdown knowledge stored in GitHub is durable and agent-friendly but inconvenient for everyday human reading, browsing, and lightweight editing.

Building a custom knowledge-library application too early creates unnecessary cost and maintenance burden.

## Approved Pattern

Use a three-layer access model:

`GitHub -> Obsidian -> Quartz`

## Layer Roles

### GitHub

Canonical durable storage, version history, agent writes, and system automation.

### Obsidian

Personal desktop workspace over the same Markdown files for search, navigation, links, tags, graph view, and manual editing.

### Quartz

Browser-readable publication layer over the same Markdown library for search, backlinks, graph exploration, and mobile-friendly access.

## When To Use

Use this pattern when:

- GitHub already stores Markdown knowledge;
- the owner needs a better human interface;
- a custom application is not yet justified;
- read access from phone or browser is useful;
- version control must remain canonical.

## When Not To Use

Reconsider when:

- rich browser editing is mandatory;
- private authenticated publishing is required;
- database-backed workflows are necessary;
- collaboration requirements exceed a lightweight Markdown stack.

## Risks

- Mobile editing remains weaker than desktop editing.
- Quartz is primarily read-oriented.
- Private publishing may require additional hosting configuration.

## Source

Approved during Project Execution OS knowledge-library access discussion on 2026-06-04.

## Related Standards

- `docs/KNOWLEDGE_LIBRARY_ACCESS_ARCHITECTURE.md`
- `docs/KNOWLEDGE_SYSTEM.md`
- `docs/AUTOMATIC_CAPTURE_STANDARD.md`
