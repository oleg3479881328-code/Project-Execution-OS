import { afterAll, beforeEach, describe, expect, it } from 'vitest';
import {
  createWorkspaceBackup,
  restoreWorkspaceBackup,
  validateWorkspaceBackup,
  WORKSPACE_BACKUP_FORMAT,
  WORKSPACE_BACKUP_VERSION
} from '../src/core/backup';
import { DB_SCHEMA_VERSION, db, getSetting } from '../src/core/db';
import type { CanonicalMessage, OwnerConversationMetadata, ProviderConversation } from '../src/core/models';

const conversation: ProviderConversation = {
  provider: 'chatgpt',
  id: 'conv-1',
  title: 'Workspace backup test',
  updatedAt: 1_700_000_000_000,
  archived: false,
  contentHydrated: true,
  messageCount: 1,
  lastSyncedAt: 1_700_000_000_000,
  lastHydratedAt: 1_700_000_000_000
};

const message: CanonicalMessage = {
  key: 'conv-1:msg-1',
  provider: 'chatgpt',
  conversationId: 'conv-1',
  id: 'msg-1',
  index: 0,
  role: 'user',
  textPlain: 'Keep this cached message',
  source: 'live-api',
  capturedAt: 1_700_000_000_000
};

const owner: OwnerConversationMetadata = {
  conversationId: 'conv-1',
  folderIds: [],
  tagIds: ['important'],
  favorite: true,
  pinned: false,
  note: 'Keep this private note',
  bookmarkIds: [],
  updatedAt: 1_700_000_000_000
};

beforeEach(async () => {
  await db.delete();
  await db.open();
  await db.conversations.put(conversation);
  await db.messages.put(message);
  await db.ownerMetadata.put(owner);
  await db.settings.bulkPut([
    { key: 'lastSync', value: { received: 1051, upserted: 1051 }, updatedAt: 100 },
    { key: 'offlineMode', value: true, updatedAt: 200 }
  ]);
  await db.capabilities.add({
    capability: 'list-conversations',
    status: 'healthy',
    strategy: 'live-api',
    checkedAt: 300,
    message: 'Validated by sync.'
  });
});

afterAll(async () => {
  await db.delete();
});

describe('update-safe Workspace backup and restore', () => {
  it('exports the full local workspace while excluding transient Offline test state', async () => {
    const backup = await createWorkspaceBackup('0.1.5');

    expect(backup.format).toBe(WORKSPACE_BACKUP_FORMAT);
    expect(backup.formatVersion).toBe(WORKSPACE_BACKUP_VERSION);
    expect(backup.dbSchemaVersion).toBe(DB_SCHEMA_VERSION);
    expect(backup.extensionVersion).toBe('0.1.5');
    expect(backup.data.conversations).toHaveLength(1);
    expect(backup.data.messages).toHaveLength(1);
    expect(backup.data.ownerMetadata[0]?.favorite).toBe(true);
    expect(backup.data.ownerMetadata[0]?.note).toBe('Keep this private note');
    expect(backup.data.settings.some((item) => item.key === 'lastSync')).toBe(true);
    expect(backup.data.settings.some((item) => item.key === 'offlineMode')).toBe(false);
    expect(backup.data.capabilities).toHaveLength(1);
    expect('id' in backup.data.capabilities[0]!).toBe(false);
  });

  it('restores messages and owner metadata transactionally and forces Offline test off', async () => {
    const backup = await createWorkspaceBackup('0.1.5');

    await db.conversations.clear();
    await db.messages.clear();
    await db.ownerMetadata.clear();
    await db.settings.clear();
    await db.capabilities.clear();
    await db.conversations.put({ ...conversation, id: 'other', title: 'Temporary replacement' });

    const counts = await restoreWorkspaceBackup(backup);

    expect(counts).toEqual({ conversations: 1, messages: 1, ownerMetadata: 1 });
    expect((await db.conversations.get('conv-1'))?.title).toBe('Workspace backup test');
    expect((await db.conversations.get('other'))).toBeUndefined();
    expect((await db.messages.get('conv-1:msg-1'))?.textPlain).toBe('Keep this cached message');
    expect((await db.ownerMetadata.get('conv-1'))?.favorite).toBe(true);
    expect((await db.ownerMetadata.get('conv-1'))?.note).toBe('Keep this private note');
    expect(await getSetting<boolean>('offlineMode')).toBe(false);
    expect(await getSetting('lastSync')).toEqual({ received: 1051, upserted: 1051 });
    expect(await getSetting('lastRestore')).toBeTruthy();
  });

  it('rejects wrong formats and backups from a newer DB schema before touching the database', () => {
    expect(() => validateWorkspaceBackup({ format: 'something-else' })).toThrow('BACKUP_FORMAT_UNSUPPORTED');

    expect(() =>
      validateWorkspaceBackup({
        format: WORKSPACE_BACKUP_FORMAT,
        formatVersion: WORKSPACE_BACKUP_VERSION,
        exportedAt: new Date().toISOString(),
        extensionVersion: '9.9.9',
        dbSchemaVersion: DB_SCHEMA_VERSION + 1,
        data: {
          conversations: [],
          messages: [],
          ownerMetadata: [],
          settings: [],
          capabilities: []
        }
      })
    ).toThrow('BACKUP_DB_NEWER');
  });
});
