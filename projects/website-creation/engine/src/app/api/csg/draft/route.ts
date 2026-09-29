import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

import { CSG_EDITOR_COOKIE, verifyEditorSession } from '@/csg/auth'
import { CsgGitError, saveCsgDraft, validateCsgState } from '@/csg/github'

export const runtime = 'nodejs'

export async function POST(request: Request) {
  const session = (await cookies()).get(CSG_EDITOR_COOKIE)?.value
  if (!verifyEditorSession(session)) return NextResponse.json({ ok: false, error: 'Editor session expired.' }, { status: 401 })
  const body = await request.json().catch(() => ({})) as { state?: unknown }
  if (!validateCsgState(body.state)) return NextResponse.json({ ok: false, error: 'Invalid CSG canonical state.' }, { status: 422 })
  try {
    const result = await saveCsgDraft(body.state)
    return NextResponse.json({ ok: true, branch: result.branch, commitSha: result.sha })
  } catch (error) {
    const status = error instanceof CsgGitError ? error.status : 500
    return NextResponse.json({ ok: false, error: error instanceof Error ? error.message : 'Draft save failed.' }, { status })
  }
}
