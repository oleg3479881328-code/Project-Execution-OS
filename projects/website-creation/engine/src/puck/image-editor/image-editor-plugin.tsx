'use client'

import { useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react'
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

function ImageFieldsSlot({ children }: { children: ReactNode }) {
  const slotRef = useRef<HTMLDivElement | null>(null)
  const [visible, setVisible] = useState(false)

  useLayoutEffect(() => {
    const slot = slotRef.current
    if (!slot) return

    const syncVisibility = () => {
      setVisible(slot.getClientRects().length > 0 && slot.offsetWidth > 0)
    }

    syncVisibility()

    const OwnerResizeObserver = slot.ownerDocument.defaultView?.ResizeObserver
    if (!OwnerResizeObserver) return

    const observer = new OwnerResizeObserver(syncVisibility)
    observer.observe(slot)
    return () => observer.disconnect()
  }, [])

  return (
    <>
      <div
        ref={slotRef}
        data-wc-image-inspector-slot={visible ? '' : undefined}
        style={{ minHeight: 1, width: '100%' }}
      />
      {children}
    </>
  )
}

export const imageEditorPlugin: Plugin = {
  name: 'website-creator-image-editor',
  overrides: {
    puck: ({ children }) => <ImagePatchBridge>{children}</ImagePatchBridge>,
    // Puck's official `fields` override is the native extension point for the
    // right-hand fields panel. Puck can keep multiple field panels mounted for
    // responsive/editor states, so only the actually visible host advertises
    // the image-inspector slot. This keeps IMAGE inside native layout without
    // floating over Save / Publish or portalling into a hidden panel.
    fields: ({ children }) => <ImageFieldsSlot>{children}</ImageFieldsSlot>,
  },
}
