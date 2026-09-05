import { browser } from '#imports';
import type {
  CapabilityHealth,
  ProviderConversationDetail,
  ProviderConversationListResponse
} from '../../core/models';
import type { ChatGPTBridgeRequest, ChatGPTBridgeResponse } from './protocol';
import { CHATGPT_ADAPTER_VERSION } from './api-strategy';

const CHATGPT_URL_PATTERNS = ['https://chatgpt.com/*', 'https://chat.openai.com/*'];
type BrowserTab = Awaited<ReturnType<typeof browser.tabs.query>>[number];

export class ChatGPTAdapter {
  readonly provider = 'chatgpt' as const;
  readonly version = CHATGPT_ADAPTER_VERSION;

  async health(): Promise<CapabilityHealth[]> {
    const checkedAt = Date.now();
    const tab = await findChatGPTTab();
    if (!tab?.id) {
      return [
        health('chatgpt-tab', 'unavailable', checkedAt, 'Open ChatGPT in this browser window.', 'CHATGPT_TAB_MISSING'),
        health('session', 'unknown', checkedAt),
        health('list-conversations', 'unknown', checkedAt),
        health('read-conversation', 'unknown', checkedAt)
      ];
    }

    const response = await send(tab.id, { type: 'CWM_CHATGPT_HEALTH' });
    if (!response.ok) {
      return [
        health('chatgpt-tab', 'healthy', checkedAt, undefined, undefined, 'dom'),
        health('session', 'unavailable', checkedAt, response.error, response.diagnosticCode, 'live-api'),
        health('list-conversations', 'unknown', checkedAt, undefined, undefined, 'live-api'),
        health('read-conversation', 'unknown', checkedAt, undefined, undefined, 'live-api')
      ];
    }

    return [
      health('chatgpt-tab', 'healthy', checkedAt, undefined, undefined, 'dom'),
      health('session', response.session ? 'healthy' : 'unavailable', checkedAt, undefined, undefined, 'live-api'),
      health('list-conversations', response.list ? 'healthy' : 'unknown', checkedAt, undefined, undefined, 'live-api'),
      health('read-conversation', 'unknown', checkedAt, 'Validated on first successful preview.', undefined, 'live-api')
    ];
  }

  async listConversations(): Promise<ProviderConversationListResponse> {
    const tab = await requireChatGPTTab();
    const response = await send(tab.id!, { type: 'CWM_CHATGPT_LIST' });
    if (!response.ok) throw bridgeError(response);
    if (response.type !== 'list') throw new Error('CHATGPT_LIST_RESPONSE_INVALID');
    return { conversations: response.conversations, total: response.total };
  }

  async readConversation(conversationId: string): Promise<ProviderConversationDetail> {
    const tab = await requireChatGPTTab();
    const response = await send(tab.id!, { type: 'CWM_CHATGPT_READ', conversationId });
    if (!response.ok) throw bridgeError(response);
    if (response.type !== 'read') throw new Error('CHATGPT_READ_RESPONSE_INVALID');
    return response.detail;
  }
}

export const chatGPTAdapter = new ChatGPTAdapter();

async function send(tabId: number, request: ChatGPTBridgeRequest): Promise<ChatGPTBridgeResponse> {
  try {
    return (await browser.tabs.sendMessage(tabId, request)) as ChatGPTBridgeResponse;
  } catch (error) {
    const message = error instanceof Error ? error.message : String(error);
    return {
      ok: false,
      error: message.slice(0, 500),
      diagnosticCode: message.includes('Receiving end does not exist')
        ? 'CHATGPT_CONTENT_BRIDGE_MISSING'
        : 'CHATGPT_BRIDGE_ERROR'
    };
  }
}

async function requireChatGPTTab(): Promise<BrowserTab> {
  const tab = await findChatGPTTab();
  if (!tab?.id) throw new Error('CHATGPT_TAB_MISSING');
  return tab;
}

async function findChatGPTTab(): Promise<BrowserTab | undefined> {
  const active = (await browser.tabs.query({ active: true, currentWindow: true }))[0];
  if (active?.url && isChatGPTUrl(active.url)) return active;

  const matches = await browser.tabs.query({ url: CHATGPT_URL_PATTERNS });
  return matches.find((tab) => tab.active) ?? matches[0];
}

function isChatGPTUrl(url: string): boolean {
  return url.startsWith('https://chatgpt.com/') || url.startsWith('https://chat.openai.com/');
}

function bridgeError(response: Extract<ChatGPTBridgeResponse, { ok: false }>): Error {
  const error = new Error(`${response.diagnosticCode}: ${response.error}`);
  error.name = response.diagnosticCode;
  return error;
}

function health(
  capability: CapabilityHealth['capability'],
  status: CapabilityHealth['status'],
  checkedAt: number,
  message?: string,
  diagnosticCode?: string,
  strategy?: CapabilityHealth['strategy']
): CapabilityHealth {
  return { capability, status, checkedAt, message, diagnosticCode, strategy };
}
