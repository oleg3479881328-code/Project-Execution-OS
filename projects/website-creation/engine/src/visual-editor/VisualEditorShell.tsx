'use client'

import { Puck, type Data } from '@puckeditor/core'
import type { ComponentProps } from 'react'
import { useState } from 'react'

import type { VisualEditorSaveResult } from './adapter-types'

type PuckProps = ComponentProps<typeof Puck>

type Props = {
  config: PuckProps['config']
  initialData: Data
  title: string
  publicPath?: string
  durable?: boolean
  initialStatus?: string
  plugins?: PuckProps['plugins']
  viewports?: PuckProps['viewports']
  onSaveDraft: (data: Data) => Promise<VisualEditorSaveResult>
  onPublish?: (data: Data) => Promise<VisualEditorSaveResult>
}

const DEFAULT_VIEWPORTS: NonNullable<PuckProps['viewports']> = [
  { label: 'Desktop', width: 1440, height: 900, icon: 'Monitor' },
  { label: 'Tablet', width: 768, height: 1024, icon: 'Tablet' },
  { label: 'Mobile', width: 390, height: 844, icon: 'Smartphone' },
]

function resultMessage(result: VisualEditorSaveResult, fallback: string) {
  if (result.message) return result.message
  if (result.version) return `${fallback} · ${result.version}`
  return fallback
}

export default function VisualEditorShell({
  config,
  initialData,
  title,
  publicPath = '/',
  durable = true,
  initialStatus,
  plugins,
  viewports = DEFAULT_VIEWPORTS,
  onSaveDraft,
  onPublish,
}: Props) {
  const [data, setData] = useState<Data>(initialData)
  const [status, setStatus] = useState(
    initialStatus ?? (durable ? 'Editor ready.' : 'Durable editor persistence is not configured.'),
  )
  const [busy, setBusy] = useState(false)

  async function saveDraft(nextData = data) {
    setBusy(true)
    try {
      const result = await onSaveDraft(nextData)
      if (!result.ok) throw new Error(result.message || 'Draft save failed.')
      setStatus(resultMessage(result, 'Draft saved.'))
      return true
    } catch (error) {
      setStatus(error instanceof Error ? error.message : 'Draft save failed.')
      return false
    } finally {
      setBusy(false)
    }
  }

  async function publish(nextData: Data) {
    setData(nextData)
    if (!onPublish) {
      await saveDraft(nextData)
      return
    }

    setBusy(true)
    try {
      const result = await onPublish(nextData)
      if (!result.ok) throw new Error(result.message || 'Publish failed.')
      setStatus(resultMessage(result, 'Published.'))
    } catch (error) {
      setStatus(error instanceof Error ? error.message : 'Publish failed.')
    } finally {
      setBusy(false)
    }
  }

  return (
    <div className="visual-editor-shell">
      <div className="visual-editor-status" role="status" aria-live="polite">
        <span>{status}</span>
        <button type="button" onClick={() => void saveDraft()} disabled={busy || !durable}>
          {busy ? 'Working…' : 'Save draft'}
        </button>
        {onPublish ? (
          <button type="button" onClick={() => void publish(data)} disabled={busy || !durable}>
            Publish
          </button>
        ) : null}
      </div>
      <Puck
        config={config}
        data={data}
        onChange={setData}
        onPublish={publish}
        plugins={plugins}
        headerTitle={title}
        headerPath={publicPath}
        viewports={viewports}
      />
    </div>
  )
}
