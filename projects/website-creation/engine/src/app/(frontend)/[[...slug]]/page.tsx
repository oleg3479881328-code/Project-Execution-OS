import { PageRenderer } from '@delmaredigital/payload-puck/render'
import config from '@payload-config'
import type { Metadata } from 'next'
import { notFound } from 'next/navigation'
import { getPayload } from 'payload'

import { websiteConfig } from '@/puck/config'

export const dynamic = 'force-dynamic'

type Args = { params: Promise<{ slug?: string[] }> }

async function getPage(slugParts?: string[]) {
  const payload = await getPayload({ config })
  const slug = slugParts?.join('/') || ''
  const where = slug
    ? { slug: { equals: slug } }
    : { or: [{ isHomepage: { equals: true } }, { slug: { equals: 'home' } }] }

  const result = await payload.find({
    collection: 'pages' as any,
    where: where as any,
    limit: 1,
    draft: false,
    overrideAccess: false,
  })

  return result.docs[0] as any
}

export async function generateMetadata({ params }: Args): Promise<Metadata> {
  const { slug } = await params
  const page = await getPage(slug)
  if (!page) return {}
  return {
    title: page.meta?.title || page.title,
    description: page.meta?.description,
  }
}

export default async function PublicPage({ params }: Args) {
  const { slug } = await params
  const page = await getPage(slug)
  if (!page) notFound()

  return (
    <main data-site-renderer="website-creator-v0.1">
      <PageRenderer config={websiteConfig} data={page.puckData} />
    </main>
  )
}
