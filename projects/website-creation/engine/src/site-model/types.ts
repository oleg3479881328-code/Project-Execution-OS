export type SiteContact = {
  phone?: string
  phoneDisplay?: string
  address?: string
  mapUrl?: string
}

export type SiteTheme = {
  colors: {
    background: string
    surface: string
    text: string
    muted: string
    accent: string
  }
}

export type SitePageSeed = {
  title: string
  slug: string
  isHomepage?: boolean
  meta?: {
    title?: string
    description?: string
  }
  puckData: {
    root: { props: Record<string, unknown> }
    content: Array<{ type: string; props: Record<string, unknown> }>
  }
}

export type SiteInstanceV01 = {
  schemaVersion: '0.1-draft'
  siteId: string
  business: {
    name: string
    kind: string
    locationLabel?: string
    contact: SiteContact
  }
  theme: SiteTheme
  pages: SitePageSeed[]
}
