import type { MediaReference } from '@delmaredigital/payload-puck/fields'

export type ImageRatio = 'natural' | 'landscape' | 'portrait' | 'square'
export type ImageFitMode = 'fill' | 'fit'
export type ImageAlign = 'left' | 'center' | 'right'

export type EditableImageValue = {
  image: MediaReference | null
  imageAlt: string
  caption: string
  ratio: ImageRatio
  fitMode: ImageFitMode
  zoom: number
  focalX: number
  focalY: number
  visualWidth?: number
  visualAlign?: ImageAlign
}

export type EditableImageSelection = {
  blockId: string
  variant: 'hero' | 'block'
  allowLayoutResize: boolean
}

export type { MediaReference }
