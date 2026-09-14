'use client'

import { PuckConfigProvider } from '@delmaredigital/payload-puck/client'
import { websiteEditorConfig } from '@/puck/editor-config'

export default function PuckProvider({ children }: { children: React.ReactNode }) {
  return <PuckConfigProvider config={websiteEditorConfig}>{children}</PuckConfigProvider>
}
