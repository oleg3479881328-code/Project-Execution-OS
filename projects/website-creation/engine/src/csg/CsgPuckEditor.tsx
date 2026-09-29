'use client'

import { Puck, type Data } from '@puckeditor/core'
import { useMemo, useState } from 'react'

import { csgWebsiteEditorConfig } from '@/puck/editor-config.client'
import { imageEditorPlugin } from '@/puck/image-editor/image-editor-plugin'
import type { SiteInstanceV01 } from '@/site-model/types'

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
  const [data, setData] = useState<Data>(initialData)
  const [status, setStatus] = useState(durable ? 'Loaded GitHub staging state.' : 'GitHub editor persistence is not configured.')
  const [busy, setBusy] = useState(false)

  const currentSite = useMemo<SiteInstanceV01>(() => ({
    ...initialSite,
    pages: initialSite.pages.map((page, index) => index === 0 ? { ...page, puckData: data as SiteInstanceV01['pages'][number]['puckData'] } : page),
  }), [data, initialSite])

  async function saveDraft(nextSite = currentSite) {
    setBusy(true)
    try {
      const response = await fetch('/api/csg/draft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: nextSite }),
      })
      const result = await response.json() as ApiResult
      if (!response.ok) throw new Error(result.error || 'Draft save failed.')
      setStatus(`Draft saved to ${result.branch || 'GitHub staging'}.`)
      return true
    } catch (error) {
      setStatus(error instanceof Error ? error.message : 'Draft save failed.')
      return false
    } finally {
      setBusy(false)
    }
  }

  async function publish(nextData: Data) {
    const nextSite: SiteInstanceV01 = {
      ...initialSite,
      pages: initialSite.pages.map((page, index) => index === 0 ? { ...page, puckData: nextData as SiteInstanceV01['pages'][number]['puckData'] } : page),
    }
    setData(nextData)
    setBusy(true)
    try {
      const draftResponse = await fetch('/api/csg/draft', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ state: nextSite }),
      })
      const draftResult = await draftResponse.json() as ApiResult
      if (!draftResponse.ok) throw new Error(draftResult.error || 'Draft save failed.')

      const response = await fetch('/api/csg/publish', { method: 'POST' })
      const result = await response.json() as ApiResult
      if (!response.ok) throw new Error(result.error || 'Publish failed.')
      setStatus(`Published to GitHub/${result.branch || 'main'} · ${result.commitSha?.slice(0, 7) || 'commit'} · Vercel deployment follows Git.`)
    } catch (error) {
      setStatus(error instanceof Error ? error.message : 'Publish failed.')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="csg-editor-shell">
      <div className="csg-editor-status" role="status" aria-live="polite">
        <span>{status}</span>
        <button type="button" onClick={() => void saveDraft()} disabled={busy || !durable}>
          {busy ? 'Working…' : 'Save draft'}
        </button>
        <button type="button" onClick={() => void publish(data)} disabled={busy || !durable}>
          Publish
        </button>
      </div>
      <Puck
        config={csgWebsiteEditorConfig}
        data={data}
        onChange={setData}
        onPublish={publish}
        plugins={[imageEditorPlugin]}
        headerTitle="Car Service Garage"
        headerPath="/"
        viewports={[
          { label: 'Desktop', width: 1440, height: 900, icon: 'Monitor' },
          { label: 'Tablet', width: 768, height: 1024, icon: 'Tablet' },
          { label: 'Mobile', width: 390, height: 844, icon: 'Smartphone' },
        ]}
      />
    </div>
  )
}
