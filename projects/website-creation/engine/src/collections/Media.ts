import type { CollectionConfig } from 'payload'

const isVercelRuntime = process.env.VERCEL === '1'

export const Media: CollectionConfig = {
  slug: 'media',
  access: {
    read: () => true,
    create: ({ req }) => Boolean(req.user),
    update: ({ req }) => Boolean(req.user),
    delete: ({ req }) => Boolean(req.user),
  },
  upload: {
    staticDir: process.env.MEDIA_DIR || 'media',
    // Vercel's filesystem is ephemeral, so production uploads there must use
    // the official Blob adapter. Other hosts may deliberately provide a
    // persistent filesystem through MEDIA_DIR and must keep local storage on.
    disableLocalStorage: isVercelRuntime && !process.env.BLOB_READ_WRITE_TOKEN,
    mimeTypes: ['image/*'],
  },
  fields: [
    {
      name: 'alt',
      type: 'text',
      required: true,
    },
  ],
}
