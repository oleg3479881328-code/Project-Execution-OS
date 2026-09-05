import type { CanonicalMessage, ProviderConversation, ProviderConversationDetail } from '../../core/models';

export const CHATGPT_ADAPTER_VERSION = '2026-09-slice1';
const PAGE_LIMIT = 50;

interface SessionResponse {
  accessToken?: string;
}

interface RawConversationList {
  items?: RawConversation[];
  total?: number;
  limit?: number;
  offset?: number;
  has_missing_conversations?: boolean;
}

interface RawConversation {
  id?: string;
  title?: string;
  create_time?: number;
  update_time?: number;
  is_archived?: boolean;
  current_node?: string;
  gizmo_id?: string | null;
  gizmo_type?: string | null;
  conversation_origin?: unknown;
}

interface RawMessageContent {
  content_type?: string;
  parts?: unknown[];
  text?: string;
}

interface RawMessageNode {
  id?: string;
  parent?: string | null;
  children?: string[];
  message?: {
    id?: string;
    author?: { role?: string };
    create_time?: number;
    metadata?: Record<string, unknown>;
    content?: RawMessageContent;
  } | null;
}

interface RawConversationDetail extends RawConversation {
  mapping?: Record<string, RawMessageNode>;
}

export async function fetchAccessToken(): Promise<string> {
  const response = await fetch('/api/auth/session', { credentials: 'include' });
  if (!response.ok) throw new Error(`SESSION_HTTP_${response.status}`);
  const session = (await response.json()) as SessionResponse;
  if (!session.accessToken) throw new Error('SESSION_TOKEN_MISSING');
  return session.accessToken;
}

function authHeaders(accessToken: string): HeadersInit {
  return {
    Authorization: `Bearer ${accessToken}`,
    'Content-Type': 'application/json'
  };
}

export function normalizeConversation(raw: RawConversation, syncedAt = Date.now()): ProviderConversation | null {
  if (!raw.id) return null;
  return {
    provider: 'chatgpt',
    id: raw.id,
    title: raw.title?.trim() || 'Untitled conversation',
    createdAt: toMs(raw.create_time),
    updatedAt: toMs(raw.update_time),
    nativeProjectId: raw.gizmo_id ?? null,
    archived: Boolean(raw.is_archived),
    currentNodeId: raw.current_node ?? null,
    contentHydrated: false,
    lastSyncedAt: syncedAt,
    providerRawVersion: CHATGPT_ADAPTER_VERSION
  };
}

export async function listAllConversations(accessToken: string): Promise<{
  conversations: ProviderConversation[];
  total: number;
}> {
  const syncedAt = Date.now();
  const byId = new Map<string, ProviderConversation>();

  for (const archived of [false, true]) {
    let offset = 0;
    for (let page = 0; page < 500; page += 1) {
      const url = `/backend-api/conversations?offset=${offset}&limit=${PAGE_LIMIT}&order=updated&is_archived=${archived}`;
      const response = await fetch(url, { headers: authHeaders(accessToken), credentials: 'include' });
      if (!response.ok) {
        if (archived && response.status === 400) break;
        throw new Error(`LIST_HTTP_${response.status}`);
      }
      const payload = (await response.json()) as RawConversationList;
      const items = Array.isArray(payload.items) ? payload.items : [];
      for (const raw of items) {
        const normalized = normalizeConversation(raw, syncedAt);
        if (normalized) byId.set(normalized.id, normalized);
      }

      offset += items.length;
      const total = typeof payload.total === 'number' ? payload.total : undefined;
      if (items.length === 0 || items.length < PAGE_LIMIT || (total !== undefined && offset >= total)) break;
    }
  }

  const conversations = [...byId.values()].sort((a, b) => (b.updatedAt ?? 0) - (a.updatedAt ?? 0));
  return { conversations, total: conversations.length };
}

