import { cookies } from 'next/headers'
import { redirect } from 'next/navigation'

import { CSG_EDITOR_COOKIE, verifyEditorSession } from '@/csg/auth'
import { loadEditorState } from '@/csg/github'
import CsgPuckEditor from '@/csg/CsgPuckEditor'

export const dynamic = 'force-dynamic'

export default async function EditorEntryPage() {
  const session = (await cookies()).get(CSG_EDITOR_COOKIE)?.value
  if (!verifyEditorSession(session)) redirect('/editor/login?next=/editor')
  const { state, durable } = await loadEditorState()
  return <CsgPuckEditor initialSite={state} durable={durable} />
}
