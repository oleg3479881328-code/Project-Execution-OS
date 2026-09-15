'use client'

import { useEffect, useState } from 'react'
import { MediaField } from '@delmaredigital/payload-puck/fields'
import type { EditableImageSelection, EditableImageValue, ImageAlign } from './types'

type Props = {
  selection: EditableImageSelection
  value: EditableImageValue
  onPatch: (patch: Record<string, unknown>) => void
  onClose: () => void
}

function emitAdjustMode(blockId: string, adjusting: boolean) {
  window.dispatchEvent(new CustomEvent('wc-image-adjust-mode', { detail: { blockId, adjusting } }))
}

const sectionStyle: React.CSSProperties = {
  padding: '16px 14px',
  borderTop: '1px solid var(--puck-color-border, #dedede)',
}

const labelStyle: React.CSSProperties = {
  display: 'block',
  marginBottom: 7,
  color: 'var(--puck-color-text-secondary, #5a5a5a)',
  fontSize: 11,
  fontWeight: 650,
  letterSpacing: '.04em',
  textTransform: 'uppercase',
}

const controlStyle: React.CSSProperties = {
  width: '100%',
  minHeight: 36,
  border: '1px solid var(--puck-color-border, #dcdcdc)',
  borderRadius: 5,
  background: 'var(--puck-color-surface, #fff)',
  color: 'var(--puck-color-text, #111)',
  padding: '7px 9px',
}

const buttonStyle: React.CSSProperties = {
  minHeight: 34,
  border: '1px solid var(--puck-color-border, #dcdcdc)',
  borderRadius: 5,
  background: 'var(--puck-color-surface, #fff)',
  color: 'var(--puck-color-text, #111)',
  padding: '0 10px',
  cursor: 'pointer',
  fontSize: 12,
  fontWeight: 600,
}

