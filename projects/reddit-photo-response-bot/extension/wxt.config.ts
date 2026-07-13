import { defineConfig } from 'wxt';

export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    name: 'WedditNYC Photo Lead Review',
    description:
      'Classifies visible r/WedditNYC posts and manages local and DeepSeek-assisted review decisions in a Chrome side panel.',
    minimum_chrome_version: '114',
    permissions: ['storage', 'sidePanel'],
    optional_host_permissions: ['https://*/*'],
    action: {
      default_title: 'Open WedditNYC lead panel'
    },
    host_permissions: [
      'https://www.reddit.com/r/WedditNYC/*',
      'https://old.reddit.com/r/WedditNYC/*'
    ]
  }
});