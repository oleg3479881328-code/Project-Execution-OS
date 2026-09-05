import { afterAll, beforeEach, describe, expect, it } from 'vitest';
import {
  DB_SCHEMA_VERSION,
  db,
  getWorkspaceConversations,
  updateOwnerMetadata,
  upsertConversationMetadata
} from '../src/core/db';
import { normalizeConversation } from '../src/providers/chatgpt/api-strategy';
import { errorResponse } from '../src/providers/chatgpt/protocol';

beforeEach(async () => {
  await db.delete();
  await db.open();
});

afterAll(async () => {
  await db.delete();
});

describe('Slice 1 canonicalization and local workspace', () => {
  it('normalizes provider metadata with stable millisecond timestamps', () => {
    const syncedAt = 2_000_000_000_000;
    const normalized = normalizeConversation(
      {
        id: 'conv-1',
        title: '  Example chat  ',
        create_time: 1_700_000_000,
        update_time: 1_700_000_010,
        is_archived: true
      },
      syncedAt
    );

    expect(normalized).not.toBeNull();
    expect(normalized?.id).toBe('conv-1');
    expect(normalized?.title).toBe('Example chat');
    expect(normalized?.createdAt).toBe(1_700_000_000_000);
    expect(normalized?.updatedAt).toBe(1_700_000_010_000);
    expect(normalized?.archived).toBe(true);
    expect(normalized?.contentHydrated).toBe(false);
  });

  it('keeps owner metadata when provider metadata is synced again', async () => {
    const first = normalizeConversation({ id: 'conv-1', title: 'First title', update_time: 100 }, 1_000)!;
    await upsertConversationMetadata([first]);
    await updateOwnerMetadata('conv-1', { favorite: true, note: 'Keep this note' });

    const refreshed = normalizeConversation({ id: 'conv-1', title: 'Updated title', update_time: 200 }, 2_000)!;
    await upsertConversationMetadata([refreshed]);

    const [workspace] = await getWorkspaceConversations();
    expect(workspace?.title).toBe('Updated title');
    expect(workspace?.owner.favorite).toBe(true);
    expect(workspace?.owner.note).toBe('Keep this note');
  });

  it('opens the expected Dexie schema version', async () => {
    expect(db.isOpen()).toBe(true);
    expect(db.verno).toBe(DB_SCHEMA_VERSION);
  });

  it('filters cached conversations locally by title', async () => {
    await upsertConversationMetadata([
      normalizeConversation({ id: 'a', title: 'Vercel migration', update_time: 300 }, 3_000)!,
      normalizeConversation({ id: 'b', title: 'CDL vocabulary', update_time: 200 }, 3_000)!,
      normalizeConversation({ id: 'c', title: 'Wedding publication', update_time: 100 }, 3_000)!
    ]);

    const result = await getWorkspaceConversations('vercel');
    expect(result).toHaveLength(1);
    expect(result[0]?.id).toBe('a');
  });

  it('sanitizes bearer tokens and JWT-like strings from diagnostics errors', () => {
    const response = errorResponse(
      new Error('LIST_HTTP_401 Bearer super-secret-token eyJhbGciOiJIUzI1NiJ9.payload.signature')
    );

    expect(response.ok).toBe(false);
    if (!response.ok) {
      expect(response.error).not.toContain('super-secret-token');
      expect(response.error).not.toContain('eyJhbGci');
      expect(response.error).toContain('[redacted]');
      expect(response.diagnosticCode).toBe('LIST_HTTP_401');
    }
  });
});
