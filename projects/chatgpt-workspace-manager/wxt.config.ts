import { defineConfig } from 'wxt';
import react from '@wxt-dev/module-react';

export default defineConfig({
  modules: [react()],
  manifest: {
    name: 'ChatGPT Workspace Manager',
    description: 'Private local-first control center for managing ChatGPT conversations.',
    version: '0.1.0',
    permissions: ['storage', 'sidePanel', 'activeTab'],
    host_permissions: ['https://chatgpt.com/*', 'https://chat.openai.com/*'],
    side_panel: {
      default_path: 'sidepanel.html'
    },
    action: {
      default_title: 'ChatGPT Workspace Manager'
    }
  }
});
