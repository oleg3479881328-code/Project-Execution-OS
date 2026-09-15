'use client'

import { useEffect, type ReactNode } from 'react'
import { useGetPuck, type Plugin } from '@puckeditor/core'

type ImagePatchDetail = {
  blockId?: string
  patch?: Record<string, unknown>
}

function ImagePatchBridge({ children }: { children: ReactNode }) {
  const getPuck = useGetPuck()

  useEffect(() => {
    const onImagePatch = (event: Event) => {
      const detail = (event as CustomEvent<ImagePatchDetail>).detail
      if (!detail?.blockId || !detail.patch) return

      const puck = getPuck()
      const selector = puck.getSelectorForId(detail.blockId)
      const current = puck.getItemById(detail.blockId)

      if (!selector?.zone || !current) return

      // Match Puck's own field editing path: update only the selected node.
      // Whole-tree setData updates are intentionally avoided here because Puck
      // documents them as expensive and they can reset transient editor state.
      puck.dispatch({
        type: 'replace',
        destinationIndex: selector.index,
        destinationZone: selector.zone,
        data: {
          ...current,
          props: {
            ...current.props,
            ...detail.patch,
          },
        },
        ui: { itemSelector: selector },
      })

      // The replace action can remount the rendered component even though its
      // Puck selection is preserved. Olga's image controls are event-driven, so
      // re-emit the same activation after React commits the replacement. This
      // keeps the photograph selected for sequential crop/shape/zoom edits.
      window.requestAnimationFrame(() => {
        window.dispatchEvent(
          new CustomEvent('wc-image-layout-activate', {
            detail: { blockId: detail.blockId },
          }),
        )
      })
    }

    window.addEventListener('wc-image-layout-change', onImagePatch)
    return () => window.removeEventListener('wc-image-layout-change', onImagePatch)
  }, [getPuck])

  return <>{children}</>
}

export const imageEditorPlugin: Plugin = {
  name: 'website-creator-image-editor',
  overrides: {
    puck: ({ children }) => <ImagePatchBridge>{children}</ImagePatchBridge>,
  },
}
