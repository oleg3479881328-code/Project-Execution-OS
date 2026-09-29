import { NextResponse } from 'next/server'

import { loadEditorState, readCsgState } from '@/csg/github'

export const runtime = 'nodejs'

export async function GET(request: Request) {
  const scope = new URL(request.url).searchParams.get('scope')
  const result = scope === 'published'
    ? { state: await readCsgState('main'), durable: true }
    : await loadEditorState()
  return NextResponse.json(result)
}
