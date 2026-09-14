import type { ComponentConfig } from '@puckeditor/core'
import React from 'react'

type LinkProps = {
  label?: string
  href?: string
  secondary?: boolean
}

function ActionLink({ label, href, secondary = false }: LinkProps) {
  if (!label || !href) return null
  return (
    <a className={secondary ? 'wc-button wc-button--secondary' : 'wc-button'} href={href}>
      {label}
    </a>
  )
}

export const HeroSectionConfig: ComponentConfig<any> = {
  label: 'Hero',
  fields: {
    eyebrow: { type: 'text', label: 'Eyebrow' },
    title: { type: 'text', label: 'Title' },
    highlight: { type: 'text', label: 'Highlighted word / phrase' },
    body: { type: 'textarea', label: 'Body' },
    primaryLabel: { type: 'text', label: 'Primary CTA label' },
    primaryHref: { type: 'text', label: 'Primary CTA URL' },
    secondaryLabel: { type: 'text', label: 'Secondary CTA label' },
    secondaryHref: { type: 'text', label: 'Secondary CTA URL' },
    imageUrl: { type: 'text', label: 'Image URL (optional)' },
    imageAlt: { type: 'text', label: 'Image alt text' },
  },
  defaultProps: {
    eyebrow: 'Independent service · Local experts',
    title: 'Clear work. Better outcomes.',
    highlight: 'Better outcomes.',
    body: 'Explain the problem, verify the cause, and make the next step easy to understand.',
    primaryLabel: 'Call now',
    primaryHref: 'tel:+10000000000',
    secondaryLabel: 'Explore services',
    secondaryHref: '#services',
    imageUrl: '',
    imageAlt: '',
  },
  render: ({ eyebrow, title, highlight, body, primaryLabel, primaryHref, secondaryLabel, secondaryHref, imageUrl, imageAlt }) => {
    const highlightedTitle = highlight && title.includes(highlight)
      ? <>{title.slice(0, title.indexOf(highlight))}<span>{highlight}</span>{title.slice(title.indexOf(highlight) + highlight.length)}</>
      : title

    return (
      <section className="wc-hero" data-wc-section="hero">
        <div className="wc-shell wc-hero__grid">
          <div className="wc-hero__copy">
            <div className="wc-eyebrow">{eyebrow}</div>
            <h1>{highlightedTitle}</h1>
            <p>{body}</p>
            <div className="wc-actions">
              <ActionLink label={primaryLabel} href={primaryHref} />
              <ActionLink label={secondaryLabel} href={secondaryHref} secondary />
            </div>
          </div>
          <div className="wc-hero__visual" aria-hidden={!imageUrl}>
            {imageUrl ? <img src={imageUrl} alt={imageAlt || ''} /> : <div className="wc-hero__visual-placeholder">SERVICE / CRAFT / TRUST</div>}
          </div>
        </div>
      </section>
    )
  },
}

type ServiceItem = {
  kicker?: string
  title?: string
  body?: string
  actionLabel?: string
  actionHref?: string
}

export const ServicesSectionConfig: ComponentConfig<any> = {
  label: 'Services',
  fields: {
    eyebrow: { type: 'text', label: 'Eyebrow' },
    heading: { type: 'text', label: 'Heading' },
    intro: { type: 'textarea', label: 'Intro' },
    services: {
      type: 'array',
      label: 'Services',
      arrayFields: {
        kicker: { type: 'text', label: 'Kicker' },
        title: { type: 'text', label: 'Title' },
        body: { type: 'textarea', label: 'Description' },
        actionLabel: { type: 'text', label: 'Action label' },
        actionHref: { type: 'text', label: 'Action URL' },
      },
      defaultItemProps: (index: number) => ({
        kicker: String(index + 1).padStart(2, '0'),
        title: `Service ${index + 1}`,
        body: 'Describe this service and the customer outcome.',
        actionLabel: 'Learn more',
        actionHref: '#contact',
      }),
      getItemSummary: (item: ServiceItem) => item.title || 'Untitled service',
    },
  },
  defaultProps: {
    eyebrow: 'Capabilities',
    heading: 'Explore our services',
    intro: 'A focused set of services built around solving the actual problem.',
    services: [],
  },
  render: ({ eyebrow, heading, intro, services = [] }) => (
    <section className="wc-section wc-services" id="services" data-wc-section="services">
      <div className="wc-shell">
        <div className="wc-section-head">
          <div>
            <div className="wc-eyebrow wc-eyebrow--accent">{eyebrow}</div>
            <h2>{heading}</h2>
          </div>
          <p>{intro}</p>
        </div>
        <div className="wc-services__grid">
          {(services as ServiceItem[]).map((service, index) => (
            <article className="wc-service-card" key={`${service.title || 'service'}-${index}`}>
              <div className="wc-service-card__kicker">{service.kicker || String(index + 1).padStart(2, '0')}</div>
              <h3>{service.title}</h3>
              <p>{service.body}</p>
              {service.actionLabel && service.actionHref ? <a href={service.actionHref}>{service.actionLabel}<span aria-hidden="true"> →</span></a> : null}
            </article>
          ))}
        </div>
      </div>
    </section>
  ),
}

