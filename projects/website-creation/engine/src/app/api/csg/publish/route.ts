import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

import { CSG_EDITOR_COOKIE, verifyEditorSession } from '@/csg/auth'
import { CsgGitError, publishCsgDraft } from '@/csg/github'

export const runtime = 'nodejs'

export async function POST() {
  const session = (await cookies()).get(CSG_EDITOR_COOKIE)?.value
  if (!verifyEditorSession(session)) return NextResponse.json({ ok: false, error: 'Editor session expired.' }, { status: 401 })
  try {
    const result = await publishCsgDraft()
    return NextResponse.json({ ok: true, ...result })
  } catch (error) {
    const status = error instanceof CsgGitError ? error.status : 500
    return NextResponse.json({ ok: false, error: error instanceof Error ? error.message : 'Publish failed.' }, { status })
  }
}
