# Notion Database Schema

## Purpose

Define the baseline Notion database schema for an agent-compatible Project Execution OS workspace.

## Design Rule

Prefer simple properties that agents can read and write reliably.

Avoid decorative formulas and complex relations until repeated use proves they reduce real work.

## Projects Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — stable text or unique ID.
- `Status` — idea, candidate, active, paused, archived, deprecated.
- `Project Type` — app, workflow, content, research, system, legal, personal, other.
- `Current Mode` — new, continue, review, research, execution, handoff, archive.
- `Owner` — people or text.
- `Project Entrypoint` — URL.
- `GitHub Repo` — URL.
- `Drive Folder` — URL.
- `Bublup Folder` — URL.
- `Telegram Channel` — URL.
- `Active Layers` — multi-select.
- `Truth Map` — rich text.
- `Next Practical Step` — rich text.
- `Last Agent Touch` — date.
- `Needs Review` — checkbox.

## Tasks Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation to Projects.
- `Status` — backlog, ready, in progress, blocked, review, done, canceled.
- `Priority` — low, medium, high, urgent.
- `Task Type` — research, design, implementation, review, bug, decision, handoff, admin.
- `Assignee Agent` — text or people.
- `Due` — date.
- `GitHub Issue` — URL.
- `Codex Handoff` — URL.
- `Blocked By` — rich text or relation.
- `Definition of Done` — rich text.
- `Output URL` — URL.
- `Needs Review` — checkbox.

## Research Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `Research Question` — rich text.
- `Source Type` — official, vendor, open-source, professional, community, anecdotal.
- `Source URL` — URL.
- `Date Checked` — date.
- `Freshness Risk` — low, medium, high.
- `Finding` — rich text.
- `Actionability` — candidate, validated, rejected, monitor.
- `Related Task` — rich text or relation.

## Decisions Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `Decision Status` — proposed, accepted, rejected, superseded.
- `Decision Date` — date.
- `Context` — rich text.
- `Decision` — rich text.
- `Rationale` — rich text.
- `Consequences` — rich text.
- `GitHub Evidence` — URL.
- `Needs Review` — checkbox.

## Assets Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `Asset Type` — file, image, video, prompt, design, dataset, credential-pointer, external-link.
- `Location` — URL.
- `Storage Layer` — GitHub, Notion, Google Drive, Bublup, local, other.
- `Usage Rights` — owned, licensed, public, unknown, restricted.
- `Related Task` — rich text or relation.

## Links Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `URL` — URL.
- `Link Type` — official, tool, repo, article, video, competitor, template, reference.
- `Why It Matters` — rich text.
- `Date Checked` — date.

## Logs Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `Log Type` — agent run, owner note, meeting, handoff, error, sync.
- `Timestamp` — date.
- `Agent Author` — text or people.
- `Summary` — rich text.
- `Next Action` — rich text.
- `Evidence URL` — URL.

## Knowledge Extracted Database

Required properties:

- `Name` — title.
- `PROJECT_ID` — text or relation.
- `Knowledge Type` — reusable rule, pattern, source, warning, prompt, workflow.
- `Candidate Text` — rich text.
- `Promotion Status` — captured, researched, candidate, reviewed, active, rejected, retired.
- `Target Location` — rich text or URL.
- `Needs Review` — checkbox.

## Initial MVP Rule

Start with all eight databases, but use text `PROJECT_ID` fields first.

Add relations only after the first practical test confirms that they improve navigation without making agent writes fragile.

## Final Rule

The schema succeeds only when different agents can use it consistently without losing project identity or confusing layer-specific truth.