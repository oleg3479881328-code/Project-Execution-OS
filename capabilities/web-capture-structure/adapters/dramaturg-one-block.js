// GENERATED FILE — do not hand-edit.
// Build: node scripts/build-dramaturg-adapter.mjs
// Dramaturg / playwright-repl JS mode. Uses the currently attached page only.

const BLOCK_ID = 'web.capture_structure';
const BLOCK_VERSION = '0.1.0';
const SCHEMA = 'peos.web_structure.v1';

const STANDARD_STYLE_PROPERTIES = [
  'display','position','box-sizing','overflow-x','overflow-y',
  'width','height','min-width','max-width','min-height','max-height',
  'margin-top','margin-right','margin-bottom','margin-left',
  'padding-top','padding-right','padding-bottom','padding-left',
  'gap','row-gap','column-gap',
  'flex-direction','flex-wrap','justify-content','align-items','align-content',
  'flex-grow','flex-shrink','flex-basis','order',
  'grid-template-columns','grid-template-rows','grid-column-start','grid-column-end','grid-row-start','grid-row-end',
  'font-family','font-size','font-weight','font-style','line-height','letter-spacing',
  'text-align','text-transform','text-decoration-line','white-space',
  'color','background-color','background-image','background-size','background-position','background-repeat',
  'border-top-width','border-right-width','border-bottom-width','border-left-width',
  'border-top-style','border-right-style','border-bottom-style','border-left-style',
  'border-top-color','border-right-color','border-bottom-color','border-left-color',
  'border-top-left-radius','border-top-right-radius','border-bottom-right-radius','border-bottom-left-radius',
  'opacity','visibility','transform','transform-origin','z-index',
  'object-fit','object-position','aspect-ratio'
];

const DEFAULT_ATTRS = new Set([
  'id','class','role','href','target','rel','src','srcset','sizes','alt','title','type','name','value','placeholder',
  'width','height','loading','decoding','fetchpriority','for','action','method','checked','selected','disabled','hidden',
  'aria-label','aria-labelledby','aria-describedby','aria-hidden','aria-expanded','aria-controls','aria-current','aria-selected',
  'aria-pressed','aria-live'
]);

const SKIP_TAGS = new Set(['script','style','noscript','meta','link','base','title']);

function round(n) {
  return Number.isFinite(n) ? Math.round(n * 100) / 100 : n;
}

function decodeRare(data, strings, kind = 'string') {
  const out = new Map();
  if (!data || !Array.isArray(data.index)) return out;
  if (kind === 'boolean') {
    for (const idx of data.index) out.set(idx, true);
    return out;
  }
  const values = Array.isArray(data.value) ? data.value : [];
  for (let i = 0; i < data.index.length; i += 1) {
    const raw = values[i];
    out.set(data.index[i], kind === 'string' ? (strings[raw] ?? '') : raw);
  }
  return out;
}

function decodeAttributes(raw, strings, includeDataAttributes = false, includeInlineStyle = false) {
  if (!Array.isArray(raw) || raw.length === 0) return undefined;
  const attrs = {};
  for (let i = 0; i < raw.length; i += 2) {
    const name = String(strings[raw[i]] ?? '').toLowerCase();
    const value = String(strings[raw[i + 1]] ?? '');
    if (!name) continue;
    if (name === 'style' && includeInlineStyle) attrs[name] = value;
    else if (DEFAULT_ATTRS.has(name) || name.startsWith('aria-') || (includeDataAttributes && name.startsWith('data-'))) attrs[name] = value;
  }
  return Object.keys(attrs).length ? attrs : undefined;
}

function nodeKind(type) {
  if (type === 9) return 'document';
  if (type === 1) return 'element';
  if (type === 3) return 'text';
  if (type === 8) return 'comment';
  return 'other';
}

