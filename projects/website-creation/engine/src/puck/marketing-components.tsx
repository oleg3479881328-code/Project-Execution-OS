import type { ComponentConfig } from '@puckeditor/core'
import React from 'react'

type NavItem = { label?: string; href?: string }
type TrustItem = { symbol?: string; title?: string; body?: string }
type BenefitItem = { symbol?: string; title?: string; body?: string }
type TestimonialItem = { quote?: string; name?: string; detail?: string }

export const HeaderSectionConfig: ComponentConfig<any> = {
  label: 'Header',
  fields: {
    brand: { type: 'text', label: 'Brand' },
    subBrand: { type: 'text', label: 'Sub-brand' },
    nav: {
      type: 'array',
      label: 'Navigation',
      arrayFields: {
        label: { type: 'text', label: 'Label' },
        href: { type: 'text', label: 'URL / anchor' },
      },
      defaultItemProps: (index: number) => ({ label: `Link ${index + 1}`, href: '#' }),
      getItemSummary: (item: NavItem) => item.label || 'Navigation link',
    },
    phoneLabel: { type: 'text', label: 'Phone label' },
    phoneHref: { type: 'text', label: 'Phone URL' },
    note: { type: 'text', label: 'Phone note' },
    ctaLabel: { type: 'text', label: 'CTA label' },
    ctaHref: { type: 'text', label: 'CTA URL' },
  },
  defaultProps: {
    brand: 'YOUR BUSINESS',
    subBrand: 'SERVICE CENTER',
    nav: [],
    phoneLabel: '(000) 000-0000',
    phoneHref: 'tel:+10000000000',
    note: 'Call before you arrive',
    ctaLabel: 'Schedule service',
    ctaHref: 'tel:+10000000000',
  },
  render: ({ brand, subBrand, nav = [], phoneLabel, phoneHref, note, ctaLabel, ctaHref }) => (
    <header className="wc-site-header" data-wc-section="header">
      <div className="wc-shell wc-site-header__inner">
        <a className="wc-brand" href="#top" aria-label={brand}>
          <span className="wc-brand__mark" aria-hidden="true">⚙</span>
          <span>{brand}<small>{subBrand}</small></span>
        </a>
        <nav className="wc-site-nav" aria-label="Primary navigation">
          {(nav as NavItem[]).map((item, index) => item.label && item.href ? <a key={`${item.label}-${index}`} href={item.href}>{item.label}</a> : null)}
        </nav>
        <div className="wc-site-header__actions">
          <a className="wc-phone" href={phoneHref}><strong>{phoneLabel}</strong><small>{note}</small></a>
          <a className="wc-button wc-button--compact" href={ctaHref}>{ctaLabel}</a>
        </div>
      </div>
    </header>
  ),
}

export const TrustStripSectionConfig: ComponentConfig<any> = {
  label: 'Trust strip',
  fields: {
    items: {
      type: 'array',
      label: 'Trust items',
      arrayFields: {
        symbol: { type: 'text', label: 'Symbol' },
        title: { type: 'text', label: 'Title' },
        body: { type: 'text', label: 'Body' },
      },
      defaultItemProps: (index: number) => ({ symbol: '✓', title: `Benefit ${index + 1}`, body: 'Short proof point' }),
      getItemSummary: (item: TrustItem) => item.title || 'Trust item',
    },
  },
  defaultProps: { items: [] },
  render: ({ items = [] }) => (
    <section className="wc-trust-strip" data-wc-section="trust-strip">
      <div className="wc-shell wc-trust-strip__grid">
        {(items as TrustItem[]).map((item, index) => (
          <div className="wc-trust-item" key={`${item.title || 'trust'}-${index}`}>
            <span aria-hidden="true">{item.symbol || '✓'}</span>
            <div><strong>{item.title}</strong><small>{item.body}</small></div>
          </div>
        ))}
      </div>
    </section>
  ),
}

