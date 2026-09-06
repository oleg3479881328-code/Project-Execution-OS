# ChatGPT Workspace Manager — Latest State

## Date

2026-09-06

## Current Status

Architecture accepted. Slice 1 is implemented and browser-validated on the owner's real ChatGPT account. The v0.1.5 Update-Safe layer is implemented and machine-validated; final Chrome acceptance is pending.

## Browser Acceptance Already Passed

- self-healing content bridge works without reloading an already-open ChatGPT tab;
- live metadata sync returned 1051 conversations;
- `ChatGPT Workspace Manager` hydrated 583 messages;
- `Домен Vercel обсудить` hydrated 15 messages;
- favorites and local notes persisted across normal conversation navigation;
- controlled Offline test blocks live ChatGPT calls while local DB/search remain healthy;
- Health bookkeeping no longer lets passive UNKNOWN hide prior validated results;
- Offline-test synthetic UNAVAILABLE evidence is ignored after Offline test is disabled.

## Important Lifecycle Finding

Browser testing across multiple unpacked version folders showed that local metadata could be re-synced while hydrated message cache and owner-only test data from an earlier installation were not present in the next installation.

The important correction is:

- stable manifest identity is necessary but not sufficient;
- routine updates must not use Chrome `Remove`;
- the production owner workflow must preserve the installed extension and update it in place.

## Stable Identity

Starting with v0.1.4 the manifest contains a pinned public `key`.

Frozen Chrome extension ID:

`ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`

A unit test derives the Chrome ID from the pinned public key and prevents accidental identity drift.

## v0.1.5 Update-Safe — IMPLEMENTED

### Permanent update contract

- keep one permanent folder, recommended `C:\ChatGPT-Workspace-Manager\`;
- load that folder once using `Load unpacked`;
- before a routine update, export a Workspace backup;
- copy/replace new build files into that same folder;
- press `Reload` in `chrome://extensions`;
- never press `Remove` for a routine update.

### Storage protection

The manifest now requests `unlimitedStorage` in addition to:

- `storage`;
- `sidePanel`;
- `activeTab`;
- `scripting`.

Host permissions remain limited to ChatGPT domains.

### Full Workspace Backup

Health now includes `Backup workspace`.

Backup JSON contains:

- provider conversation metadata;
- hydrated/cached messages;
- favorites, notes and owner metadata;
- persistent settings except transient Offline test state;
- capability/health history.

The backup contains private conversation content when chats have been hydrated and must be stored privately.

### Full Workspace Restore

Health now includes `Restore backup`.

Restore flow:

1. parse JSON;
2. validate backup format/version/schema and minimum record identities;
3. show record counts and require explicit confirmation;
4. export a pre-restore safety backup of the current Workspace;
5. transactionally replace conversations/messages/owner metadata/settings/capabilities;
6. force Offline test mode off;
7. record restore metadata;
8. reload the Side Panel.

Invalid backup input is rejected before the database is modified.

## v0.1.5 Machine Validation

GitHub Actions `ChatGPT Workspace Manager CI` passed on 2026-09-06:

- dependency install: PASS;
- TypeScript: PASS;
- test files: 3 passed;
- unit tests: 12 passed;
  - identity: 1;
  - Slice 1: 8;
  - Backup/Restore: 3;
- WXT production build: PASS;
- unpacked artifact upload: PASS.

Build output size: approximately 324 KB unpacked.

## Project Execution OS Integrity

The first v0.1.5 validation PR exposed project-registration debt rather than extension-code failure:

- missing `projects/chatgpt-workspace-manager/PROJECT_STATE.md`;
- missing ChatGPT Workspace Manager route in `projects/ROUTER.md`.

Both are now corrected. A fresh validation run is required to prove the overall Project Execution OS gate is green.

## Canonical Project Files

- `PROJECT.md`
- `PROJECT_STATE.md`
- `TECHNICAL_ARCHITECTURE.md`
- `DONOR_CAPABILITY_MATRIX.md`
- `EXTENSION_IDENTITY.md`
- `UPDATE_SAFETY.md`
- `logs/latest.md`

## Current Acceptance Boundary

Do not start destructive bulk archive/delete implementation until v0.1.5 passes the final owner-browser update-safety test.

## Next Browser Acceptance

1. Create permanent folder `C:\ChatGPT-Workspace-Manager\`.
2. Install v0.1.5 from that folder and confirm ID `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
3. Sync metadata and hydrate one conversation.
4. Add one favorite and one local note.
5. Export `Backup workspace`.
6. Enable Offline test and verify the hydrated conversation renders from local cache.
7. Disable Offline test.
8. Validate `Restore backup` using the exported file.
9. On the next build, replace files in the same permanent folder and press `Reload` without `Remove`.
10. Confirm local cache, favorite, note and stable ID survive the update.
11. After this proof, close Slice 1/update-safety and begin Slice 2.
