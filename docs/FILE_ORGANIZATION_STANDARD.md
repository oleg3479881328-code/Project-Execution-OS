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

## Global Google Drive Persistence Rule

Chat, model memory, temporary runtime storage, and local session folders are not durable file storage.

Whenever work produces a file or package that has continuing value and another human or AI executor may need later, preserve a durable copy in Google Drive before treating the work as safely retained.

This rule applies globally across Project Execution OS, not only to a specific project.

Examples include:

- ZIP archives and export packages;
- design extracts and evidence packages;
- generated documents, spreadsheets, presentations, PDFs, images, audio, and video;
- technical specifications and migration packages when a file copy matters;
- source bundles, backups, snapshots, and reproducibility artifacts;
- uploaded reference files that become important to ongoing work.

Storage routing:

1. Project-specific durable files belong inside that project's Google Drive folder tree.
2. Cross-project, reusable, infrastructure, or system-wide artifacts belong under the global `System Artifacts` folder.
3. The global `System Artifacts` folder is: `https://drive.google.com/drive/folders/17HCaGyRQsauU5f5r9HwnCksOr4IlV4t_`.
4. Do not duplicate a file into both locations without a real reason. Prefer one canonical Drive copy plus durable links from Notion, GitHub, or project entrypoints.
5. Text or code whose canonical source is GitHub or Notion may remain canonical there, but any valuable generated/downloadable file artifact must not exist only in chat or temporary runtime storage.

The executor should perform this persistence step proactively. The owner should not need to say “save this to Drive” each time.

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
3. route reusable or system-wide artifacts under the global `System Artifacts` folder;
4. if the correct destination is still unclear, ask the owner before creating a persistent file;
5. do not silently fall back to the root of Drive or another random location.

## Tool Limitation Rule

If the available connector or tool cannot create or move a file into the correct destination:

1. do not silently scatter the file elsewhere;
2. state the limitation clearly;
3. ask the owner for the minimum manual action required, or provide a temporary local artifact explicitly marked as temporary;
4. continue only after the canonical destination is clear.

## Temporary Workspace Rule

A runtime workspace such as `/mnt/data` may be used for temporary generation, validation, conversion, or download delivery.

Files in a temporary runtime workspace are not canonical storage. When a durable copy is needed, place it into the correct persistent Google Drive folder before treating the artifact as safely preserved, or explicitly tell the owner that only a temporary copy exists because persistence was technically blocked.

## Final Rule

Create deliberately. Store canonically. Persist valuable file artifacts to Google Drive. Keep folders clean. Do not spread files around.