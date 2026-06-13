# File Organization Standard

## Purpose

This is the global file-placement rule for all durable work performed through Project Execution OS.

Its purpose is simple: do not create a mess. Every persistent artifact must be placed deliberately and cleanly.

## Scope

This standard applies whenever work creates, saves, imports, uploads, exports, copies, or updates a durable artifact in any storage layer, including:

- Google Drive;
- local folders;
- Git repositories and GitHub;
- Notion attachments or linked files;
- generated documents, spreadsheets, presentations, PDFs, images, archives, exports, and backups.

It applies to project work and to non-project work.

## Core Rule

Before creating a durable file, determine its correct destination.

Do not create persistent files in:

- the root of Google Drive;
- the root of a computer or workspace;
- random folders;
- unrelated project folders;
- temporary locations that are later mistaken for canonical storage.

Use the narrowest correct existing folder. If no suitable folder exists, create a logical subfolder inside the correct parent location before creating the file.

## Canonical Placement Rules

1. Keep all files belonging to one project inside that project's folder tree.
2. Use descriptive folder names and descriptive file names.
3. Keep one canonical working version of each document.
4. Store temporary files separately from canonical files.
5. Store exports separately from editable source files.
6. Store backups separately from active working files.
7. Do not create duplicate copies merely for convenience when a link to the canonical file is sufficient.
8. When a file has already been misplaced, move it into the correct folder before continuing normal work.

## Non-Project Work

When a durable artifact does not belong to an existing project:

1. identify the correct general-purpose parent folder;
2. use or create a clearly named subfolder;
3. if the correct destination is unclear, ask the owner before creating a persistent file;
4. do not silently fall back to the root of Drive or another random location.

## Tool Limitation Rule

If the available connector or tool cannot create or move a file into the correct destination:

1. do not silently scatter the file elsewhere;
2. state the limitation clearly;
3. ask the owner for the minimum manual action required, or provide a temporary local artifact explicitly marked as temporary;
4. continue only after the canonical destination is clear.

## Temporary Workspace Rule

A runtime workspace such as `/mnt/data` may be used for temporary generation, validation, conversion, or download delivery.

Files in a temporary runtime workspace are not canonical storage. When a durable copy is needed, place it into the correct persistent folder or explicitly tell the owner that only a temporary downloadable copy exists.

## Final Rule

Create deliberately. Store canonically. Keep folders clean. Do not spread files around.