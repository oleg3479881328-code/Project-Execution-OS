import { defineConfig } from '@playwright/test'

const appCommand = process.env.CI ? 'pnpm start' : 'pnpm dev'

export default defineConfig({
  testDir: './tests',
  use: {
    baseURL: process.env.PLAYWRIGHT_BASE_URL || 'http://127.0.0.1:3000',
  },
  webServer: [
    {
      command: 'node tests/mock-github-server.mjs',
      url: 'http://127.0.0.1:4010/health',
      reuseExistingServer: true,
    },
    {
      command: appCommand,
      url: 'http://127.0.0.1:3000/health',
      reuseExistingServer: true,
    },
  ],
})
