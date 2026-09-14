import type { Metadata } from 'next'
import type { ReactNode } from 'react'
import '../../../public/site.css'
import '../../../public/image-editor.css'

export const metadata: Metadata = {
  title: 'Website Creator Engine',
}

export default function FrontendLayout({ children }: { children: ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
