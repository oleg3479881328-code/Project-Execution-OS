# Source Traceability Standard

## Purpose

This standard prevents orphaned notes, cards, project records, and saved research from becoming impossible to verify later.

Any saved knowledge must include a durable way to find the source again.

## Core Rule

Every card, project entrypoint, saved idea, research note, handoff packet, or durable project artifact must include at least one explicit source pointer.

A source pointer can be:

- a direct URL;
- a repository path;
- a Notion page URL;
- a Google Drive file URL;
- an attached file link;
- a local artifact path plus checksum when no external URL exists;
- a source list with filenames and hashes;
- a citation to the exact file or document location.

If the source cannot be opened or recovered from the artifact, the artifact is incomplete.

## Required Source Block

Every durable card or project artifact should include a compact block named one of:

- `Source`
- `Sources`
- `Source Trail`
- `Исходник`
- `Источники`
- `След источника`

The block must answer:

1. What was the original source?
2. Where can it be opened?
3. If it was generated from files, what files were used?
4. If a raw package exists, where is it stored?
5. If a raw package cannot be externally linked, what checksum identifies it?

## Minimum Acceptable Source Pointer

At least one of these must be present:

```text
source_url: <openable URL>
```

or

```text
source_file: <filename>
source_location: <repo path, Drive URL, Notion URL, or sandbox artifact path>
sha256: <checksum>
```

or

```text
sources:
  - title: <source title>
    url: <openable URL>
    captured_at: <date>
```

## Raw Package Rule

If a saved card says that a full package, archive, raw file, source bundle, attachment, or research pack exists, the card must include a direct path or URL to that package.

Do not write only:

```text
Full package saved separately.
```

Write instead:

```text
Full package: <URL or repo path or Drive file URL>
SHA256: <checksum>
```

If upload failed or no durable external file exists, say explicitly:

```text
Full package was generated in the chat workspace only and is not yet stored in a durable external system.
```

## Failure Rule

If an artifact lacks source links, do not present it as fully saved.

Say:

```text
Saved summary only. Source package is not durably linked yet.
```

Then either attach/upload the source package or record the missing-link gap as a follow-up problem.

## Applies To

This standard applies to:

- Notion cards;
- GitHub cards;
- Reference-Idea-Library records;
- Project Execution OS project files;
- PROJECT.md;
- PROJECT_STATE.md;
- Codex handoff packets;
- research summaries;
- saved prompts and prompt libraries;
- any durable knowledge entry created for the owner.

## Final Rule

No source trail, no durable knowledge.

A saved card without a recoverable source is not complete.