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

      // Puck documents `setData` as an expensive whole-tree replacement and
      // recommends atomic actions where possible. Replacing the selected node
      // keeps its id and itemSelector stable, matching the proven Olga editor
      // behavior where a photograph remains active across sequential edits.
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
