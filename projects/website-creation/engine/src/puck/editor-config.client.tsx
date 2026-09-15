'use client'

import type { ComponentConfig } from '@puckeditor/core'
import { editorConfig, extendConfig } from '@delmaredigital/payload-puck/config/editor'
import { createMediaField } from '@delmaredigital/payload-puck/fields'
import PersistentEditableImageFrame from './image-editor/PersistentEditableImageFrame'
import {
  HeroSectionConfig,
  ImageSectionConfig,
  ServicesSectionConfig,
  websiteComponents,
  websiteComponentNames,
} from './website-components'

const heroConfig: ComponentConfig<any> = {
  ...HeroSectionConfig,
  fields: {
    ...HeroSectionConfig.fields,
    image: createMediaField({ label: 'Hero image' }),
  },
  render: ({
    id,
    eyebrow,
    title,
    highlight,
    body,
    primaryLabel,
    primaryHref,
    secondaryLabel,
    secondaryHref,
    image,
    imageAlt,
    imageCredit,
    imageRatio,
    imageFitMode,
    imageZoom,
    imageFocalX,
    imageFocalY,
  }) => {
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
              {primaryLabel && primaryHref ? <a className="wc-button" href={primaryHref}>{primaryLabel}</a> : null}
              {secondaryLabel && secondaryHref ? <a className="wc-button wc-button--secondary" href={secondaryHref}>{secondaryLabel}</a> : null}
            </div>
          </div>
          <PersistentEditableImageFrame
            blockId={id}
            variant="hero"
            image={image ?? null}
            imageAlt={imageAlt || image?.alt || ''}
            caption={imageCredit || ''}
            ratio={imageRatio || 'portrait'}
            fitMode={imageFitMode || 'fill'}
            zoom={imageZoom ?? 1}
            focalX={imageFocalX ?? 50}
            focalY={imageFocalY ?? 50}
            allowLayoutResize={false}
          />
        </div>
      </section>
    )
  },
}

const imageSectionConfig: ComponentConfig<any> = {
  ...ImageSectionConfig,
  fields: {
    ...ImageSectionConfig.fields,
    image: createMediaField({ label: 'Image' }),
  },
  render: ({ id, image, imageAlt, caption, ratio, fitMode, zoom, focalX, focalY, visualWidth, visualAlign }) => (
    <section className="wc-section wc-image-section" data-wc-section="image">
      <div className="wc-shell">
        <PersistentEditableImageFrame
          blockId={id}
          image={image ?? null}
          imageAlt={imageAlt || image?.alt || ''}
          caption={caption || ''}
          ratio={ratio || 'landscape'}
          fitMode={fitMode || 'fill'}
          zoom={zoom ?? 1}
          focalX={focalX ?? 50}
          focalY={focalY ?? 50}
          visualWidth={visualWidth ?? 100}
          visualAlign={visualAlign || 'center'}
        />
      </div>
    </section>
  ),
}

const serviceFields = (ServicesSectionConfig.fields?.services as any)?.arrayFields || {}
const servicesConfig: ComponentConfig<any> = {
  ...ServicesSectionConfig,
  fields: {
    ...ServicesSectionConfig.fields,
    services: {
      ...(ServicesSectionConfig.fields?.services as any),
      arrayFields: {
        ...serviceFields,
        image: createMediaField({ label: 'Service image' }),
      },
    },
  },
}

const editorWebsiteComponents = {
  ...websiteComponents,
  HeroSection: heroConfig,
  ServicesSection: servicesConfig,
  ImageSection: imageSectionConfig,
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
