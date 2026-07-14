import { defineConfig } from 'wxt';

export default defineConfig({
  srcDir: '.',
  manifest: {
    name: 'TikTok Research Sorter',
    description: 'Scan TikTok profiles and hashtag pages, save favorites, and export selected research as HTML.',
    version: '0.4.0',
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