export default function ImageInspectorPanel({ selection, value, onPatch, onClose }: Props) {
  const [adjusting, setAdjusting] = useState(false)

  useEffect(() => {
    setAdjusting(false)
    emitAdjustMode(selection.blockId, false)
    return () => emitAdjustMode(selection.blockId, false)
  }, [selection.blockId])

  useEffect(() => {
    const onAdjustMode = (event: Event) => {
      const detail = (event as CustomEvent<{ blockId?: string; adjusting?: boolean }>).detail
      if (detail?.blockId === selection.blockId) setAdjusting(Boolean(detail.adjusting))
    }
    window.addEventListener('wc-image-adjust-mode', onAdjustMode)
    return () => window.removeEventListener('wc-image-adjust-mode', onAdjustMode)
  }, [selection.blockId])

  const toggleAdjusting = () => {
    const next = !adjusting
    setAdjusting(next)
    emitAdjustMode(selection.blockId, next)
  }

  const close = () => {
    emitAdjustMode(selection.blockId, false)
    setAdjusting(false)
    onClose()
  }

  return (
    <div
      data-wc-image-inspector={selection.blockId}
      style={{ minHeight: '100%', background: 'var(--puck-color-surface, #fff)', color: 'var(--puck-color-text, #111)' }}
    >
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', gap: 12, padding: 14 }}>
        <div>
          <div style={{ fontSize: 11, fontWeight: 750, letterSpacing: '.08em' }}>IMAGE</div>
          <div style={{ marginTop: 3, color: 'var(--puck-color-text-secondary, #666)', fontSize: 11 }}>
            {selection.variant === 'hero' ? 'Hero photograph' : 'Page photograph'}
          </div>
        </div>
        <button type="button" style={buttonStyle} onClick={close}>Back to block</button>
      </div>

      <div style={sectionStyle}>
        <MediaField value={value.image} onChange={(image) => onPatch({ image })} label="Image" />
      </div>

      <div style={sectionStyle}>
        <span style={labelStyle}>Frame</span>
        <div style={{ display: 'grid', gap: 10 }}>
          <label>
            <span style={labelStyle}>Shape</span>
            <select style={controlStyle} value={value.ratio} onChange={(event) => onPatch({ ratio: event.currentTarget.value })}>
              <option value="natural">Natural</option>
              <option value="landscape">Landscape</option>
              <option value="portrait">Portrait</option>
              <option value="square">Square</option>
            </select>
          </label>

          <div>
            <span style={labelStyle}>Fit</span>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 7 }}>
              <button type="button" style={{ ...buttonStyle, background: value.fitMode === 'fill' ? 'var(--puck-color-interactive-soft, #eef4fb)' : buttonStyle.background }} onClick={() => onPatch({ fitMode: 'fill' })}>Fill / crop</button>
              <button type="button" style={{ ...buttonStyle, background: value.fitMode === 'fit' ? 'var(--puck-color-interactive-soft, #eef4fb)' : buttonStyle.background }} onClick={() => onPatch({ fitMode: 'fit', zoom: 1 })}>Fit full photo</button>
            </div>
          </div>

          <label>
            <span style={labelStyle}>Zoom · {value.zoom.toFixed(2)}×</span>
            <input
              style={{ width: '100%' }}
              type="range"
              min="1"
              max="3"
              step="0.05"
              value={value.zoom}
              disabled={value.ratio === 'natural' || value.fitMode === 'fit'}
              onChange={(event) => onPatch({ zoom: Number(event.currentTarget.value), fitMode: 'fill' })}
            />
          </label>

          <button
            type="button"
            style={{ ...buttonStyle, width: '100%', background: adjusting ? 'var(--puck-color-interactive, #0158ad)' : buttonStyle.background, color: adjusting ? '#fff' : buttonStyle.color }}
            disabled={value.ratio === 'natural' || value.fitMode === 'fit'}
            onClick={toggleAdjusting}
          >
            {adjusting ? 'Done moving crop' : 'Crop / move photograph'}
          </button>
          <div style={{ color: 'var(--puck-color-text-secondary, #666)', fontSize: 11, lineHeight: 1.45 }}>
            {value.ratio === 'natural'
              ? 'Choose Landscape, Portrait or Square to crop.'
              : value.fitMode === 'fit'
                ? 'Fit shows the full photograph. Switch to Fill to reposition it inside the frame.'
                : adjusting
                  ? 'Drag the photograph directly on the canvas. Use the Zoom slider for scale.'
                  : 'Use Crop / move photograph, then drag the photograph inside its frame.'}
          </div>
        </div>
      </div>

      <div style={sectionStyle}>
        <span style={labelStyle}>Crop position</span>
        <div style={{ display: 'grid', gap: 10 }}>
          <label>
            <span style={labelStyle}>Horizontal · {Math.round(value.focalX)}%</span>
            <input style={{ width: '100%' }} type="range" min="0" max="100" step="1" value={value.focalX} onChange={(event) => onPatch({ focalX: Number(event.currentTarget.value) })} />
          </label>
          <label>
            <span style={labelStyle}>Vertical · {Math.round(value.focalY)}%</span>
            <input style={{ width: '100%' }} type="range" min="0" max="100" step="1" value={value.focalY} onChange={(event) => onPatch({ focalY: Number(event.currentTarget.value) })} />
          </label>
          <button type="button" style={{ ...buttonStyle, width: '100%' }} onClick={() => onPatch({ focalX: 50, focalY: 50, zoom: 1, fitMode: 'fill' })}>Reset crop</button>
        </div>
      </div>

      {selection.allowLayoutResize ? (
        <div style={sectionStyle}>
          <span style={labelStyle}>Size & position</span>
          <label>
            <span style={labelStyle}>Width · {Math.round(value.visualWidth ?? 100)}%</span>
            <input style={{ width: '100%' }} type="range" min="28" max="100" step="1" value={value.visualWidth ?? 100} onChange={(event) => onPatch({ visualWidth: Number(event.currentTarget.value) })} />
          </label>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 7, marginTop: 10 }}>
            {(['left', 'center', 'right'] as ImageAlign[]).map((align) => (
              <button
                key={align}
                type="button"
                style={{ ...buttonStyle, background: value.visualAlign === align ? 'var(--puck-color-interactive-soft, #eef4fb)' : buttonStyle.background }}
                onClick={() => onPatch({ visualAlign: align })}
              >
                {align[0].toUpperCase() + align.slice(1)}
              </button>
            ))}
          </div>
        </div>
      ) : null}

      <div style={sectionStyle}>
        <label>
          <span style={labelStyle}>Alt text</span>
          <input style={controlStyle} type="text" value={value.imageAlt} onChange={(event) => onPatch({ imageAlt: event.currentTarget.value })} />
        </label>
        <label style={{ display: 'block', marginTop: 12 }}>
          <span style={labelStyle}>Caption / credit</span>
          <input style={controlStyle} type="text" value={value.caption} onChange={(event) => onPatch({ caption: event.currentTarget.value })} />
        </label>
      </div>
    </div>
  )
}
