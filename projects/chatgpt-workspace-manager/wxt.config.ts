import { defineConfig } from 'wxt';
import { STABLE_EXTENSION_KEY } from './src/core/extension-identity';

export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    name: 'ChatGPT Workspace Manager',
    description: 'Private local-first control center for managing ChatGPT conversations.',
    version: '0.1.5',
    key: STABLE_EXTENSION_KEY,
    permissions: ['storage', 'sidePanel', 'activeTab', 'scripting', 'unlimitedStorage'],
    host_permissions: ['https://chatgpt.com/*', 'https://chat.openai.com/*'],
    side_panel: {
      default_path: 'sidepanel.html'
    },
    action: {
      default_title: 'ChatGPT Workspace Manager'
    }
  }
});
