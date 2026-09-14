import config from '@payload-config'
import { redirect } from 'next/navigation'
import { getPayload } from 'payload'

export const dynamic = 'force-dynamic'

export default async function EditorEntryPage() {
  const payload = await getPayload({ config })
  const result = await payload.find({
    collection: 'pages' as any,
    where: {
      or: [
        { isHomepage: { equals: true } },
        { slug: { equals: 'home' } },
      ],
    } as any,
    limit: 1,
    draft: true,
    overrideAccess: true,
  })

  const page = result.docs[0] as any

  if (!page?.id) {
    redirect('/admin/collections/pages')
  }

  redirect(`/admin/puck-editor/pages/${page.id}`)
}