export const BenefitsSectionConfig: ComponentConfig<any> = {
  label: 'Benefits',
  fields: {
    heading: { type: 'text', label: 'Heading' },
    items: {
      type: 'array',
      label: 'Benefits',
      arrayFields: {
        symbol: { type: 'text', label: 'Symbol' },
        title: { type: 'text', label: 'Title' },
        body: { type: 'text', label: 'Body' },
      },
      defaultItemProps: (index: number) => ({ symbol: '✓', title: `Benefit ${index + 1}`, body: 'Short supporting statement' }),
      getItemSummary: (item: BenefitItem) => item.title || 'Benefit',
    },
  },
  defaultProps: { heading: 'Why choose us', items: [] },
  render: ({ heading, items = [] }) => (
    <section className="wc-benefits" id="why" data-wc-section="benefits">
      <div className="wc-shell wc-benefits__inner">
        <h2>{heading}</h2>
        <div className="wc-benefits__grid">
          {(items as BenefitItem[]).map((item, index) => (
            <article key={`${item.title || 'benefit'}-${index}`}>
              <span aria-hidden="true">{item.symbol || '✓'}</span>
              <div><strong>{item.title}</strong><p>{item.body}</p></div>
            </article>
          ))}
        </div>
      </div>
    </section>
  ),
}

export const TestimonialsContactSectionConfig: ComponentConfig<any> = {
  label: 'Testimonials + Contact',
  fields: {
    heading: { type: 'text', label: 'Reviews heading' },
    testimonials: {
      type: 'array',
      label: 'Testimonials',
      arrayFields: {
        quote: { type: 'textarea', label: 'Quote' },
        name: { type: 'text', label: 'Name' },
        detail: { type: 'text', label: 'Detail' },
      },
      defaultItemProps: (index: number) => ({ quote: 'Clear communication and careful service.', name: `Customer ${index + 1}`, detail: 'Local driver' }),
      getItemSummary: (item: TestimonialItem) => item.name || 'Testimonial',
    },
    contactHeading: { type: 'text', label: 'Contact heading' },
    address: { type: 'textarea', label: 'Address' },
    phoneLabel: { type: 'text', label: 'Phone label' },
    phoneHref: { type: 'text', label: 'Phone URL' },
    note: { type: 'text', label: 'Note' },
    mapLabel: { type: 'text', label: 'Map link label' },
    mapHref: { type: 'text', label: 'Map URL' },
  },
  defaultProps: {
    heading: 'What customers say',
    testimonials: [],
    contactHeading: 'Contact',
    address: 'Street address\nCity, State ZIP',
    phoneLabel: '(000) 000-0000',
    phoneHref: 'tel:+10000000000',
    note: 'Call before you arrive',
    mapLabel: 'Open directions',
    mapHref: '#',
  },
  render: ({ heading, testimonials = [], contactHeading, address, phoneLabel, phoneHref, note, mapLabel, mapHref }) => (
    <section className="wc-section wc-reviews-contact" id="contact" data-wc-section="reviews-contact">
      <div className="wc-shell wc-reviews-contact__grid">
        <div className="wc-reviews">
          <h2>{heading}</h2>
          <div className="wc-reviews__cards">
            {(testimonials as TestimonialItem[]).map((item, index) => (
              <article key={`${item.name || 'review'}-${index}`}>
                <div className="wc-stars" aria-label="5 out of 5 stars">★★★★★</div>
                <p>“{item.quote}”</p>
                <strong>{item.name}</strong>
                <small>{item.detail}</small>
              </article>
            ))}
          </div>
        </div>
        <aside className="wc-contact-card">
          <h2>{contactHeading}</h2>
          <p>{String(address || '').split('\n').map((line, index, all) => <React.Fragment key={`${line}-${index}`}>{line}{index < all.length - 1 ? <br /> : null}</React.Fragment>)}</p>
          <a className="wc-contact-card__phone" href={phoneHref}>{phoneLabel}</a>
          <small>{note}</small>
          <a className="wc-map-card" href={mapHref} target="_blank" rel="noreferrer"><span aria-hidden="true">⌖</span><strong>{mapLabel}</strong></a>
        </aside>
      </div>
    </section>
  ),
}

export const marketingComponents = {
  HeaderSection: HeaderSectionConfig,
  TrustStripSection: TrustStripSectionConfig,
  BenefitsSection: BenefitsSectionConfig,
  TestimonialsContactSection: TestimonialsContactSectionConfig,
}

export const marketingComponentNames = Object.keys(marketingComponents)
