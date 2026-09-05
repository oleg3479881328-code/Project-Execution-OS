import { browser, defineContentScript } from '#imports';
import {
  fetchAccessToken,
  listAllConversations,
  readConversation
} from '../src/providers/chatgpt/api-strategy';
import type { ChatGPTBridgeRequest, ChatGPTBridgeResponse } from '../src/providers/chatgpt/protocol';
import { errorResponse } from '../src/providers/chatgpt/protocol';

export default defineContentScript({
  matches: ['https://chatgpt.com/*', 'https://chat.openai.com/*'],
  runAt: 'document_idle',
  main() {
    browser.runtime.onMessage.addListener((request: ChatGPTBridgeRequest) => {
      if (!request || typeof request !== 'object' || !('type' in request)) return undefined;
      return handleRequest(request);
    });
  }
});

async function handleRequest(request: ChatGPTBridgeRequest): Promise<ChatGPTBridgeResponse> {
  try {
    switch (request.type) {
      case 'CWM_CHATGPT_HEALTH': {
        await fetchAccessToken();
        return {
          ok: true,
          type: 'health',
          session: true,
          list: 'unknown',
          read: 'unknown'
        };
      }
      case 'CWM_CHATGPT_LIST': {
        const token = await fetchAccessToken();
        const result = await listAllConversations(token);
        return {
          ok: true,
          type: 'list',
          conversations: result.conversations,
          total: result.total
        };
      }
      case 'CWM_CHATGPT_READ': {
        const token = await fetchAccessToken();
        const detail = await readConversation(token, request.conversationId);
        return { ok: true, type: 'read', detail };
      }
      default:
        return {
          ok: false,
          error: 'Unsupported request',
          diagnosticCode: 'CHATGPT_UNSUPPORTED_REQUEST'
        };
    }
  } catch (error) {
    return errorResponse(error);
  }
}
