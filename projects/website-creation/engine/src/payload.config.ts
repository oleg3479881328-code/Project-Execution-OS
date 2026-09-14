import { postgresAdapter } from '@payloadcms/db-postgres'
import { createPuckPlugin } from '@delmaredigital/payload-puck/plugin'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import sharp from 'sharp'
import { buildConfig } from 'payload'

import { Media } from './collections/Media'
import { Users } from './collections/Users'

const filename = fileURLToPath(import.meta.url)
const dirname = path.dirname(filename)

export default buildConfig({
  admin: {
    user: Users.slug,
    importMap: {
      baseDir: path.resolve(dirname),
    },
    components: {
      providers: ['@/components/PuckProvider'],
    },
    livePreview: {
      breakpoints: [
        { label: 'Mobile', name: 'mobile', width: 390, height: 844 },
        { label: 'Tablet', name: 'tablet', width: 768, height: 1024 },
        { label: 'Desktop', name: 'desktop', width: 1440, height: 900 }
      ],
    },
  },
  db: postgresAdapter({
    pool: {
      connectionString: process.env.DATABASE_URL || '',
    },
  }),
  collections: [Users, Media],
  plugins: [
    createPuckPlugin({
      pagesCollection: 'pages',
      editorStylesheets: ['/site.css', '/image-editor.css'],
      previewUrl: (page) => (page.isHomepage ? '/' : `/${page.slug || ''}`),
    }),
  ],
  secret: process.env.PAYLOAD_SECRET || 'development-only-change-me',
  sharp,
  typescript: {
    outputFile: path.resolve(dirname, 'payload-types.ts'),
  },
})