function normalizeCdpSnapshot(raw, meta, options, styleProperties) {
  const strings = Array.isArray(raw?.strings) ? raw.strings : [];
  const styleTable = [];
  const styleKeyToRef = new Map();

  const internStyle = (values) => {
    if (!values || values.length === 0) return undefined;
    const normalized = values.map((v) => String(v ?? ''));
    const key = JSON.stringify(normalized);
    if (styleKeyToRef.has(key)) return styleKeyToRef.get(key);
    const ref = styleTable.length;
    styleTable.push(normalized);
    styleKeyToRef.set(key, ref);
    return ref;
  };

  const documents = (raw?.documents ?? []).map((doc, docIndex) => {
    const nodes = doc.nodes ?? {};
    const layout = doc.layout ?? {};
    const layoutByNode = new Map();
    for (let li = 0; li < (layout.nodeIndex ?? []).length; li += 1) layoutByNode.set(layout.nodeIndex[li], li);

    const shadowRootType = decodeRare(nodes.shadowRootType, strings, 'string');
    const pseudoType = decodeRare(nodes.pseudoType, strings, 'string');
    const pseudoIdentifier = decodeRare(nodes.pseudoIdentifier, strings, 'string');
    const isClickable = decodeRare(nodes.isClickable, strings, 'boolean');
    const currentSourceURL = decodeRare(nodes.currentSourceURL, strings, 'string');
    const contentDocumentIndex = decodeRare(nodes.contentDocumentIndex, strings, 'integer');
    const stackingContexts = decodeRare(layout.stackingContexts, strings, 'boolean');

    const rawNodes = [];
    const total = (nodes.nodeType ?? []).length;
    for (let i = 0; i < total; i += 1) {
      const type = nodes.nodeType[i];
      const kind = nodeKind(type);
      const rawName = strings[nodes.nodeName?.[i]] ?? '';
      const tag = kind === 'element' ? String(rawName).toLowerCase() : undefined;
      if (tag && SKIP_TAGS.has(tag)) {
        rawNodes.push(null);
        continue;
      }

      const li = layoutByNode.get(i);
      let bounds;
      let paintOrder;
      let styleRef;
      let visible;
      let stackingContext;
      if (li !== undefined) {
        const b = layout.bounds?.[li];
        if (Array.isArray(b) && b.length >= 4) bounds = b.slice(0, 4).map(round);
        paintOrder = layout.paintOrders?.[li];
        stackingContext = stackingContexts.get(li) || undefined;
        const styleIndexes = layout.styles?.[li];
        if (Array.isArray(styleIndexes)) {
          const styleValues = styleIndexes.map((idx) => strings[idx] ?? '');
          styleRef = internStyle(styleValues);
          const style = Object.fromEntries(styleProperties.map((p, idx) => [p, styleValues[idx] ?? '']));
          const opacity = Number.parseFloat(style.opacity || '1');
          visible = Boolean(bounds && bounds[2] > 0 && bounds[3] > 0 && style.display !== 'none' && style.visibility !== 'hidden' && opacity !== 0);
        } else {
          visible = Boolean(bounds && bounds[2] > 0 && bounds[3] > 0);
        }
      }

      const value = strings[nodes.nodeValue?.[i]] ?? '';
      const text = kind === 'text' ? String(value).replace(/\s+/g, ' ').trim().slice(0, options.maxTextLength) : undefined;
      const attrs = kind === 'element' ? decodeAttributes(nodes.attributes?.[i], strings, options.includeDataAttributes, options.includeInlineStyle) : undefined;

      rawNodes.push({
        id: `d${docIndex}:n${i}`,
        parent: Number.isInteger(nodes.parentIndex?.[i]) && nodes.parentIndex[i] >= 0 ? `d${docIndex}:n${nodes.parentIndex[i]}` : undefined,
        kind,
        tag,
        text: text || undefined,
        attrs,
        currentSrc: currentSourceURL.get(i) || undefined,
        clickable: isClickable.get(i) || undefined,
        pseudoType: pseudoType.get(i) || undefined,
        pseudoIdentifier: pseudoIdentifier.get(i) || undefined,
        shadowRootType: shadowRootType.get(i) || undefined,
        contentDocument: Number.isInteger(contentDocumentIndex.get(i)) ? contentDocumentIndex.get(i) : undefined,
        bounds,
        styleRef,
        paintOrder: Number.isInteger(paintOrder) ? paintOrder : undefined,
        stackingContext,
        visible
      });
    }

    const keep = new Set();
    for (let i = 0; i < rawNodes.length; i += 1) {
      const n = rawNodes[i];
      if (!n) continue;
      const meaningfulText = n.kind === 'text' && n.text;
      const meaningfulElement = n.kind === 'element' && (n.bounds || ['html','body','header','main','nav','section','article','aside','footer','form','a','button','input','textarea','select','img','picture','video','svg','iframe'].includes(n.tag));
      const meaningfulDocument = n.kind === 'document';
      const allowedVisibility = options.includeHidden || n.visible !== false || !n.bounds;
      if ((meaningfulDocument || meaningfulText || meaningfulElement) && allowedVisibility) {
        let cursor = i;
        while (cursor >= 0 && !keep.has(cursor)) {
          if (rawNodes[cursor]) keep.add(cursor);
          const parent = nodes.parentIndex?.[cursor];
          if (!Number.isInteger(parent) || parent < 0) break;
          cursor = parent;
        }
      }
    }

    const compactNodes = [];
    for (let i = 0; i < rawNodes.length; i += 1) if (keep.has(i) && rawNodes[i]) compactNodes.push(rawNodes[i]);

    return {
      id: `d${docIndex}`,
      url: strings[doc.documentURL] ?? meta.url,
      title: strings[doc.title] ?? (docIndex === 0 ? meta.title : ''),
      baseURL: strings[doc.baseURL] ?? undefined,
      contentWidth: round(doc.contentWidth),
      contentHeight: round(doc.contentHeight),
      scrollX: round(doc.scrollOffsetX),
      scrollY: round(doc.scrollOffsetY),
      nodes: compactNodes
    };
  });

  return {
    schema: SCHEMA,
    block: { id: BLOCK_ID, version: BLOCK_VERSION },
    capturedAt: new Date().toISOString(),
    provider: 'cdp-dom-snapshot',
    page: meta,
    styleProperties,
    styles: styleTable,
    documents,
    stats: {
      documents: documents.length,
      nodes: documents.reduce((sum, d) => sum + d.nodes.length, 0),
      uniqueStyles: styleTable.length
    }
  };
}

