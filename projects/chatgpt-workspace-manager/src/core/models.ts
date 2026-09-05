export type ProviderName = 'chatgpt';

export type Capability =
  | 'chatgpt-tab'
  | 'session'
  | 'list-conversations'
  | 'read-conversation'
  | 'list-projects'
  | 'archive-conversation'
  | 'delete-conversation'
  | 'rename-conversation'
  | 'dom-navigation'
  | 'local-db'
  | 'local-search';

export type CapabilityStatus = 'healthy' | 'degraded' | 'unavailable' | 'unknown';
export type CapabilityStrategy = 'live-api' | 'dom' | 'official-export' | 'local';

export interface CapabilityHealth {
  id?: number;
  capability: Capability;
  status: CapabilityStatus;
  strategy?: CapabilityStrategy;
  checkedAt: number;
  message?: string;
  diagnosticCode?: string;
}

export interface ProviderConversation {
  provider: ProviderName;
  id: string;
  title: string;
  createdAt?: number;
  updatedAt?: number;
  nativeProjectId?: string | null;
  nativeProjectTitle?: string | null;
  archived?: boolean;
  providerMissing?: boolean;
  currentNodeId?: string | null;
  messageCount?: number;
  contentHydrated: boolean;
  lastSyncedAt: number;
  lastHydratedAt?: number;
  providerRawVersion?: string;
}

export type CanonicalRole = 'user' | 'assistant' | 'system' | 'tool' | 'other';

export interface CanonicalMessage {
  key: string;
  provider: ProviderName;
  conversationId: string;
  id: string;
  parentId?: string | null;
  index: number;
  role: CanonicalRole;
  model?: string | null;
  createdAt?: number;
  textPlain: string;
  contentHtml?: string;
  source: 'live-api' | 'dom' | 'official-export';
  capturedAt: number;
}

export interface OwnerConversationMetadata {
  conversationId: string;
  folderIds: string[];
  tagIds: string[];
  favorite: boolean;
  pinned: boolean;
  note?: string;
  bookmarkIds: string[];
  customStatus?: string;
  updatedAt: number;
}

export interface SettingRecord {
  key: string;
  value: unknown;
  updatedAt: number;
}

export interface SyncSummary {
  syncedAt: number;
  received: number;
  upserted: number;
  hydrated?: number;
}

export interface WorkspaceConversation extends ProviderConversation {
  owner: OwnerConversationMetadata;
}

export interface ProviderConversationListResponse {
  conversations: ProviderConversation[];
  total?: number;
}

export interface ProviderConversationDetail {
  conversation: ProviderConversation;
  messages: CanonicalMessage[];
}

export interface DiagnosticsReport {
  exportedAt: string;
  extensionVersion: string;
  extensionId: string;
  dbSchemaVersion: number;
  adapterVersion: string;
  capabilities: CapabilityHealth[];
  syncSummary?: SyncSummary;
  browser?: {
    userAgent?: string;
    platform?: string;
  };
}
