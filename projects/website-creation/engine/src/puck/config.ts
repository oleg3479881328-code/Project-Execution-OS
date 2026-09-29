import { baseConfig, extendConfig } from '@delmaredigital/payload-puck/config'
import { marketingComponents, marketingComponentNames } from './marketing-components'
import { websiteComponents, websiteComponentNames } from './website-components'

export const websiteConfig = extendConfig({
  base: baseConfig,
  components: {
    ...websiteComponents,
    ...marketingComponents,
  },
  categories: {
    website: {
      title: 'Website Sections',
      components: [...marketingComponentNames, ...websiteComponentNames],
      defaultExpanded: true,
    },
  },
})
