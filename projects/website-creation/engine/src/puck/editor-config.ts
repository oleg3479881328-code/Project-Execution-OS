'use client'

import { editorConfig, extendConfig } from '@delmaredigital/payload-puck/config/editor'
import { websiteComponents, websiteComponentNames } from './website-components'

export const websiteEditorConfig = extendConfig({
  base: editorConfig,
  components: websiteComponents,
  categories: {
    website: {
      title: 'Website Sections',
      components: websiteComponentNames,
      defaultExpanded: true,
    },
  },
})
