import type {
  CanonicalMessage,
  CapabilityHealth,
  OwnerConversationMetadata,
  ProviderConversation,
  SettingRecord
} from './models';
import { DB_SCHEMA_VERSION, db } from './db';

export const WORKSPACE_BACKUP_FORMAT = 'chatgpt-workspace-manager-backup';
export const WORKSPACE_BACKUP_VERSION = 1;

export interface WorkspaceBackup {
  format: typeof WORKSPACE_BACKUP_FORMAT;
  formatVersion: typeof WORKSPACE_BACKUP_VERSION;
  exportedAt: string;
  extensionVersion: string;
  dbSchemaVersion: number;
  data: {
    conversations: ProviderConversation[];
    messages: CanonicalMessage[];
    ownerMetadata: OwnerConversationMetadata[];
    settings: SettingRecord[];
    capabilities: Array<Omit<CapabilityHealth, 'id'>>;
  };
}

export interface WorkspaceBackupCounts {
  conversations: number;
  messages: number;
  ownerMetadata: number;
}

export async function createWorkspaceBackup(extensionVersion: string): Promise<WorkspaceBackup> {
  const [conversations, messages, ownerMetadata, settings, capabilities] = await Promise.all([
    db.conversations.toArray(),
    db.messages.toArray(),
    db.ownerMetadata.toArray(),
    db.settings.toArray(),
    db.capabilities.toArray()
  ]);

  return {
    format: WORKSPACE_BACKUP_FORMAT,
    formatVersion: WORKSPACE_BACKUP_VERSION,
    exportedAt: new Date().toISOString(),
    extensionVersion,
    dbSchemaVersion: DB_SCHEMA_VERSION,
    data: {
      conversations,
      messages,
      ownerMetadata,
      settings: settings.filter((item) => item.key !== 'offlineMode'),
      capabilities: capabilities.map(({ id: _id, ...item }) => item)
    }
  };
}

export function workspaceBackupCounts(backup: WorkspaceBackup): WorkspaceBackupCounts {
  return {
    conversations: backup.data.conversations.length,
    messages: backup.data.messages.length,
    ownerMetadata: backup.data.ownerMetadata.length
  };
}

export async function restoreWorkspaceBackup(input: unknown): Promise<WorkspaceBackupCounts> {
  const backup = validateWorkspaceBackup(input);

  await db.transaction(
    'rw',
    db.conversations,
    db.messages,
    db.ownerMetadata,
    db.settings,
    db.capabilities,
    async () => {
      await db.conversations.clear();
      await db.messages.clear();
      await db.ownerMetadata.clear();
      await db.settings.clear();
      await db.capabilities.clear();

      if (backup.data.conversations.length) await db.conversations.bulkPut(backup.data.conversations);
      if (backup.data.messages.length) await db.messages.bulkPut(backup.data.messages);
      if (backup.data.ownerMetadata.length) await db.ownerMetadata.bulkPut(backup.data.ownerMetadata);
      if (backup.data.settings.length) await db.settings.bulkPut(backup.data.settings);
      if (backup.data.capabilities.length) await db.capabilities.bulkAdd(backup.data.capabilities);

      const restoredAt = Date.now();
      await db.settings.put({ key: 'offlineMode', value: false, updatedAt: restoredAt });
      await db.settings.put({
        key: 'lastRestore',
        value: {
          restoredAt,
          backupExportedAt: backup.exportedAt,
          sourceExtensionVersion: backup.extensionVersion
        },
        updatedAt: restoredAt
      });
    }
  );

  return workspaceBackupCounts(backup);
}

export function validateWorkspaceBackup(input: unknown): WorkspaceBackup {
  if (!input || typeof input !== 'object') throw new Error('BACKUP_INVALID: Backup must be a JSON object.');
  const candidate = input as Partial<WorkspaceBackup>;

  if (candidate.format !== WORKSPACE_BACKUP_FORMAT) {
    throw new Error('BACKUP_FORMAT_UNSUPPORTED: Not a ChatGPT Workspace Manager backup.');
  }
  if (candidate.formatVersion !== WORKSPACE_BACKUP_VERSION) {
    throw new Error(`BACKUP_VERSION_UNSUPPORTED: Expected format version ${WORKSPACE_BACKUP_VERSION}.`);
  }
  if (typeof candidate.exportedAt !== 'string' || !candidate.exportedAt) {
    throw new Error('BACKUP_INVALID: Missing exportedAt.');
  }
  if (typeof candidate.extensionVersion !== 'string' || !candidate.extensionVersion) {
    throw new Error('BACKUP_INVALID: Missing extensionVersion.');
  }
  if (typeof candidate.dbSchemaVersion !== 'number' || !Number.isFinite(candidate.dbSchemaVersion)) {
    throw new Error('BACKUP_INVALID: Missing dbSchemaVersion.');
  }
  if (candidate.dbSchemaVersion > DB_SCHEMA_VERSION) {
    throw new Error(
      `BACKUP_DB_NEWER: Backup DB schema ${candidate.dbSchemaVersion} is newer than supported schema ${DB_SCHEMA_VERSION}.`
    );
  }
  if (!candidate.data || typeof candidate.data !== 'object') {
    throw new Error('BACKUP_INVALID: Missing data section.');
  }

  const data = candidate.data as WorkspaceBackup['data'];
  const arrays: Array<[string, unknown]> = [
    ['conversations', data.conversations],
    ['messages', data.messages],
    ['ownerMetadata', data.ownerMetadata],
    ['settings', data.settings],
    ['capabilities', data.capabilities]
  ];
  for (const [name, value] of arrays) {
    if (!Array.isArray(value)) throw new Error(`BACKUP_INVALID: data.${name} must be an array.`);
  }

  for (const conversation of data.conversations) {
    if (!conversation || typeof conversation !== 'object' || typeof conversation.id !== 'string' || !conversation.id) {
      throw new Error('BACKUP_INVALID: Conversation record missing id.');
    }
    if (conversation.provider !== 'chatgpt') {
      throw new Error('BACKUP_INVALID: Unsupported conversation provider.');
    }
  }

  for (const message of data.messages) {
    if (
      !message ||
      typeof message !== 'object' ||
      typeof message.key !== 'string' ||
      !message.key ||
      typeof message.conversationId !== 'string' ||
      !message.conversationId
    ) {
      throw new Error('BACKUP_INVALID: Message record missing key or conversationId.');
    }
  }

  for (const owner of data.ownerMetadata) {
    if (!owner || typeof owner !== 'object' || typeof owner.conversationId !== 'string' || !owner.conversationId) {
      throw new Error('BACKUP_INVALID: Owner metadata record missing conversationId.');
    }
  }

  for (const setting of data.settings) {
    if (!setting || typeof setting !== 'object' || typeof setting.key !== 'string' || !setting.key) {
      throw new Error('BACKUP_INVALID: Setting record missing key.');
    }
  }

  for (const capability of data.capabilities) {
    if (!capability || typeof capability !== 'object' || typeof capability.capability !== 'string') {
      throw new Error('BACKUP_INVALID: Capability record missing capability.');
    }
  }

  return candidate as WorkspaceBackup;
}
