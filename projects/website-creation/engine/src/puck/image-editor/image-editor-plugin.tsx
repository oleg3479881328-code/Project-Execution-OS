'use client'

import { useEffect, type ReactNode } from 'react'
import { createUsePuck, type Data, type Plugin } from '@puckeditor/core'

const usePuck = createUsePuck()

type ImagePatchDetail = {
  blockId?: string
  patch?: Record<string, unknown>
}

function ImagePatchBridge({ children }: { children: ReactNode }) {
  const data = usePuck((state) => state.appState.data)
  const dispatch = usePuck((state) => state.dispatch)

  useEffect(() => {
    const onImagePatch = (event: Event) => {
      const detail = (event as CustomEvent<ImagePatchDetail>).detail
      if (!detail?.blockId || !detail.patch) return

      const next = {
        ...data,
        content: (data.content ?? []).map((block) =>
          block.props?.id === detail.blockId
            ? { ...block, props: { ...block.props, ...detail.patch } }
            : block
        ),
      } as Data

      dispatch({ type: 'setData', data: next })
    }

    window.addEventListener('wc-image-layout-change', onImagePatch)
    return () => window.removeEventListener('wc-image-layout-change', onImagePatch)
  }, [data, dispatch])

  return <>{children}</>
}

export const imageEditorPlugin: Plugin = {
  name: 'website-creator-image-editor',
  overrides: {
    puck: ({ children }) => <ImagePatchBridge>{children}</ImagePatchBridge>,
  },
}
