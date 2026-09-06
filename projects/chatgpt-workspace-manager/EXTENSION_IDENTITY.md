# ChatGPT Workspace Manager — Stable Extension Identity

## Decision

Starting with v0.1.4, the private unpacked extension uses a pinned manifest `key` so Chrome derives the same extension ID for every build.

Expected stable Chrome extension ID:

`ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`

## Important distinction

A stable ID protects the extension origin across builds, but it does **not** make uninstall/reinstall a safe update procedure. Removing an extension can remove its extension-owned local storage. Therefore the update contract is stricter than “same ID”.

## Frozen update rule starting with v0.1.5

1. Keep one permanent install directory, recommended:
   `C:\ChatGPT-Workspace-Manager\`
2. Load that directory once with `Load unpacked`.
3. Before an update, use `Health -> Backup workspace`.
4. Extract the new build to a temporary directory.
5. Copy/replace the new build files into the same permanent install directory.
6. Open `chrome://extensions` and press `Reload` on ChatGPT Workspace Manager.
7. Never use `Remove` for a routine version update.

The pinned manifest key remains a second line of protection against accidental ID drift.

## Storage protection

Starting with v0.1.5 the manifest also requests `unlimitedStorage` because this owner tool may keep a large IndexedDB cache and future search indexes.

The extension also provides full Workspace Backup/Restore:

- provider conversation metadata;
- hydrated/cached messages;
- favorites, notes and owner metadata;
- settings except transient Offline test state;
- capability/health history.

Restore validates the backup before replacing the database and downloads a pre-restore safety backup of the current Workspace first.

## Acceptance

1. Install v0.1.5 from the permanent folder and confirm ID `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
2. Sync conversations, hydrate one conversation, add a favorite and note.
3. Export Workspace backup.
4. Update a later build by replacing files in the same permanent folder and pressing `Reload`, without `Remove`.
5. Confirm ID, local metadata and hydrated messages remain present.
6. Restore the exported backup into a disposable/test state and confirm data round-trips correctly.
