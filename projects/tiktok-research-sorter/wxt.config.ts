import { defineConfig } from 'wxt';

export default defineConfig({
  srcDir: '.',
  manifest: {
    name: 'TikTok Research Sorter',
    description: 'Scan, sort, compare, and export public TikTok profile video metrics locally.',
    version: '0.2.0',
    permissions: ['storage', 'sidePanel', 'activeTab', 'scripting'],
    host_permissions: ['https://www.tiktok.com/*', 'https://tiktok.com/*'],
    action: {
      default_title: 'Open TikTok Research Sorter',
    },
    web_accessible_resources: [
      {
        resources: ['page-hook.js'],
        matches: ['https://www.tiktok.com/*', 'https://tiktok.com/*'],
      },
    ],
  },
});
