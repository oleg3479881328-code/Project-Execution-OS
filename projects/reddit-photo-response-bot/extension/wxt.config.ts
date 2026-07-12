import { defineConfig } from 'wxt';

export default defineConfig({
  modules: ['@wxt-dev/module-react'],
  manifest: {
    name: 'WedditNYC Photo Lead Review',
    description:
      'Locally classifies visible r/WedditNYC posts and helps review potential wedding photography leads.',
    permissions: ['storage'],
    host_permissions: [
      'https://www.reddit.com/r/WedditNYC/*',
      'https://old.reddit.com/r/WedditNYC/*'
    ]
  }
});
