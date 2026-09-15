'use client'

import { useEffect, type ReactNode } from 'react'
import { useGetPuck, type Plugin } from '@puckeditor/core'

type ImagePatchDetail = {
  blockId?: string
  patch?: Record<string, unknown>
}

function emitImageActivation(blockId: string) {
  const eventName = 'wc-image-layout-activate'
  const makeEvent = () => new CustomEvent(eventName, { detail: { blockId } })

  // The Payload/Puck editor renders the page canvas in a same-origin iframe.
  // The proven Olga image component listens inside that canvas, while this
  // bridge runs in Puck's editor shell. Broadcast to both sides of the boundary.
  try {
    window.dispatchEvent(makeEvent())
  } catch {
    // Best-effort bridge; the iframe dispatch below is the important path.
  }

  try {
    if (window.parent && window.parent !== window) {
      window.parent.dispatchEvent(makeEvent())
    }
  } catch {
    // Ignore cross-origin access. Website Creator's own editor is same-origin.
  }

  try {
    for (const frame of Array.from(document.querySelectorAll('iframe'))) {
      frame.contentWindow?.dispatchEvent(makeEvent())
    }
  } catch {
    // Ignore an inaccessible iframe rather than breaking the edit operation.
  }
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

      // `replace` can remount the rendered component even though Puck keeps the
      // same selected node. Olga's image controls are event-driven. Re-activate
      // the same image after the replacement has committed, including inside
      // Puck's canvas iframe, so sequential shape/crop/zoom edits stay active.
      window.requestAnimationFrame(() => {
        window.requestAnimationFrame(() => emitImageActivation(detail.blockId!))
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
