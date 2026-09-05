import { defineConfig } from 'wxt';

// Stable development identity for the private unpacked extension.
// Do not change this key: Chrome derives the extension ID from it.
const STABLE_EXTENSION_KEY =
  'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAry/iPfb9NRHdmo9+UkcXnAVd1J1bGNkuwdnRddJUV5cMU5U6dCjV6gbsT3vYvPPB6KC6cPloUVdv+nqI5un/T8vMYsJ2ii4PWtd+IgyFLCZvBcPp4GFntI8NCgBOrRkMFFIEytjErC5SKs4caIYsVVErsh6dPJG3rRifzmsDK13p9RtvNcYi8IqLx7/tQ7h6h/H6q/41AwJfsIATpUTfmWj736aN2KhsvORz1bFcheVmiGfG1AtMQZ9p9BI01Dpk8EFYiTbWcy+WXcWCdZHWuVaarHNrDerPYkOWwu53lXBz/obwVDRR2gZHnfFGpu1cfNHCQ9i7qqIHZkugK2neTwIDAQAB';

export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    name: 'ChatGPT Workspace Manager',
    description: 'Private local-first control center for managing ChatGPT conversations.',
    version: '0.1.4',
    key: STABLE_EXTENSION_KEY,
    permissions: ['storage', 'sidePanel', 'activeTab', 'scripting'],
    host_permissions: ['https://chatgpt.com/*', 'https://chat.openai.com/*'],
    side_panel: {
      default_path: 'sidepanel.html'
    },
    action: {
      default_title: 'ChatGPT Workspace Manager'
    }
  }
});
