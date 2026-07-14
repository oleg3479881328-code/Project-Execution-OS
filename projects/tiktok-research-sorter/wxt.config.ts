import { defineConfig } from 'wxt';

export default defineConfig({
  srcDir: '.',
  manifest: {
    name: 'TikTok Research Sorter',
    description: 'Research TikTok profiles and hashtags, save favorites, queue videos in the local yt-dlp Download Manager, and export selected HTML.',
    version: '0.6.0',
    permissions: ['storage', 'sidePanel', 'activeTab', 'scripting'],
    host_permissions: [
      'https://www.tiktok.com/*',
      'https://tiktok.com/*',
      'http://127.0.0.1:8000/*',
    ],
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
