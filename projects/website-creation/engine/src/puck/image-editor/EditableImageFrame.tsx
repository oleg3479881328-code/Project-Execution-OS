'use client'

import { useEffect, useLayoutEffect, useRef, useState } from 'react'
import type { CSSProperties, PointerEvent as ReactPointerEvent } from 'react'
import { createPortal } from 'react-dom'
import { registerOverlayPortal } from '@puckeditor/core'
import Moveable from 'react-moveable'
import ImageInspectorPanel from './ImageInspectorPanel'
import type { ImageAlign, ImageFitMode, ImageRatio, MediaReference } from './types'

type DragState = {
  pointerId: number
  x: number
  y: number
  focalX: number
  focalY: number
  width: number
  height: number
  zoom: number
}

type CropPoint = { x: number; y: number }

type Props = {
  blockId: string
  image: MediaReference | null
  imageAlt: string
  caption?: string
  ratio?: ImageRatio
  fitMode?: ImageFitMode
  zoom?: number
  focalX?: number
  focalY?: number
  variant?: 'hero' | 'block'
  visualWidth?: number
  visualAlign?: ImageAlign
  allowLayoutResize?: boolean
}

function clamp(value: number, min: number, max: number) {
  return Math.min(max, Math.max(min, value))
}

function dispatchEditorEvent(name: string, detail: Record<string, unknown>) {
  window.dispatchEvent(new CustomEvent(name, { detail }))
  if (window.parent && window.parent !== window) {
    window.parent.dispatchEvent(new CustomEvent(name, { detail }))
  }
}

function dispatchPatch(blockId: string, patch: Record<string, unknown>) {
  dispatchEditorEvent('wc-image-layout-change', { blockId, patch })
}

function heroCropPatch(patch: Record<string, unknown>) {
  const mapped: Record<string, unknown> = {}
  for (const [key, value] of Object.entries(patch)) {
    if (key === 'ratio') mapped.imageRatio = value
    else if (key === 'fitMode') mapped.imageFitMode = value
    else if (key === 'zoom') mapped.imageZoom = value
    else if (key === 'focalX') mapped.imageFocalX = value
    else if (key === 'focalY') mapped.imageFocalY = value
    else if (key === 'caption') mapped.imageCredit = value
    else mapped[key] = value
  }
  return mapped
}

function ToolbarIcon({ kind }: { kind: 'replace' | 'crop' | 'fit' | 'fill' | 'reset' | 'remove' }) {
  if (kind === 'replace') return <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3.5" y="5" width="12.5" height="11" rx="1.5"/><path d="m5.5 14 3.2-3.4 2.4 2.3 2-2 2.9 3.1"/><path d="M18 8h3m-1.5-1.5V9.5"/></svg>
  if (kind === 'crop') return <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 3v13a1 1 0 0 0 1 1h13"/><path d="M3 7h13a1 1 0 0 1 1 1v13"/></svg>
  if (kind === 'fit') return <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="6" width="16" height="12" rx="1.5"/><path d="M8 10h8v4H8z"/></svg>
  if (kind === 'fill') return <svg viewBox="0 0 24 24" aria-hidden="true"><rect x="4" y="6" width="16" height="12" rx="1.5"/><path d="M6 8h12v8H6z"/></svg>
  if (kind === 'reset') return <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8V4m0 0h4M5 4l3 3a7 7 0 1 1-1.2 8"/></svg>
  return <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 7h14M9 7V4h6v3m-8 0 1 13h8l1-13M10 10v7m4-7v7"/></svg>
}

