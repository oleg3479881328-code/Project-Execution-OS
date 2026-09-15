'use client'

import { useEffect, useState } from 'react'
import Cropper from 'react-easy-crop'
import type { CropAreaPercentages, ImageRatio } from './types'

type Point = { x: number; y: number }

type Props = {
  imageUrl: string
  imageAlt: string
  ratio: Exclude<ImageRatio, 'natural'>
  variant: 'hero' | 'block'
  initialArea?: CropAreaPercentages | null
  onCancel: () => void
  onApply: (area: CropAreaPercentages) => void
}

function roundArea(area: CropAreaPercentages): CropAreaPercentages {
  return {
    x: Math.round(area.x * 1000) / 1000,
    y: Math.round(area.y * 1000) / 1000,
    width: Math.round(area.width * 1000) / 1000,
    height: Math.round(area.height * 1000) / 1000,
  }
}

function aspectFor(ratio: Exclude<ImageRatio, 'natural'>, variant: 'hero' | 'block') {
  if (ratio === 'square') return 1
  if (ratio === 'portrait') return variant === 'hero' ? 0.9 : 0.82
  return 1.55
}

function clampZoom(value: number) {
  return Math.min(3, Math.max(1, value))
}

export default function CropMoveDialog({ imageUrl, imageAlt, ratio, variant, initialArea, onCancel, onApply }: Props) {
  const [crop, setCrop] = useState<Point>({ x: 0, y: 0 })
  const [zoom, setZoom] = useState(1)
  const [completedArea, setCompletedArea] = useState<CropAreaPercentages | null>(initialArea ?? null)

  useEffect(() => {
    const onKeyDown = (event: KeyboardEvent) => {
      if (event.key !== 'Escape') return
      event.preventDefault()
      onCancel()
    }
    window.addEventListener('keydown', onKeyDown)
    return () => window.removeEventListener('keydown', onKeyDown)
  }, [onCancel])

  const reset = () => {
    setCrop({ x: 0, y: 0 })
    setZoom(1)
    setCompletedArea(null)
  }

  const nudgeZoom = (delta: number) => {
    setZoom((current) => Math.round(clampZoom(current + delta) * 100) / 100)
  }

  return (
    <div
      className="wc-crop-dialog"
      role="dialog"
      aria-modal="true"
      aria-label="Crop and move photograph"
      data-wc-crop-dialog
      data-initial-crop-x={initialArea?.x}
      data-initial-crop-y={initialArea?.y}
      data-initial-crop-width={initialArea?.width}
      data-initial-crop-height={initialArea?.height}
      onPointerDown={(event) => {
        event.stopPropagation()
        if (event.target === event.currentTarget) onCancel()
      }}
      onClick={(event) => event.stopPropagation()}
    >
      <div className="wc-crop-dialog__panel">
        <div className="wc-crop-dialog__header">
          <div>
            <strong>Crop / move photograph</strong>
            <span>{initialArea ? 'Saved crop restored. Drag the photograph or adjust zoom.' : 'Drag the photograph. Use zoom for a tighter crop.'}</span>
          </div>
          <button type="button" aria-label="Cancel crop" onClick={onCancel}>×</button>
        </div>

        <div
          className="wc-crop-dialog__stage"
          data-testid="wc-crop-stage"
          style={{ position: 'relative', height: 'min(56vh, 560px)', minHeight: 320, overflow: 'hidden', isolation: 'isolate' }}
        >
          <Cropper
            image={imageUrl}
            crop={crop}
            zoom={zoom}
            minZoom={1}
            maxZoom={3}
            zoomSpeed={0.1}
            aspect={aspectFor(ratio, variant)}
            showGrid
            initialCroppedAreaPercentages={initialArea ?? undefined}
            onCropChange={setCrop}
            onZoomChange={setZoom}
            onCropComplete={(area) => setCompletedArea(roundArea(area))}
            mediaProps={{ alt: imageAlt || 'Photograph being cropped' }}
          />
        </div>

        <div className="wc-crop-dialog__controls" style={{ position: 'relative', zIndex: 2 }}>
          <label>
            <span>Zoom · {zoom.toFixed(2)}×</span>
            <div style={{ display: 'grid', gridTemplateColumns: 'auto 1fr auto', alignItems: 'center', gap: 10 }}>
              <button type="button" aria-label="Zoom out crop" disabled={zoom <= 1} onClick={() => nudgeZoom(-0.1)}>−</button>
              <input
                aria-label="Crop zoom"
                type="range"
                min="1"
                max="3"
                step="0.01"
                value={zoom}
                onChange={(event) => setZoom(Number(event.currentTarget.value))}
              />
              <button type="button" aria-label="Zoom in crop" disabled={zoom >= 3} onClick={() => nudgeZoom(0.1)}>+</button>
            </div>
          </label>
          <div className="wc-crop-dialog__actions">
            <button type="button" onClick={reset}>Reset</button>
            <button type="button" onClick={onCancel}>Cancel</button>
            <button
              type="button"
              className="is-primary"
              disabled={!completedArea}
              onClick={() => completedArea && onApply(completedArea)}
            >
              Apply crop
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
