---
status: in-progress
project_mode: compact
last_updated: 2026-09-06
next_action: Install v0.1.5 Update-Safe in one permanent folder, validate Backup/Restore and update persistence in Chrome, then begin Slice 2 bulk operations.
---

# ChatGPT Workspace Manager — Project State

Date: 2026-09-06

## Current Phase

`Slice 1 implemented and browser-validated; update-safety layer machine-validated in v0.1.5`

## Product Direction

Build a private owner-operated ChatGPT control center as an unpacked Chrome extension.

The architecture is modular and local-first:

- WXT + TypeScript + React + Manifest V3;
- persistent Side Panel operator UI;
- ChatGPT-specific behavior isolated behind `ChatGPTAdapter`;
- IndexedDB/Dexie local workspace;
- ChatGPT owns provider/platform state;
- local DB owns cache, favorites, notes, owner metadata, snapshots, indexes and operation history;
- two-stage sync: metadata first, content hydration on demand;
- no telemetry, analytics or vendor backend.

## Browser-Validated Slice 1

Confirmed on the owner's real ChatGPT account:

- self-healing content bridge works on already-open ChatGPT tabs;
- live metadata sync returned 1051 conversations;
- long conversation hydration succeeded with 583 messages;
- second conversation hydration succeeded with 15 messages;
- owner favorite persisted across navigation;
- local note persisted across navigation;
- local DB/search remain healthy during controlled Offline test mode;
- Health evidence bookkeeping distinguishes passive UNKNOWN from validated HEALTHY/UNAVAILABLE results.

## Update-Safety Decision

Starting with v0.1.4 the manifest has a pinned public key producing stable extension ID:

`ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`

Starting with v0.1.5 the update contract is stronger:

- use one permanent install folder;
- never use `Remove` for routine updates;
- replace build files in place and press `Reload` in `chrome://extensions`;
- use `unlimitedStorage` for the large IndexedDB-backed workspace;
- use built-in full Workspace Backup/Restore;
- Restore validates input, asks for confirmation and downloads a pre-restore safety backup before replacing local data.

## v0.1.5 Machine Validation

GitHub Actions validation passed:

- dependency install: PASS;
- TypeScript: PASS;
- 12 unit tests across 3 files: PASS;
- stable extension identity derivation: PASS;
- backup export/restore/validation tests: PASS;
- WXT production build: PASS;
- unpacked artifact upload: PASS.

## Active Files

- `PROJECT.md`
- `PROJECT_STATE.md`
- `TECHNICAL_ARCHITECTURE.md`
- `DONOR_CAPABILITY_MATRIX.md`
- `EXTENSION_IDENTITY.md`
- `UPDATE_SAFETY.md`
- `logs/latest.md`
- `src/core/db.ts`
- `src/core/backup.ts`
- `src/core/extension-identity.ts`
- `src/providers/chatgpt/`
- `entrypoints/sidepanel/`
- `tests/`

## Explicitly Deferred Until Slice 2

- bulk selection;
- archive queue;
- delete queue;
- destructive-operation snapshot plan;
- pause/resume/cancel;
- per-item verification and operation log;
- rate-limit pause behavior.

## Next Practical Step

1. Install v0.1.5 into one permanent folder, recommended `C:\ChatGPT-Workspace-Manager\`.
2. Confirm stable ID `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
3. Sync and hydrate at least one conversation; create a test favorite/note.
4. Export Workspace backup.
5. Validate restore using the exported backup.
6. Validate a subsequent in-place update by replacing files and pressing `Reload` without `Remove`.
7. If local data survives, close Slice 1/update-safety acceptance and begin Slice 2.
