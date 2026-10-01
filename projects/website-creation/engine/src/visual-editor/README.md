# Reusable visual editor

This module is the project-neutral Puck editing shell for existing Next.js projects deployed on Vercel.

It is intentionally small. A project keeps ownership of its auth, page state, API routes, React components, and deployment path. The shared editor only owns the editing UI and the draft/publish interaction contract.

## What a Vercel project supplies

1. `config` — the Puck config that registers the project's editable React components.
2. `initialData` — the current Puck `Data` for the page.
3. `onSaveDraft(data)` — persistence for a draft.
4. `onPublish(data)` — optional publish operation when publish is distinct from draft save.
5. Optional editor plugins, viewport presets, title, and public path.

## Minimal client adapter

```tsx
'use client'

import type { Data } from '@puckeditor/core'
import VisualEditorShell from '@/visual-editor/VisualEditorShell'
import { projectPuckConfig } from './project-puck-config'

export default function ProjectEditor({ initialData }: { initialData: Data }) {
  return (
    <VisualEditorShell
      config={projectPuckConfig}
      initialData={initialData}
      title="Project editor"
      publicPath="/"
      onSaveDraft={async (data) => {
        const response = await fetch('/api/editor/draft', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ data }),
        })
        return response.ok
          ? { ok: true, message: 'Draft saved.' }
          : { ok: false, message: 'Draft save failed.' }
      }}
      onPublish={async (data) => {
        const response = await fetch('/api/editor/publish', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ data }),
        })
        return response.ok
          ? { ok: true, message: 'Published.' }
          : { ok: false, message: 'Publish failed.' }
      }}
    />
  )
}
```

The route `/editor` remains project-owned. It may authenticate the owner, load the page state, and then render the client adapter above.

## Public/editor parity rule

The public page must render the same canonical Puck data with the same registered component implementations. Do not create a second visual-only renderer for the editor.

## Existing proof

`src/csg/CsgPuckEditor.tsx` is now a thin adapter around this shell. Its GitHub staging/publish routes and image plugin remain CSG/project bindings; the Puck shell is shared.

## Non-goals

This module does not add a CMS, change the Vercel deployment route, infer arbitrary React source code, or introduce project-domain entities. It only makes the already adopted Puck editor reusable across Vercel/Next.js projects that expose editable components and page state.
