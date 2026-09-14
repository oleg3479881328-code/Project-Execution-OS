'use client'

import { PuckConfigProvider } from '@delmaredigital/payload-puck/client'
import { websiteEditorConfig } from '@/puck/editor-config'
import { imageEditorPlugin } from '@/puck/image-editor/image-editor-plugin'

export default function PuckProvider({ children }: { children: React.ReactNode }) {
  return (
    <PuckConfigProvider config={websiteEditorConfig} plugins={[imageEditorPlugin]}>
      {children}
    </PuckConfigProvider>
  )
}
