'use client'

import { useLayoutEffect, useRef } from 'react'
import { createUsePuck } from '@puckeditor/core'
import EditableImageFrame from './EditableImageFrame'
import type { ComponentProps } from 'react'

const usePuck = createUsePuck()

type Props = ComponentProps<typeof EditableImageFrame>

export default function PersistentEditableImageFrame(props: Props) {
  const hostRef = useRef<HTMLDivElement | null>(null)
  const selectedId = usePuck((state) => state.selectedItem?.props?.id)

  useLayoutEffect(() => {
    if (selectedId !== props.blockId) return

    // Puck may remount a rendered component after an atomic `replace` update.
    // Olga's image frame owns transient `active` state locally, so restore that
    // state immediately from Puck's canonical selection instead of inventing a
    // second selection model. This preserves the proven Olga interaction while
    // adapting it to Payload/Puck's iframe renderer.
    const frame = hostRef.current?.querySelector<HTMLElement>('.wc-image-frame')
    if (!frame) return

    const raf = window.requestAnimationFrame(() => frame.click())
    return () => window.cancelAnimationFrame(raf)
  })

  return (
    <div ref={hostRef} style={{ display: 'contents' }}>
      <EditableImageFrame {...props} />
    </div>
  )
}
