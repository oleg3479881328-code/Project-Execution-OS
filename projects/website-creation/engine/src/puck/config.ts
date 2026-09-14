import { baseConfig, extendConfig } from '@delmaredigital/payload-puck/config'
import { websiteComponents, websiteComponentNames } from './website-components'

export const websiteConfig = extendConfig({
  base: baseConfig,
  components: websiteComponents,
  categories: {
    website: {
      title: 'Website Sections',
      components: websiteComponentNames,
      defaultExpanded: true,
    },
  },
})
