# ChatGPT Workspace Manager — Stable Extension Identity

## Decision

Starting with v0.1.4, the private unpacked extension uses a pinned manifest `key` so Chrome derives the same extension ID regardless of which folder the unpacked build is loaded from.

Expected stable Chrome extension ID:

`ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`

## Why

Before v0.1.4, each version was commonly extracted into a different folder and loaded as a fresh unpacked extension. Chrome can therefore assign a different unpacked extension origin/ID, which also means a different extension IndexedDB origin. The browser acceptance run exposed the consequence: metadata could be re-synced, but locally hydrated messages and owner-only metadata from an earlier installation were not present in the new installation.

## Rule

- Do not change the manifest `key` unless intentionally creating a new extension identity.
- Treat the `key` as public identity material, not a secret.
- Future unpacked builds may be loaded from different folders while retaining the same extension ID.
- The transition to v0.1.4 is a one-time identity reset from prior path-derived development IDs.
- After v0.1.4, owner-local IndexedDB state is expected to survive normal version updates as long as Chrome recognizes the same pinned extension ID.

## Acceptance

1. Load v0.1.4 and confirm Chrome reports extension ID `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa`.
2. Sync conversations, hydrate one conversation, create a test favorite/note.
3. Load a later build from a different folder.
4. Confirm the extension ID remains `ejpgnlcdfbbjkhlnbfonplngcfcjmbaa` and the local data is still present.
