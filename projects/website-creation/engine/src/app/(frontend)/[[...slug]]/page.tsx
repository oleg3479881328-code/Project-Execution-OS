import { PageRenderer } from '@delmaredigital/payload-puck/render'
import config from '@payload-config'
import type { Metadata } from 'next'
import { notFound } from 'next/navigation'
import { getPayload } from 'payload'

import { readCsgState } from '@/csg/github'
import { websiteConfig } from '@/puck/config'
import { carServiceGarage } from '@/sites/car-service-garage'

export const dynamic = 'force-dynamic'

type Args = { params: Promise<{ slug?: string[] }> }

async function getPage(slugParts?: string[]) {
  if (process.env.CSG_GITHUB_MODE !== '0') {
    const state = process.env.CSG_GITHUB_LIVE_READBACK === '1'
      ? await readCsgState('main')
      : carServiceGarage
    const slug = slugParts?.join('/') || ''
    return state.pages.find((page) => slug ? page.slug === slug : page.isHomepage || page.slug === 'home')
  }
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
