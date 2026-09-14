import type { ComponentConfig } from '@puckeditor/core'
import React from 'react'

type MediaReference = {
  id: string | number
  url: string
  alt?: string
  width?: number
  height?: number
}

type ImageRatio = 'natural' | 'landscape' | 'portrait' | 'square'
type ImageFitMode = 'fill' | 'fit'
type ImageAlign = 'left' | 'center' | 'right'

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

const ratioField = {
  type: 'select' as const,
  label: 'Image shape',
  options: [
    { label: 'Natural', value: 'natural' },
    { label: 'Landscape', value: 'landscape' },
    { label: 'Portrait', value: 'portrait' },
    { label: 'Square', value: 'square' },
  ],
}

const fitModeField = {
  type: 'select' as const,
  label: 'Image fit',
  options: [
    { label: 'Fill frame (crop)', value: 'fill' },
    { label: 'Fit full photograph', value: 'fit' },
  ],
}

function PublicImageFrame({
  image,
  alt,
  caption,
  ratio = 'landscape',
  fitMode = 'fill',
  zoom = 1,
  focalX = 50,
  focalY = 50,
  visualWidth,
  visualAlign = 'center',
  className = '',
}: {
  image?: MediaReference | null
  alt?: string
  caption?: string
  ratio?: ImageRatio
  fitMode?: ImageFitMode
  zoom?: number
  focalX?: number
  focalY?: number
  visualWidth?: number
  visualAlign?: ImageAlign
  className?: string
}) {
  if (!image?.url) return null
  const style = {
    '--wc-image-focal-x': `${focalX}%`,
    '--wc-image-focal-y': `${focalY}%`,
    '--wc-image-zoom': String(zoom),
    ...(typeof visualWidth === 'number' ? { width: `${Math.max(28, Math.min(100, visualWidth))}%` } : {}),
  } as React.CSSProperties

  return (
    <figure className={`wc-public-image ${className}`.trim()} data-ratio={ratio} data-fit={fitMode} data-visual-align={visualAlign} style={style}>
      <div className="wc-public-image__frame" data-ratio={ratio} data-fit={fitMode}>
        <img src={image.url} alt={alt || image.alt || ''} />
      </div>
      {caption ? <figcaption>{caption}</figcaption> : null}
    </figure>
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
    imageAlt: { type: 'text', label: 'Image alt override' },
    imageCredit: { type: 'text', label: 'Image caption / credit' },
    imageRatio: ratioField,
    imageFitMode: fitModeField,
    imageZoom: { type: 'number', label: 'Image zoom', min: 1, max: 3 },
    imageFocalX: { type: 'number', label: 'Image focal X (%)', min: 0, max: 100 },
    imageFocalY: { type: 'number', label: 'Image focal Y (%)', min: 0, max: 100 },
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
    image: null,
    imageAlt: '',
    imageCredit: '',
    imageRatio: 'portrait',
    imageFitMode: 'fill',
    imageZoom: 1,
    imageFocalX: 50,
    imageFocalY: 50,
  },
  render: ({ eyebrow, title, highlight, body, primaryLabel, primaryHref, secondaryLabel, secondaryHref, image, imageAlt, imageCredit, imageRatio, imageFitMode, imageZoom, imageFocalX, imageFocalY }) => {
    const highlightedTitle = highlight && title.includes(highlight)
      ? <>{title.slice(0, title.indexOf(highlight))}<span>{highlight}</span>{title.slice(title.indexOf(highlight) + highlight.length)}</>
      : title
    const heroImage = image as MediaReference | null

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
          {heroImage?.url ? (
            <PublicImageFrame
              image={heroImage}
              alt={imageAlt}
              caption={imageCredit}
              ratio={imageRatio || 'portrait'}
              fitMode={imageFitMode || 'fill'}
              zoom={imageZoom ?? 1}
              focalX={imageFocalX ?? 50}
              focalY={imageFocalY ?? 50}
              className="wc-hero__image"
            />
          ) : (
            <div className="wc-hero__visual"><div className="wc-hero__visual-placeholder">SERVICE / CRAFT / TRUST</div></div>
          )}
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
  image?: MediaReference | null
  imageAlt?: string
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
        imageAlt: { type: 'text', label: 'Image alt' },
      },
      defaultItemProps: (index: number) => ({
        kicker: String(index + 1).padStart(2, '0'),
        title: `Service ${index + 1}`,
        body: 'Describe this service and the customer outcome.',
        actionLabel: 'Learn more',
        actionHref: '#contact',
        image: null,
        imageAlt: '',
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
              {service.image?.url ? <img className="wc-service-card__image" src={service.image.url} alt={service.imageAlt || service.image.alt || ''} /> : null}
              <div className="wc-service-card__body">
                <div className="wc-service-card__kicker">{service.kicker || String(index + 1).padStart(2, '0')}</div>
                <h3>{service.title}</h3>
                <p>{service.body}</p>
                {service.actionLabel && service.actionHref ? <a href={service.actionHref}>{service.actionLabel}<span aria-hidden="true"> →</span></a> : null}
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  ),
}

export const ImageSectionConfig: ComponentConfig<any> = {
  label: 'Image',
  fields: {
    imageAlt: { type: 'text', label: 'Alt text' },
    caption: { type: 'text', label: 'Caption / credit' },
    ratio: ratioField,
    fitMode: fitModeField,
    zoom: { type: 'number', label: 'Zoom', min: 1, max: 3 },
    focalX: { type: 'number', label: 'Focal X (%)', min: 0, max: 100 },
    focalY: { type: 'number', label: 'Focal Y (%)', min: 0, max: 100 },
    visualWidth: { type: 'number', label: 'Width (%)', min: 28, max: 100 },
    visualAlign: {
      type: 'select',
      label: 'Alignment',
      options: [
        { label: 'Left', value: 'left' },
        { label: 'Center', value: 'center' },
        { label: 'Right', value: 'right' },
      ],
    },
  },
  defaultProps: {
    image: null,
    imageAlt: '',
    caption: '',
    ratio: 'landscape',
    fitMode: 'fill',
    zoom: 1,
    focalX: 50,
    focalY: 50,
    visualWidth: 100,
    visualAlign: 'center',
  },
  render: ({ image, imageAlt, caption, ratio, fitMode, zoom, focalX, focalY, visualWidth, visualAlign }) => (
    <section className="wc-section wc-image-section" data-wc-section="image">
      <div className="wc-shell">
        <PublicImageFrame image={image as MediaReference | null} alt={imageAlt} caption={caption} ratio={ratio} fitMode={fitMode} zoom={zoom} focalX={focalX} focalY={focalY} visualWidth={visualWidth} visualAlign={visualAlign} />
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
  ImageSection: ImageSectionConfig,
  ProcessSection: ProcessSectionConfig,
  CtaSection: CtaSectionConfig,
  FooterSection: FooterSectionConfig,
}

export const websiteComponentNames = Object.keys(websiteComponents)
