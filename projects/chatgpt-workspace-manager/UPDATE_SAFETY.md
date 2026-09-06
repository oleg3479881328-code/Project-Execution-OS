# ChatGPT Workspace Manager — Update-Safe Owner Procedure

## Permanent installation

Use one permanent local directory for the unpacked extension, recommended:

`C:\ChatGPT-Workspace-Manager\`

Load this directory once in `chrome://extensions` with Developer mode enabled and `Load unpacked`.

Expected extension ID from v0.1.4 onward:

`ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`

## Routine update

Do **not** remove the extension.

1. In ChatGPT Workspace Manager open `Health`.
2. Click `Backup workspace` and keep the JSON file.
3. Download the new CI ZIP.
4. Extract it to a temporary directory.
5. Copy all extracted build files into `C:\ChatGPT-Workspace-Manager\`, replacing the old build files.
6. Open `chrome://extensions`.
7. Press `Reload` on ChatGPT Workspace Manager.
8. Confirm the version changed and the extension ID is still `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
9. Confirm local conversations, favorites, notes and previously hydrated previews still exist.

## Never do this for a normal update

- Do not click `Remove`.
- Do not clear extension site data.
- Do not create a second everyday installation of the same tool.

## Workspace backup

`Backup workspace` exports a local JSON snapshot containing:

- conversation metadata;
- hydrated messages cached in IndexedDB;
- owner-local favorites, notes, folders/tags fields and bookmarks fields;
- persistent settings except transient Offline test mode;
- capability/health history.

The JSON may contain private ChatGPT content. Keep it private.

## Workspace restore

`Restore backup`:

1. parses and validates the selected JSON before changing the database;
2. rejects unknown backup format/version and backups from a newer DB schema;
3. shows counts and asks for explicit confirmation;
4. downloads a safety backup of the current Workspace;
5. transactionally replaces the local Workspace database;
6. forces Offline test mode off;
7. records restore metadata and reloads the Side Panel.

## Storage policy

Starting with v0.1.5 the extension uses `unlimitedStorage` to protect the IndexedDB-backed owner workspace from ordinary extension storage quota/eviction pressure. This is not a substitute for backups.