type ProcessStep = {
  number?: string
  title?: string
  body?: string
}

export const ProcessSectionConfig: ComponentConfig<any> = {
  label: 'Process',
  fields: {
    eyebrow: { type: 'text', label: 'Eyebrow' },
    heading: { type: 'text', label: 'Heading' },
    steps: {
      type: 'array',
      label: 'Steps',
      arrayFields: {
        number: { type: 'text', label: 'Number' },
        title: { type: 'text', label: 'Title' },
        body: { type: 'textarea', label: 'Body' },
      },
      defaultItemProps: (index: number) => ({
        number: String(index + 1).padStart(2, '0'),
        title: `Step ${index + 1}`,
        body: 'Explain what happens at this step.',
      }),
      getItemSummary: (item: ProcessStep) => item.title || 'Untitled step',
    },
  },
  defaultProps: {
    eyebrow: 'A simple process',
    heading: 'From problem to solution.',
    steps: [],
  },
  render: ({ eyebrow, heading, steps = [] }) => (
    <section className="wc-section wc-process" data-wc-section="process">
      <div className="wc-shell">
        <div className="wc-eyebrow wc-eyebrow--accent">{eyebrow}</div>
        <h2>{heading}</h2>
        <div className="wc-process__grid">
          {(steps as ProcessStep[]).map((step, index) => (
            <article className="wc-process-step" key={`${step.number || index}-${step.title || ''}`}>
              <div className="wc-process-step__number">{step.number || String(index + 1).padStart(2, '0')}</div>
              <h3>{step.title}</h3>
              <p>{step.body}</p>
            </article>
          ))}
        </div>
      </div>
    </section>
  ),
}

export const CtaSectionConfig: ComponentConfig<any> = {
  label: 'Call to Action',
  fields: {
    eyebrow: { type: 'text', label: 'Eyebrow' },
    heading: { type: 'text', label: 'Heading' },
    body: { type: 'textarea', label: 'Body' },
    primaryLabel: { type: 'text', label: 'Primary CTA label' },
    primaryHref: { type: 'text', label: 'Primary CTA URL' },
    secondaryLabel: { type: 'text', label: 'Secondary CTA label' },
    secondaryHref: { type: 'text', label: 'Secondary CTA URL' },
  },
  defaultProps: {
    eyebrow: 'Ready when you are',
    heading: 'Start with a clear next step.',
    body: 'Call or message before you arrive so the team can plan the right next step.',
    primaryLabel: 'Call now',
    primaryHref: 'tel:+10000000000',
    secondaryLabel: 'Get directions',
    secondaryHref: '#',
  },
  render: ({ eyebrow, heading, body, primaryLabel, primaryHref, secondaryLabel, secondaryHref }) => (
    <section className="wc-section wc-cta" id="contact" data-wc-section="cta">
      <div className="wc-shell">
        <div className="wc-cta__card">
          <div className="wc-eyebrow">{eyebrow}</div>
          <h2>{heading}</h2>
          <p>{body}</p>
          <div className="wc-actions">
            <ActionLink label={primaryLabel} href={primaryHref} />
            <ActionLink label={secondaryLabel} href={secondaryHref} secondary />
          </div>
        </div>
      </div>
    </section>
  ),
}

export const FooterSectionConfig: ComponentConfig<any> = {
  label: 'Footer',
  fields: {
    brand: { type: 'text', label: 'Brand' },
    address: { type: 'textarea', label: 'Address' },
    phoneLabel: { type: 'text', label: 'Phone label' },
    phoneHref: { type: 'text', label: 'Phone URL' },
    tagline: { type: 'text', label: 'Tagline' },
  },
  defaultProps: {
    brand: 'YOUR BUSINESS',
    address: 'Street address\nCity, State ZIP',
    phoneLabel: '(000) 000-0000',
    phoneHref: 'tel:+10000000000',
    tagline: 'Independent local service',
  },
  render: ({ brand, address, phoneLabel, phoneHref, tagline }) => (
    <footer className="wc-footer" data-wc-section="footer">
      <div className="wc-shell">
        <div className="wc-footer__grid">
          <strong>{brand}</strong>
          <div className="wc-footer__meta">
            <span>{String(address || '').split('\n').map((line, index) => <React.Fragment key={`${line}-${index}`}>{line}{index < String(address || '').split('\n').length - 1 ? <br /> : null}</React.Fragment>)}</span>
            {phoneLabel && phoneHref ? <a href={phoneHref}>{phoneLabel}</a> : null}
          </div>
        </div>
        <div className="wc-footer__bottom">{tagline}</div>
      </div>
    </footer>
  ),
}

export const websiteComponents = {
  HeroSection: HeroSectionConfig,
  ServicesSection: ServicesSectionConfig,
  ProcessSection: ProcessSectionConfig,
  CtaSection: CtaSectionConfig,
  FooterSection: FooterSectionConfig,
}

export const websiteComponentNames = Object.keys(websiteComponents)
