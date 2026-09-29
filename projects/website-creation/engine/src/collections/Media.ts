import type { CollectionConfig } from 'payload'

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
    // Vercel's filesystem is ephemeral. The official Blob adapter disables
    // local storage when configured; keep the fallback disabled in production
    // so a missing Blob token cannot masquerade as durable media persistence.
    disableLocalStorage: process.env.NODE_ENV === 'production' && !process.env.BLOB_READ_WRITE_TOKEN,
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