async function captureMeta(page) {
  return page.evaluate(() => ({
    url: location.href,
    title: document.title,
    viewport: {
      width: window.innerWidth,
      height: window.innerHeight,
      devicePixelRatio: window.devicePixelRatio
    },
    scroll: { x: window.scrollX, y: window.scrollY },
    document: {
      width: Math.max(document.documentElement.scrollWidth, document.body?.scrollWidth || 0),
      height: Math.max(document.documentElement.scrollHeight, document.body?.scrollHeight || 0)
    }
  }));
}

async function captureViaDom(page, meta, options, styleProperties) {
  const payload = await page.evaluate(({ styleProperties, includeHidden, maxTextLength, includeDataAttributes, includeInlineStyle }) => {
    const attrAllow = new Set([
      'id','class','role','href','target','rel','src','srcset','sizes','alt','title','type','name','value','placeholder',
      'width','height','loading','decoding','fetchpriority','for','action','method','checked','selected','disabled','hidden',
      'aria-label','aria-labelledby','aria-describedby','aria-hidden','aria-expanded','aria-controls','aria-current','aria-selected',
      'aria-pressed','aria-live'
    ]);
    const skipTags = new Set(['script','style','noscript','meta','link','base','title']);
    const styleTable = [];
    const styleMap = new Map();
    const nodes = [];

    const intern = (values) => {
      const key = JSON.stringify(values);
      if (styleMap.has(key)) return styleMap.get(key);
      const ref = styleTable.length;
      styleTable.push(values);
      styleMap.set(key, ref);
      return ref;
    };

    const attrsFor = (el) => {
      const out = {};
      for (const a of el.attributes || []) {
        const name = a.name.toLowerCase();
        if (name === 'style' && includeInlineStyle) out[name] = a.value;
        else if (attrAllow.has(name) || name.startsWith('aria-') || (includeDataAttributes && name.startsWith('data-'))) out[name] = a.value;
      }
      return Object.keys(out).length ? out : undefined;
    };

    const walk = (node, parentId) => {
      if (node.nodeType === Node.ELEMENT_NODE) {
        const tag = node.tagName.toLowerCase();
        if (skipTags.has(tag)) return;
        const cs = getComputedStyle(node);
        const r = node.getBoundingClientRect();
        const visible = r.width > 0 && r.height > 0 && cs.display !== 'none' && cs.visibility !== 'hidden' && Number.parseFloat(cs.opacity || '1') !== 0;
        if (!includeHidden && !visible && tag !== 'html' && tag !== 'body') return;
        const id = `d0:n${nodes.length}`;
        const values = styleProperties.map((p) => cs.getPropertyValue(p) || '');
        nodes.push({
          id,
          parent: parentId || undefined,
          kind: 'element',
          tag,
          attrs: attrsFor(node),
          currentSrc: node.currentSrc || undefined,
          clickable: (typeof node.matches === 'function' && node.matches('a,button,input,select,textarea,[role="button"],[onclick]')) || undefined,
          bounds: [r.x + window.scrollX, r.y + window.scrollY, r.width, r.height].map((n) => Math.round(n * 100) / 100),
          styleRef: intern(values),
          visible
        });
        for (const child of node.childNodes) walk(child, id);
        if (node.shadowRoot) for (const child of node.shadowRoot.childNodes) walk(child, id);
      } else if (node.nodeType === Node.TEXT_NODE) {
        const text = String(node.nodeValue || '').replace(/\s+/g, ' ').trim().slice(0, maxTextLength);
        if (!text || !parentId) return;
        const range = document.createRange();
        range.selectNodeContents(node);
        const r = range.getBoundingClientRect();
        if (!includeHidden && (r.width === 0 || r.height === 0)) return;
        nodes.push({
          id: `d0:n${nodes.length}`,
          parent: parentId,
          kind: 'text',
          text,
          bounds: [r.x + window.scrollX, r.y + window.scrollY, r.width, r.height].map((n) => Math.round(n * 100) / 100),
          visible: r.width > 0 && r.height > 0
        });
      }
    };

    const rootId = 'd0:n0';
    nodes.push({ id: rootId, kind: 'document', visible: true });
    if (document.documentElement) walk(document.documentElement, rootId);
    return { nodes, styles: styleTable };
  }, { styleProperties, includeHidden: options.includeHidden, maxTextLength: options.maxTextLength, includeDataAttributes: options.includeDataAttributes, includeInlineStyle: options.includeInlineStyle });

  const documentEntry = {
    id: 'd0',
    url: meta.url,
    title: meta.title,
    contentWidth: meta.document?.width,
    contentHeight: meta.document?.height,
    scrollX: meta.scroll?.x,
    scrollY: meta.scroll?.y,
    nodes: payload.nodes
  };
  return {
    schema: SCHEMA,
    block: { id: BLOCK_ID, version: BLOCK_VERSION },
    capturedAt: new Date().toISOString(),
    provider: 'dom-evaluate-fallback',
    page: meta,
    styleProperties,
    styles: payload.styles,
    documents: [documentEntry],
    stats: { documents: 1, nodes: payload.nodes.length, uniqueStyles: payload.styles.length },
    warnings: ['CDP DOMSnapshot was unavailable; fallback cannot fully flatten cross-origin iframes or closed shadow roots.']
  };
}

