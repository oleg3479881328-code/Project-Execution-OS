import { defineConfig } from 'wxt';

export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    name: 'WedditNYC Photo Lead Review',
    description:
      'Locally classifies visible r/WedditNYC posts and manages review decisions in a Chrome side panel.',
    minimum_chrome_version: '114',
    permissions: ['storage', 'sidePanel'],
    action: {
      default_title: 'Open WedditNYC lead panel'
    },
    host_permissions: [
      'https://www.reddit.com/r/WedditNYC/*',
      'https://old.reddit.com/r/WedditNYC/*'
    ]
  }
});
