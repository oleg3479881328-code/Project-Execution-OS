import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

import { CSG_EDITOR_COOKIE, verifyEditorSession } from '@/csg/auth'
import { approvedCsgMedia, CsgGitError, uploadCsgMedia } from '@/csg/github'

export const runtime = 'nodejs'

export async function GET() {
  const docs = approvedCsgMedia()
  return NextResponse.json({ docs, totalDocs: docs.length, hasNextPage: false, page: 1, totalPages: 1 })
}

export async function POST(request: Request) {
  const session = (await cookies()).get(CSG_EDITOR_COOKIE)?.value
  if (!verifyEditorSession(session)) return NextResponse.json({ ok: false, error: 'Editor session expired.' }, { status: 401 })
  const form = await request.formData()
  const file = form.get('file')
  if (!(file instanceof File)) return NextResponse.json({ ok: false, error: 'Image file is required.' }, { status: 400 })
  try {
    const result = await uploadCsgMedia(file, String(form.get('alt') || ''))
    return NextResponse.json({ doc: result, ok: true })
  } catch (error) {
    const status = error instanceof CsgGitError ? error.status : 500
    return NextResponse.json({ ok: false, error: error instanceof Error ? error.message : 'Upload failed.' }, { status })
  }
}
