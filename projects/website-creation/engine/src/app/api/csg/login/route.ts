import { cookies } from 'next/headers'
import { NextResponse } from 'next/server'

import { CSG_EDITOR_COOKIE, createEditorSession, editorUsername, isEditorAuthConfigured, verifyEditorCredentials } from '@/csg/auth'

export const runtime = 'nodejs'

export async function POST(request: Request) {
  if (!isEditorAuthConfigured()) {
    return NextResponse.json({ ok: false, setupRequired: true, error: 'CSG_EDITOR_PASSWORD and CSG_EDITOR_SESSION_SECRET are required.' }, { status: 503 })
  }
  const body = await request.json().catch(() => ({})) as { username?: string; password?: string }
  if (!verifyEditorCredentials(String(body.username || ''), String(body.password || ''))) {
    return NextResponse.json({ ok: false, error: 'Invalid editor credentials.' }, { status: 401 })
  }
  const response = NextResponse.json({ ok: true, username: editorUsername() })
  response.cookies.set(CSG_EDITOR_COOKIE, createEditorSession(), {
    httpOnly: true,
    sameSite: 'lax',
    secure: process.env.NODE_ENV === 'production',
    path: '/',
    maxAge: 60 * 60 * 24 * 30,
  })
  return response
}

export async function DELETE() {
  const response = NextResponse.json({ ok: true })
  response.cookies.delete(CSG_EDITOR_COOKIE)
  return response
}
