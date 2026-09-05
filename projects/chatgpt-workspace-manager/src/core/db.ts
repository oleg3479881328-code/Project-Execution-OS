import Dexie, { type Table } from 'dexie';
import type {
  CanonicalMessage,
  CapabilityHealth,
  OwnerConversationMetadata,
  ProviderConversation,
  SettingRecord,
  WorkspaceConversation
} from './models';

export const DB_NAME = 'ChatGPTWorkspaceManagerDB';
export const DB_SCHEMA_VERSION = 1;

export class WorkspaceDB extends Dexie {
  conversations!: Table<ProviderConversation, string>;
  messages!: Table<CanonicalMessage, string>;
  ownerMetadata!: Table<OwnerConversationMetadata, string>;
  capabilities!: Table<CapabilityHealth, number>;
  settings!: Table<SettingRecord, string>;

  constructor() {
    super(DB_NAME);

    this.version(DB_SCHEMA_VERSION).stores({
      conversations: '&id, provider, updatedAt, archived, nativeProjectId, lastSyncedAt',
      messages: '&key, conversationId, index, role, createdAt',
      ownerMetadata: '&conversationId, favorite, pinned, updatedAt',
      capabilities: '++id, capability, status, checkedAt',
      settings: '&key, updatedAt'
    });
  }
}

export const db = new WorkspaceDB();

export function defaultOwnerMetadata(conversationId: string): OwnerConversationMetadata {
  return {
    conversationId,
    folderIds: [],
    tagIds: [],
    favorite: false,
    pinned: false,
    bookmarkIds: [],
    updatedAt: Date.now()
  };
}

export async function upsertConversationMetadata(items: ProviderConversation[]): Promise<number> {
  if (items.length === 0) return 0;
  await db.transaction('rw', db.conversations, db.ownerMetadata, async () => {
    for (const item of items) {
      const existingConversation = await db.conversations.get(item.id);
      await db.conversations.put({
        ...existingConversation,
        ...item,
        contentHydrated: existingConversation?.contentHydrated ?? item.contentHydrated,
        lastHydratedAt: existingConversation?.lastHydratedAt,
        messageCount: existingConversation?.messageCount ?? item.messageCount,
        providerMissing: false
      });

      const existingOwner = await db.ownerMetadata.get(item.id);
      if (!existingOwner) await db.ownerMetadata.add(defaultOwnerMetadata(item.id));
    }
  });
  return items.length;
}

export async function replaceConversationMessages(
  conversationId: string,
  messages: CanonicalMessage[]
): Promise<void> {
  await db.transaction('rw', db.messages, db.conversations, async () => {
    await db.messages.where('conversationId').equals(conversationId).delete();
    if (messages.length) await db.messages.bulkPut(messages);
    await db.conversations.update(conversationId, {
      contentHydrated: true,
      lastHydratedAt: Date.now(),
      messageCount: messages.length
    });
  });
}

export async function getWorkspaceConversations(query = ''): Promise<WorkspaceConversation[]> {
  const conversations = await db.conversations.orderBy('updatedAt').reverse().toArray();
  const normalizedQuery = query.trim().toLocaleLowerCase();
  const filtered = normalizedQuery
    ? conversations.filter((item) => item.title.toLocaleLowerCase().includes(normalizedQuery))
    : conversations;

  return Promise.all(
    filtered.map(async (conversation) => ({
      ...conversation,
      owner: (await db.ownerMetadata.get(conversation.id)) ?? defaultOwnerMetadata(conversation.id)
    }))
  );
}

export async function updateOwnerMetadata(
  conversationId: string,
  patch: Partial<Omit<OwnerConversationMetadata, 'conversationId'>>
): Promise<OwnerConversationMetadata> {
  const current = (await db.ownerMetadata.get(conversationId)) ?? defaultOwnerMetadata(conversationId);
  const next: OwnerConversationMetadata = {
    ...current,
    ...patch,
    conversationId,
    updatedAt: Date.now()
  };
  await db.ownerMetadata.put(next);
  return next;
}

export async function getConversationMessages(conversationId: string): Promise<CanonicalMessage[]> {
  return db.messages.where('conversationId').equals(conversationId).sortBy('index');
}

export async function recordCapabilities(states: CapabilityHealth[]): Promise<void> {
  if (!states.length) return;
  await db.capabilities.bulkAdd(states);
}

export async function latestCapabilities(): Promise<CapabilityHealth[]> {
  const all = await db.capabilities.orderBy('checkedAt').reverse().toArray();
  const seen = new Set<string>();
  const latest: CapabilityHealth[] = [];
  for (const state of all) {
    if (seen.has(state.capability)) continue;
    seen.add(state.capability);
    latest.push(state);
  }
  return latest;
}

export async function setSetting(key: string, value: unknown): Promise<void> {
  await db.settings.put({ key, value, updatedAt: Date.now() });
}

export async function getSetting<T>(key: string): Promise<T | undefined> {
  return (await db.settings.get(key))?.value as T | undefined;
}
