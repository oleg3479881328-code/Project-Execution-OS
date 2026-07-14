import { defineConfig } from 'wxt';

export default defineConfig({
  srcDir: '.',
  manifest: {
    name: 'TikTok Research Sorter',
    description: 'Scan public TikTok profiles and hashtag pages, rank videos per account, and export research locally.',
    version: '0.3.0',
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
