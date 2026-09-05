import type { ProviderConversation, ProviderConversationDetail } from '../../core/models';

export type ChatGPTBridgeRequest =
  | { type: 'CWM_CHATGPT_HEALTH' }
  | { type: 'CWM_CHATGPT_LIST' }
  | { type: 'CWM_CHATGPT_READ'; conversationId: string };

export type ChatGPTBridgeResponse =
  | {
      ok: true;
      type: 'health';
      session: boolean;
      list: 'unknown';
      read: 'unknown';
    }
  | {
      ok: true;
      type: 'list';
      conversations: ProviderConversation[];
      total: number;
    }
  | {
      ok: true;
      type: 'read';
      detail: ProviderConversationDetail;
    }
  | {
      ok: false;
      error: string;
      diagnosticCode: string;
    };

export function errorResponse(error: unknown): ChatGPTBridgeResponse {
  const raw = error instanceof Error ? error.message : String(error);
  return {
    ok: false,
    error: sanitizeError(raw),
    diagnosticCode: diagnosticCode(raw)
  };
}

function diagnosticCode(message: string): string {
  const match = message.match(/[A-Z]+(?:_[A-Z0-9]+)+/);
  return match?.[0] ?? 'CHATGPT_UNKNOWN_ERROR';
}

function sanitizeError(message: string): string {
  return message
    .replace(/Bearer\s+[A-Za-z0-9._-]+/gi, 'Bearer [redacted]')
    .replace(/eyJ[A-Za-z0-9._-]+/g, '[token-redacted]')
    .slice(0, 500);
}
