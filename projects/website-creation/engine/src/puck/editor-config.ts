'use client'

import { editorConfig, extendConfig } from '@delmaredigital/payload-puck/config/editor'
import { createMediaField } from '@delmaredigital/payload-puck/fields'
import { HeroSectionConfig, websiteComponents, websiteComponentNames } from './website-components'

const editorWebsiteComponents = {
  ...websiteComponents,
  HeroSection: {
    ...HeroSectionConfig,
    fields: {
      ...HeroSectionConfig.fields,
      image: createMediaField({ label: 'Hero image' }),
    },
  },
}

export const websiteEditorConfig = extendConfig({
  base: editorConfig,
  components: editorWebsiteComponents,
  categories: {
    website: {
      title: 'Website Sections',
      components: websiteComponentNames,
      defaultExpanded: true,
    },
  },
})
