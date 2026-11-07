'use client'

import type { Data } from '@puckeditor/core'

import { csgWebsiteEditorConfig } from '@/puck/editor-config.client'
import { imageEditorPlugin } from '@/puck/image-editor/image-editor-plugin'
import type { SiteInstanceV01 } from '@/site-model/types'
import VisualEditorShell from '@/visual-editor/VisualEditorShell'
import type { VisualEditorSaveResult } from '@/visual-editor/adapter-types'

type Props = {
  initialSite: SiteInstanceV01
  durable: boolean
}

type ApiResult = {
  ok?: boolean
  error?: string
  commitSha?: string
  branch?: string
  merged?: boolean
}

export default function CsgPuckEditor({ initialSite, durable }: Props) {
  const initialData = initialSite.pages[0]?.puckData as Data

  function withPageData(data: Data): SiteInstanceV01 {
    return {
      ...initialSite,
      pages: initialSite.pages.map((page, index) => (
        index === 0
          ? { ...page, puckData: data as SiteInstanceV01['pages'][number]['puckData'] }
          : page
      )),
    }
  }

  async function saveDraft(data: Data): Promise<VisualEditorSaveResult> {
    try {
      const response = await fetch('/api/csg/draft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: withPageData(data) }),
      })
      const result = await response.json() as ApiResult
      if (!response.ok) return { ok: false, message: result.error || 'Draft save failed.' }

      return {
        ok: true,
        message: `Draft saved to ${result.branch || 'GitHub staging'}.`,
        version: result.commitSha?.slice(0, 7),
      }
    } catch (error) {
      return { ok: false, message: error instanceof Error ? error.message : 'Draft save failed.' }
    }
  }

  async function publish(data: Data): Promise<VisualEditorSaveResult> {
    try {
      const draftResponse = await fetch('/api/csg/draft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: withPageData(data) }),
      })
      const draftResult = await draftResponse.json() as ApiResult
      if (!draftResponse.ok) return { ok: false, message: draftResult.error || 'Draft save failed.' }

      const response = await fetch('/api/csg/publish', { method: 'POST' })
      const result = await response.json() as ApiResult
      if (!response.ok) return { ok: false, message: result.error || 'Publish failed.' }

      const version = result.commitSha?.slice(0, 7)
      return {
        ok: true,
        message: `Published to GitHub/${result.branch || 'main'}${version ? ` · ${version}` : ''} · Vercel deployment follows Git.`,
        version,
      }
    } catch (error) {
      return { ok: false, message: error instanceof Error ? error.message : 'Publish failed.' }
    }
  }

  return (
    <VisualEditorShell
      config={csgWebsiteEditorConfig}
      initialData={initialData}
      title="Car Service Garage"
      publicPath="/"
      durable={durable}
      initialStatus={durable ? 'Loaded GitHub staging state.' : 'GitHub editor persistence is not configured.'}
      plugins={[imageEditorPlugin]}
      onSaveDraft={saveDraft}
      onPublish={publish}
    />
  )
}