export default function EditableImageFrame({
  blockId,
  image,
  imageAlt,
  caption = '',
  ratio = 'natural',
  fitMode = 'fill',
  zoom = 1,
  focalX = 50,
  focalY = 50,
  variant = 'block',
  visualWidth,
  visualAlign = 'center',
  allowLayoutResize = variant === 'block',
}: Props) {
  const [target, setTarget] = useState<HTMLElement | null>(null)
  const [active, setActive] = useState(false)
  const [adjusting, setAdjusting] = useState(false)
  const [draftFocalX, setDraftFocalX] = useState(clamp(focalX, 0, 100))
  const [draftFocalY, setDraftFocalY] = useState(clamp(focalY, 0, 100))
  const [draftZoom, setDraftZoom] = useState(clamp(zoom, 1, 3))
  const [draftFitMode, setDraftFitMode] = useState<ImageFitMode>(fitMode)
  const [reviewScale, setReviewScale] = useState(1)
  const [fitCollapse, setFitCollapse] = useState(0)
  const [inspectorHost, setInspectorHost] = useState<HTMLElement | null>(null)
  const dragRef = useRef<DragState | null>(null)
  const lastPanPointRef = useRef<CropPoint | null>(null)
  const panReleaseCleanupRef = useRef<(() => void) | null>(null)
  const portalRef = useRef<HTMLElement | null>(null)
  const cropFrameRef = useRef<HTMLDivElement | null>(null)

  const width = typeof visualWidth === 'number' ? clamp(visualWidth, 28, 100) : undefined
  const align: ImageAlign = visualAlign ?? 'center'
  const imageUrl = image?.url || ''
  const canCrop = Boolean(imageUrl) && ratio !== 'natural' && draftFitMode === 'fill'
  const canZoom = Boolean(imageUrl) && ratio !== 'natural' && draftFitMode === 'fill'

  useEffect(() => {
    if (portalRef.current) registerOverlayPortal(portalRef.current)
    try {
      setInspectorHost(window.parent && window.parent !== window ? window.parent.document.body : document.body)
    } catch {
      setInspectorHost(document.body)
    }
  }, [])

  useEffect(() => () => {
    panReleaseCleanupRef.current?.()
    panReleaseCleanupRef.current = null
    dragRef.current = null
    lastPanPointRef.current = null
  }, [])

  useEffect(() => {
    if (dragRef.current) return
    setDraftFocalX(clamp(focalX, 0, 100))
    setDraftFocalY(clamp(focalY, 0, 100))
    setDraftZoom(clamp(zoom, 1, 3))
    setDraftFitMode(fitMode)
  }, [focalX, focalY, zoom, fitMode])

  useEffect(() => {
    const onActivate = (event: Event) => {
      const id = (event as CustomEvent<{ blockId?: string }>).detail?.blockId
      if (id !== blockId) {
        setActive(false)
        setAdjusting(false)
      }
    }
    const onAdjustMode = (event: Event) => {
      const detail = (event as CustomEvent<{ blockId?: string; adjusting?: boolean }>).detail
      if (detail?.blockId === blockId) setAdjusting(Boolean(detail.adjusting))
    }
    window.addEventListener('wc-image-layout-activate', onActivate)
    window.addEventListener('wc-image-adjust-mode', onAdjustMode)
    return () => {
      window.removeEventListener('wc-image-layout-activate', onActivate)
      window.removeEventListener('wc-image-adjust-mode', onAdjustMode)
    }
  }, [blockId])

  useLayoutEffect(() => {
    if (!allowLayoutResize || !active || !target) {
      setReviewScale(1)
      setFitCollapse(0)
      return
    }
    const fitSelectedFrame = () => {
      const sourceHeight = target.offsetHeight
      if (!sourceHeight) return
      const availableHeight = Math.max(360, window.innerHeight - 96)
      const nextScale = Math.min(1, availableHeight / sourceHeight)
      setReviewScale(nextScale)
      setFitCollapse(Math.max(0, sourceHeight * (1 - nextScale)))
    }
    fitSelectedFrame()
    const resizeObserver = new ResizeObserver(fitSelectedFrame)
    resizeObserver.observe(target)
    window.addEventListener('resize', fitSelectedFrame)
    return () => {
      resizeObserver.disconnect()
      window.removeEventListener('resize', fitSelectedFrame)
    }
  }, [active, allowLayoutResize, target])

  const figureStyle = width && allowLayoutResize
    ? {
        width: `${width}%`,
        maxWidth: '1200px',
        marginLeft: align === 'left' ? '0' : 'auto',
        marginRight: align === 'right' ? '0' : 'auto',
      }
    : undefined

  const frameStyle = {
    '--wc-image-focal-x': `${draftFocalX}%`,
    '--wc-image-focal-y': `${draftFocalY}%`,
    '--wc-image-zoom': String(draftZoom),
  } as CSSProperties

  const combinedFigureStyle = {
    ...figureStyle,
    position: 'relative',
    overflow: 'visible',
    '--wc-review-scale': String(active && allowLayoutResize ? reviewScale : 1),
    '--wc-fit-collapse': `${active && allowLayoutResize ? fitCollapse : 0}px`,
    '--wc-fit-origin': align === 'left' ? 'top left' : align === 'right' ? 'top right' : 'top center',
  } as CSSProperties

  function activate() {
    setActive(true)
    dispatchEditorEvent('wc-image-layout-activate', { blockId })
  }

  function commit(patch: Record<string, unknown>) {
    dispatchPatch(blockId, variant === 'hero' ? heroCropPatch(patch) : patch)
  }

  function commitInspector(patch: Record<string, unknown>) {
    if (typeof patch.focalX === 'number') setDraftFocalX(clamp(patch.focalX, 0, 100))
    if (typeof patch.focalY === 'number') setDraftFocalY(clamp(patch.focalY, 0, 100))
    if (typeof patch.zoom === 'number') setDraftZoom(clamp(patch.zoom, 1, 3))
    if (patch.fitMode === 'fill' || patch.fitMode === 'fit') setDraftFitMode(patch.fitMode)
    commit(patch)
  }

  function emitAdjusting(next: boolean) {
    setAdjusting(next)
    dispatchEditorEvent('wc-image-adjust-mode', { blockId, adjusting: next })
  }

  function setShape(next: ImageRatio) {
    if (next === 'natural') emitAdjusting(false)
    commitInspector({ ratio: next })
  }

  function setFit(next: ImageFitMode) {
    if (next === 'fit') {
      emitAdjusting(false)
      commitInspector({ fitMode: 'fit', zoom: 1 })
    } else {
      commitInspector({ fitMode: 'fill' })
    }
  }

  function resetCrop() {
    emitAdjusting(false)
    commitInspector({ focalX: 50, focalY: 50, zoom: 1, fitMode: 'fill' })
  }

  function inspectorRoot() {
    try {
      const doc = window.parent && window.parent !== window ? window.parent.document : document
      return Array.from(doc.querySelectorAll<HTMLElement>('[data-wc-image-inspector]')).find(
        (element) => element.dataset.wcImageInspector === blockId
      ) ?? null
    } catch {
      return null
    }
  }

  function requestReplace() {
    const root = inspectorRoot()
    const button = root
      ? Array.from(root.querySelectorAll<HTMLButtonElement>('button')).find((candidate) => {
          const text = candidate.textContent?.trim()
          return text === 'Change Image' || text === 'Select Image'
        })
      : null
    button?.click()
  }

  function requestRemove() {
    if (!imageUrl) return
    if (!window.confirm('Remove this photograph from the page?')) return
    const root = inspectorRoot()
    const removeButton = root
      ? Array.from(root.querySelectorAll<HTMLButtonElement>('button')).find((button) => button.textContent?.trim() === 'Remove')
      : null
    if (removeButton) removeButton.click()
    else commitInspector({ image: null })
  }

  function cropPoint(drag: DragState, clientX: number, clientY: number) {
    const sensitivity = Math.max(1, drag.zoom)
    return {
      x: clamp(drag.focalX - ((clientX - drag.x) / drag.width) * 100 / sensitivity, 0, 100),
      y: clamp(drag.focalY - ((clientY - drag.y) / drag.height) * 100 / sensitivity, 0, 100),
    }
  }

  function clearPanReleaseListeners() {
    panReleaseCleanupRef.current?.()
    panReleaseCleanupRef.current = null
  }

  function finishPan(pointerId: number, clientX?: number, clientY?: number) {
    const drag = dragRef.current
    if (!drag || drag.pointerId !== pointerId) return
    const point = typeof clientX === 'number' && typeof clientY === 'number'
      ? cropPoint(drag, clientX, clientY)
      : lastPanPointRef.current ?? { x: drag.focalX, y: drag.focalY }
    dragRef.current = null
    lastPanPointRef.current = null
    clearPanReleaseListeners()
    const frame = cropFrameRef.current
    if (frame?.hasPointerCapture(pointerId)) {
      try { frame.releasePointerCapture(pointerId) } catch { /* capture can already be gone */ }
    }
    setDraftFocalX(point.x)
    setDraftFocalY(point.y)
    commit({ focalX: Math.round(point.x * 10) / 10, focalY: Math.round(point.y * 10) / 10 })
  }

  function armPanReleaseListeners(pointerId: number, ownerWindow: Window) {
    clearPanReleaseListeners()
    const handlePointerUp = (event: PointerEvent) => {
      if (event.pointerId === pointerId) finishPan(pointerId, event.clientX, event.clientY)
    }
    const handlePointerCancel = (event: PointerEvent) => {
      if (event.pointerId === pointerId) finishPan(pointerId)
    }
    const handleMouseUp = (event: MouseEvent) => {
      if (dragRef.current?.pointerId === pointerId) finishPan(pointerId, event.clientX, event.clientY)
    }
    const handleBlur = () => finishPan(pointerId)
    ownerWindow.addEventListener('pointerup', handlePointerUp)
    ownerWindow.addEventListener('pointercancel', handlePointerCancel)
    ownerWindow.addEventListener('mouseup', handleMouseUp)
    ownerWindow.addEventListener('blur', handleBlur)

    let parentWindow: Window | null = null
    let handleParentPointerUp: ((event: PointerEvent) => void) | null = null
    let handleParentMouseUp: (() => void) | null = null
    try {
      if (ownerWindow.parent && ownerWindow.parent !== ownerWindow) {
        parentWindow = ownerWindow.parent
        handleParentPointerUp = (event: PointerEvent) => {
          if (event.pointerId === pointerId) finishPan(pointerId)
        }
        handleParentMouseUp = () => finishPan(pointerId)
        parentWindow.addEventListener('pointerup', handleParentPointerUp)
        parentWindow.addEventListener('mouseup', handleParentMouseUp)
      }
    } catch {
      parentWindow = null
    }

    panReleaseCleanupRef.current = () => {
      ownerWindow.removeEventListener('pointerup', handlePointerUp)
      ownerWindow.removeEventListener('pointercancel', handlePointerCancel)
      ownerWindow.removeEventListener('mouseup', handleMouseUp)
      ownerWindow.removeEventListener('blur', handleBlur)
      if (parentWindow && handleParentPointerUp) parentWindow.removeEventListener('pointerup', handleParentPointerUp)
      if (parentWindow && handleParentMouseUp) parentWindow.removeEventListener('mouseup', handleParentMouseUp)
    }
  }

  function startPan(event: ReactPointerEvent<HTMLDivElement>) {
    activate()
    if (event.button !== 0 || !adjusting || !imageUrl || ratio === 'natural' || draftFitMode !== 'fill') return
    event.preventDefault()
    event.stopPropagation()
    const rect = event.currentTarget.getBoundingClientRect()
    event.currentTarget.setPointerCapture(event.pointerId)
    dragRef.current = {
      pointerId: event.pointerId,
      x: event.clientX,
      y: event.clientY,
      focalX: draftFocalX,
      focalY: draftFocalY,
      width: Math.max(1, rect.width),
      height: Math.max(1, rect.height),
      zoom: draftZoom,
    }
    lastPanPointRef.current = { x: draftFocalX, y: draftFocalY }
    armPanReleaseListeners(event.pointerId, event.currentTarget.ownerDocument.defaultView ?? window)
  }

  function movePan(event: ReactPointerEvent<HTMLDivElement>) {
    const drag = dragRef.current
    if (!drag || drag.pointerId !== event.pointerId) return
    event.preventDefault()
    event.stopPropagation()
    const point = cropPoint(drag, event.clientX, event.clientY)
    lastPanPointRef.current = point
    setDraftFocalX(point.x)
    setDraftFocalY(point.y)
  }

  function endPan(event: ReactPointerEvent<HTMLDivElement>) {
    const drag = dragRef.current
    if (!drag || drag.pointerId !== event.pointerId) return
    event.preventDefault()
    event.stopPropagation()
    finishPan(event.pointerId, event.clientX, event.clientY)
  }

  function setZoom(next: number) {
    const normalized = clamp(next, 1, 3)
    setDraftZoom(normalized)
    if (normalized > 1 && draftFitMode === 'fit') {
      setDraftFitMode('fill')
      commit({ zoom: normalized, fitMode: 'fill' })
    } else {
      commit({ zoom: normalized })
    }
  }

  const inspector = active && inspectorHost
    ? createPortal(
        <div style={{ position: 'fixed', top: 56, right: 0, bottom: 0, zIndex: 100000, width: 'clamp(330px, 28vw, 450px)', overflowY: 'auto', borderLeft: '1px solid var(--puck-color-border, #dcdcdc)', background: 'var(--puck-color-surface, #fff)', boxShadow: '-12px 0 28px rgba(0,0,0,.08)' }}>
          <ImageInspectorPanel
            selection={{ blockId, variant, allowLayoutResize }}
            value={{ image, imageAlt, caption, ratio, fitMode: draftFitMode, zoom: draftZoom, focalX: draftFocalX, focalY: draftFocalY, visualWidth: width, visualAlign: align }}
            onPatch={commitInspector}
            onClose={() => {
              emitAdjusting(false)
              setActive(false)
            }}
          />
        </div>,
        inspectorHost
      )
    : null

  return (
    <>
      <figure
        ref={(node) => {
          setTarget(node)
          portalRef.current = node
        }}
        className={`wc-editable-image ${variant === 'hero' ? 'wc-editable-image--hero' : 'wc-editable-image--block'}`}
        data-ratio={ratio}
        data-visual-align={align}
        style={combinedFigureStyle}
      >
        {active ? (
          <div className="wc-image-toolbar" role="toolbar" aria-label="Image controls" onPointerDown={(event) => event.stopPropagation()} onClick={(event) => event.stopPropagation()}>
            <button type="button" className="wc-image-toolbar__button" title="Replace photograph" aria-label="Replace photograph" onClick={requestReplace}><ToolbarIcon kind="replace" /></button>
            <button type="button" className={`wc-image-toolbar__button ${adjusting ? 'is-active' : ''}`} title={adjusting ? 'Finish moving crop' : 'Crop / move photograph'} aria-label={adjusting ? 'Finish moving crop' : 'Crop / move photograph'} disabled={!canCrop} onClick={() => emitAdjusting(!adjusting)}><ToolbarIcon kind="crop" /></button>
            <select className="wc-image-toolbar__select" aria-label="Frame shape" title="Frame shape" value={ratio} onChange={(event) => setShape(event.currentTarget.value as ImageRatio)}>
              <option value="natural">Natural</option><option value="landscape">Landscape</option><option value="portrait">Portrait</option><option value="square">Square</option>
            </select>
            <button type="button" className="wc-image-toolbar__button" title={draftFitMode === 'fill' ? 'Fit full photograph' : 'Fill frame / crop'} aria-label={draftFitMode === 'fill' ? 'Fit full photograph' : 'Fill frame / crop'} disabled={!imageUrl || ratio === 'natural'} onClick={() => setFit(draftFitMode === 'fill' ? 'fit' : 'fill')}><ToolbarIcon kind={draftFitMode === 'fill' ? 'fit' : 'fill'} /></button>
            <span className="wc-image-toolbar__divider" aria-hidden="true" />
            <button type="button" className="wc-image-toolbar__button" title="Zoom out" aria-label="Zoom out" disabled={!canZoom || draftZoom <= 1} onClick={() => setZoom(draftZoom - 0.1)}>−</button>
            <span className="wc-image-toolbar__zoom">{draftZoom.toFixed(2)}×</span>
            <button type="button" className="wc-image-toolbar__button" title="Zoom in" aria-label="Zoom in" disabled={!canZoom || draftZoom >= 3} onClick={() => setZoom(draftZoom + 0.1)}>+</button>
            <button type="button" className="wc-image-toolbar__button" title="Reset crop" aria-label="Reset crop" disabled={!imageUrl} onClick={resetCrop}><ToolbarIcon kind="reset" /></button>
            <button type="button" className="wc-image-toolbar__button wc-image-toolbar__danger" title="Remove photograph" aria-label="Remove photograph" disabled={!imageUrl} onClick={requestRemove}><ToolbarIcon kind="remove" /></button>
          </div>
        ) : null}

        <div
          ref={cropFrameRef}
          className={`wc-image-frame ${active ? 'is-selected' : ''} ${adjusting ? 'is-adjusting' : ''}`}
          data-ratio={ratio}
          data-fit={draftFitMode}
          data-variant={variant}
          style={frameStyle}
          onPointerDown={startPan}
          onPointerMove={movePan}
          onPointerUp={endPan}
          onPointerCancel={(event) => finishPan(event.pointerId)}
          onLostPointerCapture={(event) => {
            if (dragRef.current?.pointerId === event.pointerId) finishPan(event.pointerId)
          }}
          onWheel={(event) => {
            activate()
            if (!adjusting || ratio === 'natural') return
            event.preventDefault()
            event.stopPropagation()
            setZoom(draftZoom + (event.deltaY < 0 ? 0.08 : -0.08))
          }}
          onClick={activate}
        >
          {imageUrl ? <img src={imageUrl} alt={imageAlt || image?.alt || ''} /> : <div className="wc-image-missing">Select an image in the right panel</div>}
          {active && adjusting ? <div className="wc-image-edit-hint">{ratio === 'natural' ? 'Choose Landscape, Portrait or Square' : draftFitMode === 'fit' ? 'Fit shows the full photograph' : 'Hold the left mouse button to move · release to stop · wheel or + / − to zoom'}</div> : null}
        </div>
        {caption ? <figcaption>{caption}</figcaption> : null}
        {active && allowLayoutResize && !adjusting ? <div className="wc-image-edit-badge">Image selected · drag side handles to resize</div> : null}
      </figure>

      {active && target && allowLayoutResize && !adjusting ? (
        <Moveable
          target={target}
          resizable
          draggable
          keepRatio
          origin={false}
          edge={false}
          renderDirections={['w', 'e']}
          throttleResize={1}
          throttleDrag={1}
          onResize={({ target: el, width: nextWidth }) => {
            el.style.width = `${Math.max(220, nextWidth)}px`
          }}
          onResizeEnd={({ target: el }) => {
            const parentWidth = el.parentElement?.getBoundingClientRect().width || el.getBoundingClientRect().width
            const scaledWidth = el.getBoundingClientRect().width
            const unscaledWidth = reviewScale > 0 ? scaledWidth / reviewScale : scaledWidth
            const next = Math.round(clamp((unscaledWidth / parentWidth) * 100, 28, 100))
            el.style.width = `${next}%`
            commit({ visualWidth: next })
          }}
          onDrag={({ target: el, beforeTranslate }) => {
            el.style.transform = `translateX(${beforeTranslate[0]}px)`
          }}
          onDragEnd={({ target: el }) => {
            const parent = el.parentElement
            if (!parent) return
            const parentRect = parent.getBoundingClientRect()
            const rect = el.getBoundingClientRect()
            const center = rect.left + rect.width / 2
            const rel = (center - parentRect.left) / Math.max(1, parentRect.width)
            const nextAlign: ImageAlign = rel < 0.4 ? 'left' : rel > 0.6 ? 'right' : 'center'
            el.style.transform = ''
            commit({ visualAlign: nextAlign })
          }}
        />
      ) : null}
      {inspector}
    </>
  )
}
