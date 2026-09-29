import config from '@payload-config'
import { getPayload } from 'payload'

export const dynamic = 'force-dynamic'

export async function GET() {
  try {
    const payload = await getPayload({ config })
    await payload.find({ collection: 'pages' as any, limit: 1, depth: 0, overrideAccess: true })

    const media = process.env.BLOB_READ_WRITE_TOKEN
      ? 'vercel-blob'
      : process.env.VERCEL === '1'
        ? 'disabled-until-vercel-blob-is-configured'
        : process.env.MEDIA_DIR
          ? 'filesystem-configured'
          : 'local-filesystem'

    return Response.json({
      ok: true,
      service: 'website-creator-engine',
      database: 'reachable',
      media,
    })
  } catch (error) {
    return Response.json(
      {
        ok: false,
        service: 'website-creator-engine',
        database: 'unreachable',
        error: error instanceof Error ? error.message : 'unknown error',
      },
      { status: 503 },
    )
  }
}
