# GitHub Obsidian Quartz Knowledge Access

## Status

approved

## Decision

Use:

`GitHub -> Obsidian -> Quartz`

for the first knowledge-library access layer.

## Context

The knowledge library already lives in versioned Markdown inside `Project-Execution-OS`.

The owner needs:

- one local editing surface over the same files;
- one browser-readable interface for approved public-facing knowledge;
- a path that does not accidentally expose the whole repository.

## Chosen Structure

- `GitHub` remains the versioned source of truth.
- `Obsidian` opens the local repository folder directly as a vault.
- `Quartz` lives in a separate portal scaffold and receives only copied allowlisted files.

## Why This Was Chosen

- It reuses plain Markdown instead of introducing a second knowledge store.
- It matches Quartz's native content model around a dedicated `content/` folder.
- It keeps the publication step reviewable and reversible.
- It postpones custom application work until the lightweight stack proves insufficient.

## Constraints

- whole-repository publication is forbidden by default;
- local preview comes before public deployment;
- allowlist sync is required for portal input;
- no credentials or secrets may be introduced.

## Consequences

- published content is a curated subset, not an automatic mirror;
- the owner edits canonical files in the main repository, then resyncs;
- the Quartz portal can be replaced later without rewriting the underlying library.