async function captureStructureFromPage(page, options = {}) {
  if (!page || typeof page.evaluate !== 'function') throw new TypeError('captureStructureFromPage requires a Playwright-compatible page object');
  const normalizedOptions = {
    provider: options.provider ?? 'auto',
    includeHidden: options.includeHidden ?? false,
    includeDataAttributes: options.includeDataAttributes ?? false,
    includeInlineStyle: options.includeInlineStyle ?? false,
    maxTextLength: Number.isFinite(options.maxTextLength) ? Math.max(0, options.maxTextLength) : 500
  };
  const styleProperties = Array.isArray(options.computedStyles) && options.computedStyles.length ? options.computedStyles.map(String) : STANDARD_STYLE_PROPERTIES;
  const meta = await captureMeta(page);

  if (normalizedOptions.provider !== 'dom') {
    const context = typeof page.context === 'function' ? page.context() : options.context;
    if (context && typeof context.newCDPSession === 'function') {
      let session;
      try {
        session = await context.newCDPSession(page);
        const raw = await session.send('DOMSnapshot.captureSnapshot', {
          computedStyles: styleProperties,
          includePaintOrder: true,
          includeDOMRects: false,
          includeBlendedBackgroundColors: false,
          includeTextColorOpacities: false
        });
        return normalizeCdpSnapshot(raw, meta, normalizedOptions, styleProperties);
      } catch (error) {
        if (normalizedOptions.provider === 'cdp') throw error;
      } finally {
        if (session && typeof session.detach === 'function') {
          try { await session.detach(); } catch {}
        }
      }
    } else if (normalizedOptions.provider === 'cdp') {
      throw new Error('CDP provider requested but page context does not expose newCDPSession');
    }
  }

  return captureViaDom(page, meta, normalizedOptions, styleProperties);
}



const __peosStructure = await captureStructureFromPage(page, { provider: 'auto' });
const __peosFilename = 'page-structure-' + new URL(__peosStructure.page.url).hostname.replace(/[^a-z0-9.-]+/gi, '-') + '-' + Date.now() + '.json';
await page.evaluate(({ filename, text }) => {
  const blob = new Blob([text], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url; a.download = filename; a.style.display = 'none';
  document.documentElement.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}, { filename: __peosFilename, text: JSON.stringify(__peosStructure) });
({ status: 'success', block: __peosStructure.block, provider: __peosStructure.provider, url: __peosStructure.page.url, nodes: __peosStructure.stats.nodes, file: __peosFilename });