export async function readConversation(
  accessToken: string,
  conversationId: string
): Promise<ProviderConversationDetail> {
  const response = await fetch(`/backend-api/conversation/${encodeURIComponent(conversationId)}`, {
    headers: authHeaders(accessToken),
    credentials: 'include'
  });
  if (!response.ok) throw new Error(`READ_HTTP_${response.status}`);

  const raw = (await response.json()) as RawConversationDetail;
  const conversation = normalizeConversation({ ...raw, id: raw.id ?? conversationId }) ?? {
    provider: 'chatgpt' as const,
    id: conversationId,
    title: raw.title?.trim() || 'Untitled conversation',
    contentHydrated: true,
    lastSyncedAt: Date.now(),
    providerRawVersion: CHATGPT_ADAPTER_VERSION
  };

  const messages = normalizeMessages(raw, conversationId);
  return {
    conversation: {
      ...conversation,
      contentHydrated: true,
      messageCount: messages.length,
      lastHydratedAt: Date.now()
    },
    messages
  };
}

function normalizeMessages(raw: RawConversationDetail, conversationId: string): CanonicalMessage[] {
  const mapping = raw.mapping ?? {};
  const currentNode = raw.current_node;
  const orderedNodes = currentNode ? activeBranch(mapping, currentNode) : chronologicalNodes(mapping);
  const capturedAt = Date.now();
  const messages: CanonicalMessage[] = [];

  for (const node of orderedNodes) {
    const message = node.message;
    if (!message) continue;
    const id = message.id || node.id;
    if (!id) continue;
    const textPlain = extractText(message.content);
    if (!textPlain && !message.content) continue;

    messages.push({
      key: `${conversationId}:${id}`,
      provider: 'chatgpt',
      conversationId,
      id,
      parentId: node.parent ?? null,
      index: messages.length,
      role: normalizeRole(message.author?.role),
      model: typeof message.metadata?.model_slug === 'string' ? message.metadata.model_slug : null,
      createdAt: toMs(message.create_time),
      textPlain,
      source: 'live-api',
      capturedAt
    });
  }

  return messages;
}

function activeBranch(mapping: Record<string, RawMessageNode>, leafId: string): RawMessageNode[] {
  const result: RawMessageNode[] = [];
  const seen = new Set<string>();
  let cursor: string | null | undefined = leafId;
  while (cursor && !seen.has(cursor)) {
    seen.add(cursor);
    const node = mapping[cursor];
    if (!node) break;
    result.push({ ...node, id: node.id ?? cursor });
    cursor = node.parent;
  }
  return result.reverse();
}

function chronologicalNodes(mapping: Record<string, RawMessageNode>): RawMessageNode[] {
  return Object.entries(mapping)
    .map(([id, node]) => ({ ...node, id: node.id ?? id }))
    .sort((a, b) => (a.message?.create_time ?? 0) - (b.message?.create_time ?? 0));
}

function normalizeRole(role?: string): CanonicalMessage['role'] {
  if (role === 'user' || role === 'assistant' || role === 'system' || role === 'tool') return role;
  return 'other';
}

function extractText(content?: RawMessageContent): string {
  if (!content) return '';
  if (typeof content.text === 'string') return content.text;
  if (!Array.isArray(content.parts)) return '';
  return content.parts.map(extractPartText).filter(Boolean).join('\n\n').trim();
}

function extractPartText(part: unknown): string {
  if (typeof part === 'string') return part;
  if (part === null || part === undefined) return '';
  if (Array.isArray(part)) return part.map(extractPartText).filter(Boolean).join('\n');
  if (typeof part === 'object') {
    const record = part as Record<string, unknown>;
    if (typeof record.text === 'string') return record.text;
    if (typeof record.content === 'string') return record.content;
    if (Array.isArray(record.parts)) return record.parts.map(extractPartText).filter(Boolean).join('\n');
  }
  return '';
}

function toMs(value?: number): number | undefined {
  if (typeof value !== 'number' || !Number.isFinite(value)) return undefined;
  return value > 10_000_000_000 ? value : Math.round(value * 1000);
}
