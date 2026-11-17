#!/usr/bin/env python3
"""Native Wix Studio Two full-page writer for LocalDesign source recipe.

Only modifies an explicitly selected page in a FRESH official Origami export.
Never imports/publishes or controls a browser. CLI:
  compile: native page edit preserving Page wrapper and shared Header/Footer.
  finalize-media: after official 'wix origami upload-media', complete image.url.
Then official Wix lint+tsc+build, import, fresh re-export, Playwright QA.
"""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import urlsplit, unquote


class Blocked(Exception):
    pass


PAGE = 'localdesign.wix-page-recipe.v1'


def num(v):
    x = round(float(v), 3)
    return str(int(x)) if x.is_integer() else str(x)


def get_page(root, page, allow_home=False):
    # Wix Origami names Home '(home)' in the official export.
    # The default remains fail-closed for destructive Home replacements.
    if page == '(home)':
        if not allow_home:
            raise Blocked('Home replacement requires explicit --allow-home-target')
    elif not re.fullmatch('[a-z0-9-]+', page) or page == 'home':
        raise Blocked('Require an exact existing Wix page folder; Home is (home)')
    p = Path(root) / 'packages/site-app/src/pages' / page
    paths = [p / x for x in ('structure.jsx', 'layout.css', 'style.css', 'unmapped.json')]
    if not all(x.is_file() for x in paths):
        raise Blocked('Target page missing from fresh Wix Origami export')
    return p


def source_text_style_css(style):
    """Observed LocalDesign native text styling; reject non-CSS source markup."""
    props = {
        'fontFamily': 'font-family', 'fontSize': 'font-size',
        'lineHeight': 'line-height', 'letterSpacing': 'letter-spacing',
        'fontWeight': 'font-weight', 'fontStyle': 'font-style',
        'textTransform': 'text-transform', 'textAlign': 'text-align',
        'color': 'color',
    }
    rules = []
    for source_key, css_key in props.items():
        value = (style or {}).get(source_key)
        if value is None or value == '':
            continue
        value = str(value)
        if not re.fullmatch(r"""[a-zA-Z0-9 _'"#.,()%/+-]+""", value):
            raise Blocked('Invalid observed source text CSS property ' + source_key)
        rules.append(css_key + ':' + value)
    return '; '.join(rules)


def wix_theme_font_family(theme_css, tag):
    """Use a declared *native Wix site theme* font, never a guessed lookalike.
    The exported theme declares --wst-heading-N-font / --wst-paragraph-1-font.
    A missing token falls back to the native WRichText inherited family.
    """
    typ = ('heading-'+tag[1]) if re.fullmatch(r'h[1-6]', str(tag or '')) else 'paragraph-1'
    m = re.search(r'--wst-'+re.escape(typ)+r'-font\s*:\s*([^;]+);', theme_css)
    if not m:
        return None
    # The native Wix shorthand has weight, size/line-height, THEN family.
    shorthand=m.group(1).strip()
    family=re.search(r'/[^\s]+\s+(.+)
    d = f'--spx-ref-width:{bp}; --spx-resolver-type:fixed;'
    vis = 'visible' if float(height) > 0 else 'hidden'
    return (
        f'.{id} {{ {d} visibility:{vis}; width:auto; height:{num(height)}px; min-height:{num(height)}px; grid-row:{row}/{row+1}; grid-column:1/2; position:relative; align-self:stretch; justify-self:stretch; }}\n'
        + f'.{ic} {{ {d} width:100%; min-height:{num(height)}px; @origami-target internal-container-content-wrapper {{ position:relative; display:grid; grid-template-columns:minmax(0px,1fr); grid-template-rows:{num(height)}px; padding-top:0px; padding-right:0px; padding-bottom:0px; padding-left:0px; }} }}\n'
        + f'.{bg} {{ {d} grid-row:1/-1; grid-column:1/-1; align-self:stretch; justify-self:stretch; visibility:{vis}; }}\n'
    )


def css_element(cid, geo, bp):
    d = f'--spx-ref-width:{bp}; --spx-resolver-type:fixed;'
    if geo is None:
        return f'.{cid} {{ {d} visibility:hidden; width:0px; height:0px; grid-row:1/2; grid-column:1/2; margin-left:0px; margin-top:0px; margin-right:0px; margin-bottom:0px; }}\n'
    if bp == 390:
        x = num(geo['x'])+'px'
    else:
        off = geo['centerX']
        x = f'calc(50% {"+" if off >= 0 else "-"} {num(abs(off))}px)'
    return f'.{cid} {{ {d} visibility:visible; position:relative; width:{num(geo["w"])}px; height:{num(geo["h"])}px; grid-row:1/2; grid-column:1/2; align-self:start; justify-self:start; margin-left:{x}; margin-top:{num(geo["y"])}px; margin-bottom:0px; margin-right:0px; }}\n'


def paint(section, bp):
    source = section['desktopBackground' if bp != 390 else 'mobileBackground']
    vals = {(x.get('color'), x.get('image')) for x in source.get('candidates', [])}
    if source['status'] == 'AMBIGUOUS' or len(vals) > 1:
        # Showit can paint an opaque section base below a separately measured
        # native image element. Keep the base color only when the transparent
        # cover image is ALREADY represented by the exact source selector and
        # the exact captured viewport geometry; never drop an unknown layer.
        candidates = source.get('candidates', [])
        bases = [x for x in candidates if x.get('image') in ('none', None)
                 and x.get('color') not in ('transparent', 'rgba(0, 0, 0, 0)', None)]
        covers = [x for x in candidates if x.get('image') == 'SOURCE_IMAGE_URLS_SEPARATE'
                  and x.get('color') in ('transparent', 'rgba(0, 0, 0, 0)', None)]
        observed_key = 'mobile' if bp == 390 else 'desktop'
        if len(bases) == 1 and len(covers) == len(candidates)-1 and covers:
            for cover in covers:
                linked = [e for e in section['elements'] if
                          e.get('type') == 'image' and
                          e.get('sourceSelector') == cover.get('selector') and
                          e.get('asset') and e.get(observed_key)]
                if len(linked) != 1:
                    raise Blocked('Painted image layer lacks exact native image '+str(cover.get('selector')))
            vals = {(bases[0]['color'], bases[0].get('image'))}
        else:
            raise Blocked('Ambiguous section background '+section['sourceSelector'])
    if not vals:
        return None
    color, image = next(iter(vals))
    if image not in ('none', None):
        raise Blocked('Unmapped full-section painted image '+section['sourceSelector'])
    if color in ('transparent', 'rgba(0, 0, 0, 0)', None):
        return None
    if color.startswith('rgb('):
        ns = re.findall(r'\d+', color)
        if len(ns) == 3:
            color = '#' + ''.join(f'{int(x):02X}' for x in ns)
    return color



def native_video_payload(layer, video_files):
    """Construct Wix's verified native Background.videoMedia value from READY
    official Media Manager get-file-descriptor responses, not guessed links.
    """
    source = layer.get('sourceUrl')
    if layer.get('type') != 'video' or not source or not source.startswith('https://'):
        raise Blocked('Invalid source video layer')
    matches = [x.get('file', x) for x in (video_files or [])
               if x.get('file', x).get('sourceUrl') == source]
    if len(matches) != 1:
        raise Blocked('Require exactly one official Wix video Media descriptor for '+source)
    file = matches[0]
    if file.get('operationStatus') != 'READY' or file.get('mediaType') != 'VIDEO':
        raise Blocked('Wix video not READY for '+source)
    media_id = file.get('id')
    video = (file.get('media') or {}).get('video') or {}
    if not media_id or video.get('id') != media_id:
        raise Blocked('Wix video media ID mismatch for '+source)
    resolutions = []
    for rendition in video.get('resolutions', []):
        quality = rendition.get('quality')
        uri = rendition.get('url') or ''
        if rendition.get('format') != 'mp4' or quality not in ('1080p','720p','480p','360p'):
            continue
        path = urlsplit(uri)
        if path.scheme != 'https' or path.netloc != 'video.wixstatic.com' or not path.path.startswith('/video/'+media_id+'/'):
            raise Blocked('Unexpected Wix source rendition URL '+uri)
        resolutions.append({'quality':quality,'width':int(rendition['width']),'height':int(rendition['height']),
                            'types':[{'format':'mp4','uri':path.path.lstrip('/'),'url':uri}]})
    if not resolutions:
        raise Blocked('READY Wix source video has no native MP4 rendition')
    fps_str = ((file.get('additionalProperties') or {}).get('video') or {}).get('fps','30/1')
    try:
        x = fps_str.split('/')
        fps = float(x[0]) / float(x[1]) if len(x)==2 else float(fps_str)
    except (ValueError, ZeroDivisionError):
        raise Blocked('Invalid Wix video fps from official descriptor')
    if not 0 < fps <= 240:
        raise Blocked('Out-of-range Wix video fps')
    audio_bitrate = ((file.get('additionalProperties') or {}).get('video') or {}).get('audioBitrate',-1)
    return {'uri':'wix:video://v1/'+media_id+'/'+file['displayName'],
            'name':file['displayName'],'sources':resolutions,
            'adaptiveSources':[],'hasAudio':bool(isinstance(audio_bitrate,(int,float)) and audio_bitrate>0),
            'fps':fps}


def video_background_props(section, video_files, bp):
    layers = section.get('dynamicLayers') or []
    if not layers:
        return '', None
    if len(layers) != 1 or layers[0].get('type') != 'video':
        raise Blocked('Unsupported multiple/non-video native background layers in '+section['sourceSelector'])
    layer = layers[0]
    observed = layer.get('desktop') or layer.get('mobile')
    if not observed:
        raise Blocked('Video layer without source viewport evidence')
    for key in ('autoplay','loop','muted','objectFit'):
        if key not in observed:
            raise Blocked('Video layer missing '+key+' source evidence')
    if observed['objectFit'] != 'cover':
        raise Blocked('Video background fit not yet supported: '+str(observed['objectFit']))
    payload = native_video_payload(layer, video_files)
    js = json.dumps(payload,ensure_ascii=False)
    opts = ' videoMedia={'+js+'} autoplay={'+json.dumps(bool(observed['autoplay']))+'} loop={'+json.dumps(bool(observed['loop']))+'} muted={'+json.dumps(bool(observed['muted']))+'} fittingType="fill" showControls={false}'
    bp_layer = layer.get('desktop' if bp != 390 else 'mobile')
    opacity = float(bp_layer['opacity']) if bp_layer is not None else 0.0
    if opacity < 0 or opacity > 1:
        raise Blocked('Invalid captured video opacity')
    return opts, opacity


def retain_exported_rules(css, identifiers):
    """Keep only real Page wrapper/header/footer/background rules; discard old
    components when their corresponding authored Sections are replaced.
    Preserve nested Wix @origami-target blocks using balanced braces.
    """
    blocks = []
    pattern = re.compile(r'(?m)^\s*\.([a-zA-Z0-9_-]+)\s*\{')
    pos = 0
    while True:
        found = pattern.search(css, pos)
        if not found:
            break
        depth, i = 1, found.end()
        while i < len(css) and depth:
            if css[i] == '{':
                depth += 1
            elif css[i] == '}':
                depth -= 1
            i += 1
        if depth:
            raise Blocked('Unbalanced native Wix CSS block')
        if found.group(1) in identifiers:
            blocks.append(css[found.start():i])
        pos = i
    return '\n'.join(blocks)+'\n'


def measured_footer_height(recipe, viewport):
    """Existing source Chrome contract: keep the native Footer in page flow.
    A captured Footer must never be given a zero-height Wix grid track.
    """
    chrome=recipe.get('sourceChrome')
    if not chrome:
        return None  # Legacy recipes have no Footer source evidence.
    if viewport not in chrome:
        raise Blocked('Missing source Chrome evidence for '+viewport)
    footers=[c for c in chrome[viewport] if c.get('role')=='footer']
    if len(footers)!=1:
        raise Blocked('Expected exactly one measured donor Footer for '+viewport)
    r=footers[0].get('rect') or {}
    height=r.get('height')
    if not isinstance(height,(int,float)) or height<=0:
        raise Blocked('Invalid captured donor Footer height for '+viewport)
    return height


def update_page_grid(css, page_id, footer_id, heights, require_footer=True, allow_missing_page=False, footer_height=None):
    if footer_height is not None and (not isinstance(footer_height,(int,float)) or footer_height<=0):
        raise Blocked('Measured source Footer requires positive grid height')
    rows = '0px ' + ' '.join(num(h)+'px' for h in heights) + ' ' + (num(footer_height)+'px' if footer_height is not None else '0px')
    def replace_page(m):
        block = m.group()
        block, count = re.subn(r'grid-template-rows:\s*[^;\n}]+', 'grid-template-rows: '+rows, block, count=1)
        if count != 1:
            raise Blocked('Page grid-template-rows missing from real Wix export')
        return block
    css, count = re.subn(r'\.'+re.escape(page_id)+r'\s*\{[^{}]*\}', replace_page, css, count=1)
    if count != 1:
        if not allow_missing_page:
            raise Blocked('Page root layout rule missing')
        # Wix often inherits Page rows on mobile without repeating Page CSS.
        # Add only a page-local override inside the already verified mobile rule.
        css = f'.{page_id} {{ grid-template-columns: minmax(0px, 1fr); grid-template-rows: {rows}; }}\n' + css
    def replace_footer(m):
        block=m.group()
        block, c=re.subn(r'grid-row:\s*\d+\s*/\s*\d+', 'grid-row: '+str(len(heights)+2)+' / '+str(len(heights)+3), block, count=1)
        if c != 1:
            raise Blocked('Footer grid-row missing')
        return block
    css,count = re.subn(r'\.'+re.escape(footer_id)+r'\s*\{[^{}]*\}', replace_footer, css, count=1)
    if count != 1 and require_footer:
        raise Blocked('Shared Footer placement rule missing')
    return css


def compile_page(recipe, root, page, expected_id, allow_replace, video_files=None, allow_home=False, vector_files=None, allow_native_defaults=False):
    if recipe.get('schema') != PAGE:
        raise Blocked('Wrong full-page normalized recipe')
    if recipe.get('unsupported'):
        raise Blocked('Source unsupported elements: '+str(recipe['unsupported'][:3]))
    if not recipe.get('sections'):
        raise Blocked('No source sections')
    if not allow_replace:
        raise Blocked('Explicit --allow-replace-page required; existing page content will be replaced')
    desktop_width = recipe.get('desktopWidth', 1280)
    if desktop_width not in (1280, 1920):
        raise Blocked('Unsupported source desktopWidth: '+str(desktop_width))
    expected_view = 'desktop-'+str(desktop_width)
    if recipe.get('viewports') and (expected_view not in recipe['viewports'] or 'mobile-390' not in recipe['viewports']):
        raise Blocked('Recipe is missing observed source desktop/mobile viewports')
    folder = get_page(root, page, allow_home=allow_home)
    strpath = folder / 'structure.jsx'
    s = strpath.read_text()
    layout = (folder/'layout.css').read_text()
    sty = (folder/'style.css').read_text()
    mt = re.search(r'<Page\s+id="([^"]+)"', s)
    if not mt or mt.group(1) != expected_id:
        raise Blocked('Selected Wix page ID mismatch')
    if s.count('<Page') != 1:
        raise Blocked('Unexpected page structure')
    # Preserve exported Page wrapper, header/footer, metadata, shared globals;
    # replace only authored native Section children on this explicitly selected page.
    a = s.find('        <Section ')
    b = s.rfind('        </Section>')
    if a < 0 or b < a:
        raise Blocked('Could not safely locate native Section sequence')
    b += len('        </Section>')
    first, last = s[:a], s[b:]
    if '<Section ' in last:
        raise Blocked('Native Section structure not consecutive')
    if "import { Image }" not in first:
        first = "import { Image } from '@origami-wrappers/wixEditorElements/image'\n" + first
    if "import { WRichText }" not in first:
        first = "import { WRichText } from '@origami-wrappers/wixEditorElements/wrichtext'\n" + first
    if "import { media }" not in first:
        first = "import { media } from '@wix/sdk'\n" + first
    if "import { Background }" not in first or "import InternalContainer" not in first:
        raise Blocked('Current native Wix page does not expose required Background/InternalContainer contract')
    header = re.search(r'header=\{<[^>]*\bid="([^"]+)"', first)
    footer = re.search(r'footer=\{<[^>]*\bid="([^"]+)"', first)
    if not header or not footer:
        raise Blocked('Missing native Page header/footer wrappers')
    background = re.search(r'backgroundLayer=\{\[<Background\s+id="([^"]+)"', first)
    if not background:
        raise Blocked('Missing native Page background')
    media_blocks = list(re.finditer(r'@media\s*\(--variants-[^)]+\)\s*\{', layout))
    if len(media_blocks) != 1:
        raise Blocked('Require exactly one mobile page layout media rule; avoid silently collapsing additional Wix breakpoints')
    media = media_blocks[0]
    media_name = re.search(r'--variants-[a-zA-Z0-9_-]+', media.group(0)).group(0)
    theme_file = Path(root) / 'packages/site-app/src/global/themes/theme.css'
    if not theme_file.is_file():
        raise Blocked('Fresh Wix theme CSS missing')
    theme_css = theme_file.read_text()
    native_default_fallbacks = []
    media_definitions = {name: int(width) for name, width in re.findall(
        r'@custom-media\s+(--variants-[a-zA-Z0-9_-]+)\s+\(max-width:\s*([0-9]+)px\)', theme_css)}
    actual_mobile_max = media_definitions.get(media_name, -1)
    if actual_mobile_max >= 390 and actual_mobile_max <= 1023:
        target_mobile_name = media_name
    else:
        # The Wix 390 design breakpoint may be declared as max-width:389px;
        # at exactly 390 CSS px it never applies. Select an already exported,
        # narrower-than-desktop named breakpoint that includes captured 390.
        candidates = sorted((width, name) for name, width in media_definitions.items()
                            if 390 <= width <= 1023 and width < desktop_width)
        if not candidates:
            raise Blocked('No existing named Wix breakpoint covers observed mobile-390')
        target_mobile_name = candidates[0][1]
    mobile_at_rule = media.group(0).replace(media_name, target_mobile_name)
    desktop, mobile = layout[:media.start()], layout[media.end():]
    keep = {expected_id, header.group(1), footer.group(1), background.group(1)}
    desktop = retain_exported_rules(desktop, keep)
    mobile = retain_exported_rules(mobile.rsplit('}', 1)[0], keep)
    sty = retain_exported_rules(sty, keep)
    sec_js, dr, mr, ds, ms, ids, originals = [], [], [], [], [], [], []
    for idx, sec in enumerate(recipe['sections']):
        sid, ic, bg = f'ldv-s{idx:03d}', f'ldv-c{idx:03d}', f'ldv-b{idx:03d}'
        row = idx + 2
        hd, hm = sec['desktopSection']['height'], sec['mobileSection']['height']
        ds.append(hd); ms.append(hm)
        children = []
        for k, e in enumerate(sec['elements']):
            cid = f'ldv-e{idx:03d}-{k:03d}'
            ids.append(cid)
            originals.append({'sourceSelector': e['sourceSelector'], 'targetProvisionalId': cid,
                              'sourceSection': sec['sourceSelector'], 'type': e['type'], 'asset': e.get('asset')})
            dr.append(css_element(cid, e.get('desktop'), desktop_width))
            mr.append(css_element(cid, e.get('mobile'), 390))
            if e['type'] == 'image':
                asset = e.get('asset')
                if not asset or not asset.startswith(('http://', 'https://')):
                    raise Blocked('Exact original image URL absent '+e['sourceSelector'])
                name = unquote(urlsplit(asset).path.rsplit('/', 1)[-1])
                if name.lower().endswith('.svg'):
                    # An original SVG media image is native Wix SvgImage, not a
                    # fabricated PNG or a custom element. Media Manager must
                    # report its exact source URL as a READY VECTOR.
                    matching=[x for x in (vector_files or []) if
                        x.get('sourceUrl')==asset and
                        x.get('operationStatus')=='READY' and
                        x.get('mediaType')=='VECTOR' and
                        re.fullmatch(r'[^:/\s]+[.]svg',x.get('id') or '')]
                    if len(matching)!=1:
                        raise Blocked('Original SVG media not uniquely READY in Wix: '+asset)
                    media_id=matching[0]['id']
                    if "import { SvgImage }" not in first:
                        first="import { SvgImage } from '@origami-wrappers/wixEditorElements/svgimage'\n"+first
                    if "import { svg }" not in first:
                        first="import { svg } from '@wix/origami-runtime'\n"+first
                    children.append('                <SvgImage id="{id}" className="{id}" displayMode="fit" svgId={{svg(media.getShapeUrl(\'wix:image://v1/{mid}\').url, \'{mid}\')}} />'.format(id=cid,mid=media_id))
                    continue
                if not name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    raise Blocked('Unsupported source image type '+name)
                # Official upload-media scanner needs exported-compatible multiline Image.
                children.append('''                <Image
                    id="{id}"
                    className="{id}"
                    displayMode="fill"
                    image={{{{
                        name: {name},
                        uri: {url},
                        width: 1,
                        height: 1,
                        alt: 'Original source image',
                        type: 'Builder.Image',
                    }}}}
                />'''.format(id=cid, name=repr(name), url=repr(asset)))
            elif e['type'] == 'text':
                tag = e.get('tag')
                tag = tag if tag in ('p', 'h1', 'h2', 'h3', 'h4') else 'p'
                content = f'<{tag}>{html.escape(e.get("text") or "", quote=False)}</{tag}>'
                children.append(f'                <WRichText id="{cid}" className="{cid}" richText={{{{ id: "data-{cid}", type: "Builder.RichText", html: {json.dumps(content, ensure_ascii=False)} }}}} />')
                for style_key, is_mobile in (('desktopStyle', False), ('mobileStyle', True)):
                    source_style=resolve_wix_default_text_style(
                        e.get(style_key) or {}, tag, theme_css,
                        enabled=allow_native_defaults,
                        selector=e['sourceSelector'],
                        view='mobile-390' if is_mobile else expected_view,
                        fallbacks=native_default_fallbacks)
                    css = source_text_style_css(source_style)
                    if not css:
                        continue
                    rule = f'.{cid} {{ {css}; }}'
                    if is_mobile:
                        sty += '\n' + mobile_at_rule + '\n' + rule + '\n}\n'
                    else:
                        sty += '\n' + rule + '\n'
            else:
                raise Blocked('Unsupported source type '+str(e['type']))
        # Static source vector overlays are native Wix Line or SvgImage.
        # Each captured viewport is independent: two Wix nodes may represent
        # one donor selector when Desktop/Mobile geometry differs. Native
        # readback must verify each one; no resize/URL or position guesses.
        source_vectors=[v for v in recipe.get('sourceVectors',[]) if
                        v.get('ownerScope')=='page-flow' and
                        v.get('ownerSection')==sec['sourceSelector']]
        for vi,vector in enumerate(source_vectors):
            view=vector.get('view')
            if view not in (expected_view,'mobile-390'):
                raise Blocked('Unobserved vector viewport '+str(view))
            rect=vector.get('rect')
            if not isinstance(rect,dict) or not all(
                 isinstance(rect.get(n),(int,float)) for n in ('x','y','width','height')):
                raise Blocked('Missing measured original SVG geometry '+str(vector.get('sourceSelector')))
            source_section=sec['desktopSection' if view==expected_view else 'mobileSection']
            gx=rect['x']-source_section['x']
            gy=rect['y']-source_section['y']
            if view==expected_view:
                geometry={'centerX':gx-source_section['width']/2,
                          'y':gy,'w':rect['width'],'h':rect['height']}
                vector_desktop,vector_mobile=geometry,None
            else:
                geometry={'x':gx,'y':gy,'w':rect['width'],'h':rect['height']}
                vector_desktop,vector_mobile=None,geometry
            cid=f'ldv-v{idx:03d}-{vi:03d}'
            dr.append(css_element(cid,vector_desktop,desktop_width))
            mr.append(css_element(cid,vector_mobile,390))
            component=vector.get('nativeComponent')
            if component=='SvgImage':
                matching=[x for x in (vector_files or []) if
                    x.get('assetSha256')==vector.get('assetSha256') and
                    x.get('mediaType')=='VECTOR' and
                    x.get('operationStatus')=='READY' and
                    re.fullmatch(r'[^:/\s]+[.]svg',x.get('id') or '')]
                if len(matching)!=1:
                    raise Blocked('Original inline SVG media missing or ambiguous '+str(vector.get('sourceSelector')))
                media_id=matching[0]['id']
                if "import { SvgImage }" not in first:
                    first="import { SvgImage } from '@origami-wrappers/wixEditorElements/svgimage'\n"+first
                if "import { svg }" not in first:
                    first="import { svg } from '@wix/origami-runtime'\n"+first
                children.append('                <SvgImage id="{id}" className="{id}" displayMode="fit" svgId={{svg(media.getShapeUrl(\'wix:image://v1/{mid}\').url, \'{mid}\')}} />'.format(id=cid,mid=media_id))
            elif component=='Line':
                if "import { Line }" not in first:
                    first="import { Line } from '@origami-wrappers/wixEditorElements/line'\n"+first
                children.append(f'                <Line id="{cid}" className="{cid}" />')
                # Source se-line XML is a 1 px solid black line. Wix Line
                # takes width/height from source measured geometry above.
                sty += f'\n.{cid} {{ --preset:horizontal; --lineColor:#000000; --lineSize:1px; --type:Solid; }}\n'
            else:
                raise Blocked('No native Wix component for source vector '+str(component))
        video_props, video_opacity_desktop = video_background_props(sec, video_files, desktop_width)
        _, video_opacity_mobile = video_background_props(sec, video_files, 390)
        sec_js.append(f'''        <Section id="{sid}" className="{sid}">
            <InternalContainer id="{ic}" className="{ic}" backgroundLayer={{[<Background id="{bg}" className="{bg}"{video_props} />]}}>
{chr(10).join(children)}
            </InternalContainer>
        </Section>''')
        if video_props:
            sty += f'\n.{bg} {{ --backgroundMediaOpacity:{num(video_opacity_desktop)}; }}\n'
            sty += '\n'+mobile_at_rule+'\n'+f'.{bg} {{ --backgroundMediaOpacity:{num(video_opacity_mobile)}; }}'+'\n}\n'
        dr.append(css_section(sid, ic, bg, hd, row, desktop_width))
        mr.append(css_section(sid, ic, bg, hm, row, 390))
        for bp in (desktop_width, 390):
            color = paint(sec, bp)
            if color:
                rule = f'.{bg} {{ --backgroundImage:none; --backgroundColor:{color}; --backgroundColorOpacity:1; }}'
                if bp != 390:
                    sty += '\n' + rule + '\n'
                else:
                    sty += '\n' + mobile_at_rule + '\n' + rule + '\n}\n'
    newjsx = first + '\n'.join(sec_js) + '\n' + last
    desktop = update_page_grid(desktop, expected_id, footer.group(1), ds,
                               footer_height=measured_footer_height(recipe, expected_view))
    mobile = update_page_grid(mobile, expected_id, footer.group(1), ms,
                              require_footer=False, allow_missing_page=True,
                              footer_height=measured_footer_height(recipe, 'mobile-390'))
    newlayout = (desktop + '\n' + ''.join(dr) + '\n' + mobile_at_rule
                 + mobile + '\n' + ''.join(mr) + '\n}\n')
    unmapped = json.loads((folder/'unmapped.json').read_text())
    removed_section_ids = set(re.findall(r'<Section\s+id="([^"]+)"', s[a:b]))
    for component_id, data in list((unmapped.get('components') or {}).items()):
        if component_id not in removed_section_ids:
            # Existing Wix Page/Header/Footer/global metadata are not part of
            # the deleted section set. Preserve verbatim.
            continue
        if not isinstance(data,dict) or set(data) != {'anchors'}:
            raise Blocked('Unknown unmapped data on removed Section: ' + component_id)
        del unmapped['components'][component_id]
    (folder/'unmapped.json').write_text(json.dumps(unmapped, indent=2))
    (folder/'structure.jsx').write_text(newjsx)
    (folder/'layout.css').write_text(newlayout)
    (folder/'style.css').write_text(sty)
    (Path(root).parent/(page+'-localdesign-transfer-manifest.json')).write_text(json.dumps({
        'source': recipe['source'], 'sha256': recipe['sha256'],
        'pageId': expected_id, 'items': originals,
        'nativeDefaultsEnabled': bool(allow_native_defaults),
        'nativeDefaultFallbacks': native_default_fallbacks,
        'sourceUnsupported': recipe.get('unsupported',[]),
        'sourceVisualParity': 'PARTIAL' if native_default_fallbacks else 'NOT_ASSESSED'
    }, indent=2))
    print(json.dumps({'status': 'WORKSPACE_ONLY_NO_IMPORT', 'pageId': expected_id,
                      'sections': len(sec_js), 'elements': len(ids),
                      'nativeDefaultFallbacks':len(native_default_fallbacks),
                      'sourceVisualParity':'PARTIAL' if native_default_fallbacks else 'NOT_ASSESSED',
                      'images': sum(e['type']=='image' for x in recipe['sections'] for e in x['elements'])}))


def finalize_media(root, page, allow_home=False):
    p = get_page(root, page, allow_home=allow_home) / 'structure.jsx'
    s = p.read_text()
    pat = r'(<Image\s[\s\S]*?\bimage=\{\{)([\s\S]*?)(\}\}\s*/>)'
    count = 0
    def replacement(match):
        nonlocal count
        body = match.group(2)
        def fld(key):
            m = re.search(r'\b'+re.escape(key)+r':\s*[\'"]([^\'"]+)[\'"]', body)
            if m:
                return m.group(1)
            m = re.search(r'\b'+re.escape(key)+r':\s*(\d+)', body)
            return m.group(1) if m else None
        uri, name, w, h = [fld(k) for k in ('uri', 'name', 'width', 'height')]
        if not uri or not re.fullmatch(r'[^:/\s]+\.(jpg|jpeg|gif|png|webp)', uri, re.I):
            raise Blocked('Original media not imported as Wix ID; run official upload-media')
        if not all((name, w, h)):
            raise Blocked('Missing official image metadata')
        if 'url:' in body:
            return match.group()
        url = f'wix:image://v1/{uri}/{name}#originWidth={w}&originHeight={h}'
        body += f'\n                        url: media.getCroppedImageUrl({url!r},0,0,0,0,{w},{h},{{name:{name!r},autoEncode:true,devicePixelRatio:1}}),\n'
        count += 1
        return match.group(1)+body+match.group(3)
    s = re.sub(pat, replacement, s)
    p.write_text(s)
    print(json.dumps({'status': 'MEDIA_NATIVE_FINALIZED_NO_IMPORT', 'images': count}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('compile', 'finalize-media'))
    parser.add_argument('--recipe')
    parser.add_argument('--export', required=True)
    parser.add_argument('--page', required=True)
    parser.add_argument('--page-id')
    parser.add_argument('--allow-replace-page', action='store_true')
    parser.add_argument('--allow-home-target', action='store_true', help='Only for an explicitly approved existing Wix Home page')
    parser.add_argument('--allow-native-defaults', action='store_true', help='Use native Wix theme font fallback, preserve source geometry and report partial visual parity')
    parser.add_argument('--video-media-manifest', help='JSON {files:[official READY Wix file descriptors]}')
    parser.add_argument('--vector-media-manifest', help='JSON {files:[sourceUrl, id, operationStatus READY, mediaType VECTOR]}')
    args = parser.parse_args()
    try:
        if args.action == 'compile':
            if not args.recipe or not args.page_id:
                raise Blocked('Require --recipe and --page-id')
            manifest = json.loads(Path(args.video_media_manifest).read_text()) if args.video_media_manifest else {}
            if manifest and (not isinstance(manifest,dict) or not isinstance(manifest.get('files'),list)):
                raise Blocked('Video media manifest must contain files[]')
            vector_manifest = json.loads(Path(args.vector_media_manifest).read_text()) if args.vector_media_manifest else {}
            if vector_manifest and (not isinstance(vector_manifest,dict) or not isinstance(vector_manifest.get('files'),list)):
                raise Blocked('Vector media manifest must contain files[]')
            compile_page(json.loads(Path(args.recipe).read_text()),
                         args.export, args.page, args.page_id, args.allow_replace_page,
                         manifest.get('files',[]), allow_home=args.allow_home_target,
                         vector_files=vector_manifest.get('files',[]),
                         allow_native_defaults=args.allow_native_defaults)
        else:
            finalize_media(args.export, args.page, allow_home=args.allow_home_target)
    except (Blocked, KeyError, TypeError, ValueError) as e:
        parser.exit(2, 'BLOCKED: '+str(e)+'\n')


if __name__ == '__main__':
    main()
,shorthand)
    if not family:
        return None
    value=family.group(1).strip()
    # No arbitrary CSS interpolation; only static native system/theme family.
    if not re.fullmatch(r'[a-zA-Z0-9 _\'"-]+',value):
        return None
    return value


def wix_theme_available_families(theme_css):
    """A typeface is verifiably present if in current Wix theme defaults.
    This conservative set avoids declaring uninstalled donor fonts available.
    """
    families=set()
    for tag in ('h1','h2','h3','h4','h5','h6','p'):
        font=wix_theme_font_family(theme_css,tag)
        if font:
            families.add(font.strip().strip('"\'').lower())
    return families


def resolve_wix_default_text_style(source_style, tag, theme_css, *,
                                   enabled, selector, view, fallbacks):
    """Preserve donor metrics while using the target site's native font.
    Record the exact source selector, view and reason for owner refinement.
    """
    style=dict(source_style or {})
    source_font=style.get('fontFamily')
    if not enabled or not source_font:
        return style
    # Computed font-family may be a fallback stack. Availability of a
    # generic fallback in that stack does NOT prove the intended first font.
    primary=str(source_font).split(',')[0].strip().strip('"\'')
    available=wix_theme_available_families(theme_css)
    if primary.lower() not in available:
        default=wix_theme_font_family(theme_css,tag)
        if default:
            style['fontFamily']=default
            status='WIX_THEME_DEFAULT_FONT'
        else:
            style.pop('fontFamily',None) # native WRichText inherited default
            status='WIX_INHERITED_DEFAULT_FONT'
        fallbacks.append({
            'sourceSelector':selector,'view':view,'component':'WRichText',
            'reason':'SOURCE_FONT_NOT_IN_TARGET_WIX_THEME',
            'originalFontFamily':str(source_font),
            'wixDefaultFontFamily':default,
            'status':status
        })
    return style


def css_section(id, ic, bg, height, row, bp):
    d = f'--spx-ref-width:{bp}; --spx-resolver-type:fixed;'
    vis = 'visible' if float(height) > 0 else 'hidden'
    return (
        f'.{id} {{ {d} visibility:{vis}; width:auto; height:{num(height)}px; min-height:{num(height)}px; grid-row:{row}/{row+1}; grid-column:1/2; position:relative; align-self:stretch; justify-self:stretch; }}\n'
        + f'.{ic} {{ {d} width:100%; min-height:{num(height)}px; @origami-target internal-container-content-wrapper {{ position:relative; display:grid; grid-template-columns:minmax(0px,1fr); grid-template-rows:{num(height)}px; padding-top:0px; padding-right:0px; padding-bottom:0px; padding-left:0px; }} }}\n'
        + f'.{bg} {{ {d} grid-row:1/-1; grid-column:1/-1; align-self:stretch; justify-self:stretch; visibility:{vis}; }}\n'
    )


def css_element(cid, geo, bp):
    d = f'--spx-ref-width:{bp}; --spx-resolver-type:fixed;'
    if geo is None:
        return f'.{cid} {{ {d} visibility:hidden; width:0px; height:0px; grid-row:1/2; grid-column:1/2; margin-left:0px; margin-top:0px; margin-right:0px; margin-bottom:0px; }}\n'
    if bp == 390:
        x = num(geo['x'])+'px'
    else:
        off = geo['centerX']
        x = f'calc(50% {"+" if off >= 0 else "-"} {num(abs(off))}px)'
    return f'.{cid} {{ {d} visibility:visible; position:relative; width:{num(geo["w"])}px; height:{num(geo["h"])}px; grid-row:1/2; grid-column:1/2; align-self:start; justify-self:start; margin-left:{x}; margin-top:{num(geo["y"])}px; margin-bottom:0px; margin-right:0px; }}\n'


def paint(section, bp):
    source = section['desktopBackground' if bp != 390 else 'mobileBackground']
    vals = {(x.get('color'), x.get('image')) for x in source.get('candidates', [])}
    if source['status'] == 'AMBIGUOUS' or len(vals) > 1:
        # Showit can paint an opaque section base below a separately measured
        # native image element. Keep the base color only when the transparent
        # cover image is ALREADY represented by the exact source selector and
        # the exact captured viewport geometry; never drop an unknown layer.
        candidates = source.get('candidates', [])
        bases = [x for x in candidates if x.get('image') in ('none', None)
                 and x.get('color') not in ('transparent', 'rgba(0, 0, 0, 0)', None)]
        covers = [x for x in candidates if x.get('image') == 'SOURCE_IMAGE_URLS_SEPARATE'
                  and x.get('color') in ('transparent', 'rgba(0, 0, 0, 0)', None)]
        observed_key = 'mobile' if bp == 390 else 'desktop'
        if len(bases) == 1 and len(covers) == len(candidates)-1 and covers:
            for cover in covers:
                linked = [e for e in section['elements'] if
                          e.get('type') == 'image' and
                          e.get('sourceSelector') == cover.get('selector') and
                          e.get('asset') and e.get(observed_key)]
                if len(linked) != 1:
                    raise Blocked('Painted image layer lacks exact native image '+str(cover.get('selector')))
            vals = {(bases[0]['color'], bases[0].get('image'))}
        else:
            raise Blocked('Ambiguous section background '+section['sourceSelector'])
    if not vals:
        return None
    color, image = next(iter(vals))
    if image not in ('none', None):
        raise Blocked('Unmapped full-section painted image '+section['sourceSelector'])
    if color in ('transparent', 'rgba(0, 0, 0, 0)', None):
        return None
    if color.startswith('rgb('):
        ns = re.findall(r'\d+', color)
        if len(ns) == 3:
            color = '#' + ''.join(f'{int(x):02X}' for x in ns)
    return color



def native_video_payload(layer, video_files):
    """Construct Wix's verified native Background.videoMedia value from READY
    official Media Manager get-file-descriptor responses, not guessed links.
    """
    source = layer.get('sourceUrl')
    if layer.get('type') != 'video' or not source or not source.startswith('https://'):
        raise Blocked('Invalid source video layer')
    matches = [x.get('file', x) for x in (video_files or [])
               if x.get('file', x).get('sourceUrl') == source]
    if len(matches) != 1:
        raise Blocked('Require exactly one official Wix video Media descriptor for '+source)
    file = matches[0]
    if file.get('operationStatus') != 'READY' or file.get('mediaType') != 'VIDEO':
        raise Blocked('Wix video not READY for '+source)
    media_id = file.get('id')
    video = (file.get('media') or {}).get('video') or {}
    if not media_id or video.get('id') != media_id:
        raise Blocked('Wix video media ID mismatch for '+source)
    resolutions = []
    for rendition in video.get('resolutions', []):
        quality = rendition.get('quality')
        uri = rendition.get('url') or ''
        if rendition.get('format') != 'mp4' or quality not in ('1080p','720p','480p','360p'):
            continue
        path = urlsplit(uri)
        if path.scheme != 'https' or path.netloc != 'video.wixstatic.com' or not path.path.startswith('/video/'+media_id+'/'):
            raise Blocked('Unexpected Wix source rendition URL '+uri)
        resolutions.append({'quality':quality,'width':int(rendition['width']),'height':int(rendition['height']),
                            'types':[{'format':'mp4','uri':path.path.lstrip('/'),'url':uri}]})
    if not resolutions:
        raise Blocked('READY Wix source video has no native MP4 rendition')
    fps_str = ((file.get('additionalProperties') or {}).get('video') or {}).get('fps','30/1')
    try:
        x = fps_str.split('/')
        fps = float(x[0]) / float(x[1]) if len(x)==2 else float(fps_str)
    except (ValueError, ZeroDivisionError):
        raise Blocked('Invalid Wix video fps from official descriptor')
    if not 0 < fps <= 240:
        raise Blocked('Out-of-range Wix video fps')
    audio_bitrate = ((file.get('additionalProperties') or {}).get('video') or {}).get('audioBitrate',-1)
    return {'uri':'wix:video://v1/'+media_id+'/'+file['displayName'],
            'name':file['displayName'],'sources':resolutions,
            'adaptiveSources':[],'hasAudio':bool(isinstance(audio_bitrate,(int,float)) and audio_bitrate>0),
            'fps':fps}


def video_background_props(section, video_files, bp):
    layers = section.get('dynamicLayers') or []
    if not layers:
        return '', None
    if len(layers) != 1 or layers[0].get('type') != 'video':
        raise Blocked('Unsupported multiple/non-video native background layers in '+section['sourceSelector'])
    layer = layers[0]
    observed = layer.get('desktop') or layer.get('mobile')
    if not observed:
        raise Blocked('Video layer without source viewport evidence')
    for key in ('autoplay','loop','muted','objectFit'):
        if key not in observed:
            raise Blocked('Video layer missing '+key+' source evidence')
    if observed['objectFit'] != 'cover':
        raise Blocked('Video background fit not yet supported: '+str(observed['objectFit']))
    payload = native_video_payload(layer, video_files)
    js = json.dumps(payload,ensure_ascii=False)
    opts = ' videoMedia={'+js+'} autoplay={'+json.dumps(bool(observed['autoplay']))+'} loop={'+json.dumps(bool(observed['loop']))+'} muted={'+json.dumps(bool(observed['muted']))+'} fittingType="fill" showControls={false}'
    bp_layer = layer.get('desktop' if bp != 390 else 'mobile')
    opacity = float(bp_layer['opacity']) if bp_layer is not None else 0.0
    if opacity < 0 or opacity > 1:
        raise Blocked('Invalid captured video opacity')
    return opts, opacity


def retain_exported_rules(css, identifiers):
    """Keep only real Page wrapper/header/footer/background rules; discard old
    components when their corresponding authored Sections are replaced.
    Preserve nested Wix @origami-target blocks using balanced braces.
    """
    blocks = []
    pattern = re.compile(r'(?m)^\s*\.([a-zA-Z0-9_-]+)\s*\{')
    pos = 0
    while True:
        found = pattern.search(css, pos)
        if not found:
            break
        depth, i = 1, found.end()
        while i < len(css) and depth:
            if css[i] == '{':
                depth += 1
            elif css[i] == '}':
                depth -= 1
            i += 1
        if depth:
            raise Blocked('Unbalanced native Wix CSS block')
        if found.group(1) in identifiers:
            blocks.append(css[found.start():i])
        pos = i
    return '\n'.join(blocks)+'\n'


def measured_footer_height(recipe, viewport):
    """Existing source Chrome contract: keep the native Footer in page flow.
    A captured Footer must never be given a zero-height Wix grid track.
    """
    chrome=recipe.get('sourceChrome')
    if not chrome:
        return None  # Legacy recipes have no Footer source evidence.
    if viewport not in chrome:
        raise Blocked('Missing source Chrome evidence for '+viewport)
    footers=[c for c in chrome[viewport] if c.get('role')=='footer']
    if len(footers)!=1:
        raise Blocked('Expected exactly one measured donor Footer for '+viewport)
    r=footers[0].get('rect') or {}
    height=r.get('height')
    if not isinstance(height,(int,float)) or height<=0:
        raise Blocked('Invalid captured donor Footer height for '+viewport)
    return height


def update_page_grid(css, page_id, footer_id, heights, require_footer=True, allow_missing_page=False, footer_height=None):
    if footer_height is not None and (not isinstance(footer_height,(int,float)) or footer_height<=0):
        raise Blocked('Measured source Footer requires positive grid height')
    rows = '0px ' + ' '.join(num(h)+'px' for h in heights) + ' ' + (num(footer_height)+'px' if footer_height is not None else '0px')
    def replace_page(m):
        block = m.group()
        block, count = re.subn(r'grid-template-rows:\s*[^;\n}]+', 'grid-template-rows: '+rows, block, count=1)
        if count != 1:
            raise Blocked('Page grid-template-rows missing from real Wix export')
        return block
    css, count = re.subn(r'\.'+re.escape(page_id)+r'\s*\{[^{}]*\}', replace_page, css, count=1)
    if count != 1:
        if not allow_missing_page:
            raise Blocked('Page root layout rule missing')
        # Wix often inherits Page rows on mobile without repeating Page CSS.
        # Add only a page-local override inside the already verified mobile rule.
        css = f'.{page_id} {{ grid-template-columns: minmax(0px, 1fr); grid-template-rows: {rows}; }}\n' + css
    def replace_footer(m):
        block=m.group()
        block, c=re.subn(r'grid-row:\s*\d+\s*/\s*\d+', 'grid-row: '+str(len(heights)+2)+' / '+str(len(heights)+3), block, count=1)
        if c != 1:
            raise Blocked('Footer grid-row missing')
        return block
    css,count = re.subn(r'\.'+re.escape(footer_id)+r'\s*\{[^{}]*\}', replace_footer, css, count=1)
    if count != 1 and require_footer:
        raise Blocked('Shared Footer placement rule missing')
    return css


def compile_page(recipe, root, page, expected_id, allow_replace, video_files=None, allow_home=False, vector_files=None):
    if recipe.get('schema') != PAGE:
        raise Blocked('Wrong full-page normalized recipe')
    if recipe.get('unsupported'):
        raise Blocked('Source unsupported elements: '+str(recipe['unsupported'][:3]))
    if not recipe.get('sections'):
        raise Blocked('No source sections')
    if not allow_replace:
        raise Blocked('Explicit --allow-replace-page required; existing page content will be replaced')
    desktop_width = recipe.get('desktopWidth', 1280)
    if desktop_width not in (1280, 1920):
        raise Blocked('Unsupported source desktopWidth: '+str(desktop_width))
    expected_view = 'desktop-'+str(desktop_width)
    if recipe.get('viewports') and (expected_view not in recipe['viewports'] or 'mobile-390' not in recipe['viewports']):
        raise Blocked('Recipe is missing observed source desktop/mobile viewports')
    folder = get_page(root, page, allow_home=allow_home)
    strpath = folder / 'structure.jsx'
    s = strpath.read_text()
    layout = (folder/'layout.css').read_text()
    sty = (folder/'style.css').read_text()
    mt = re.search(r'<Page\s+id="([^"]+)"', s)
    if not mt or mt.group(1) != expected_id:
        raise Blocked('Selected Wix page ID mismatch')
    if s.count('<Page') != 1:
        raise Blocked('Unexpected page structure')
    # Preserve exported Page wrapper, header/footer, metadata, shared globals;
    # replace only authored native Section children on this explicitly selected page.
    a = s.find('        <Section ')
    b = s.rfind('        </Section>')
    if a < 0 or b < a:
        raise Blocked('Could not safely locate native Section sequence')
    b += len('        </Section>')
    first, last = s[:a], s[b:]
    if '<Section ' in last:
        raise Blocked('Native Section structure not consecutive')
    if "import { Image }" not in first:
        first = "import { Image } from '@origami-wrappers/wixEditorElements/image'\n" + first
    if "import { WRichText }" not in first:
        first = "import { WRichText } from '@origami-wrappers/wixEditorElements/wrichtext'\n" + first
    if "import { media }" not in first:
        first = "import { media } from '@wix/sdk'\n" + first
    if "import { Background }" not in first or "import InternalContainer" not in first:
        raise Blocked('Current native Wix page does not expose required Background/InternalContainer contract')
    header = re.search(r'header=\{<[^>]*\bid="([^"]+)"', first)
    footer = re.search(r'footer=\{<[^>]*\bid="([^"]+)"', first)
    if not header or not footer:
        raise Blocked('Missing native Page header/footer wrappers')
    background = re.search(r'backgroundLayer=\{\[<Background\s+id="([^"]+)"', first)
    if not background:
        raise Blocked('Missing native Page background')
    media_blocks = list(re.finditer(r'@media\s*\(--variants-[^)]+\)\s*\{', layout))
    if len(media_blocks) != 1:
        raise Blocked('Require exactly one mobile page layout media rule; avoid silently collapsing additional Wix breakpoints')
    media = media_blocks[0]
    media_name = re.search(r'--variants-[a-zA-Z0-9_-]+', media.group(0)).group(0)
    theme_file = Path(root) / 'packages/site-app/src/global/themes/theme.css'
    if not theme_file.is_file():
        raise Blocked('Fresh Wix theme CSS missing')
    theme_css = theme_file.read_text()
    media_definitions = {name: int(width) for name, width in re.findall(
        r'@custom-media\s+(--variants-[a-zA-Z0-9_-]+)\s+\(max-width:\s*([0-9]+)px\)', theme_css)}
    actual_mobile_max = media_definitions.get(media_name, -1)
    if actual_mobile_max >= 390 and actual_mobile_max <= 1023:
        target_mobile_name = media_name
    else:
        # The Wix 390 design breakpoint may be declared as max-width:389px;
        # at exactly 390 CSS px it never applies. Select an already exported,
        # narrower-than-desktop named breakpoint that includes captured 390.
        candidates = sorted((width, name) for name, width in media_definitions.items()
                            if 390 <= width <= 1023 and width < desktop_width)
        if not candidates:
            raise Blocked('No existing named Wix breakpoint covers observed mobile-390')
        target_mobile_name = candidates[0][1]
    mobile_at_rule = media.group(0).replace(media_name, target_mobile_name)
    desktop, mobile = layout[:media.start()], layout[media.end():]
    keep = {expected_id, header.group(1), footer.group(1), background.group(1)}
    desktop = retain_exported_rules(desktop, keep)
    mobile = retain_exported_rules(mobile.rsplit('}', 1)[0], keep)
    sty = retain_exported_rules(sty, keep)
    sec_js, dr, mr, ds, ms, ids, originals = [], [], [], [], [], [], []
    for idx, sec in enumerate(recipe['sections']):
        sid, ic, bg = f'ldv-s{idx:03d}', f'ldv-c{idx:03d}', f'ldv-b{idx:03d}'
        row = idx + 2
        hd, hm = sec['desktopSection']['height'], sec['mobileSection']['height']
        ds.append(hd); ms.append(hm)
        children = []
        for k, e in enumerate(sec['elements']):
            cid = f'ldv-e{idx:03d}-{k:03d}'
            ids.append(cid)
            originals.append({'sourceSelector': e['sourceSelector'], 'targetProvisionalId': cid,
                              'sourceSection': sec['sourceSelector'], 'type': e['type'], 'asset': e.get('asset')})
            dr.append(css_element(cid, e.get('desktop'), desktop_width))
            mr.append(css_element(cid, e.get('mobile'), 390))
            if e['type'] == 'image':
                asset = e.get('asset')
                if not asset or not asset.startswith(('http://', 'https://')):
                    raise Blocked('Exact original image URL absent '+e['sourceSelector'])
                name = unquote(urlsplit(asset).path.rsplit('/', 1)[-1])
                if name.lower().endswith('.svg'):
                    # An original SVG media image is native Wix SvgImage, not a
                    # fabricated PNG or a custom element. Media Manager must
                    # report its exact source URL as a READY VECTOR.
                    matching=[x for x in (vector_files or []) if
                        x.get('sourceUrl')==asset and
                        x.get('operationStatus')=='READY' and
                        x.get('mediaType')=='VECTOR' and
                        re.fullmatch(r'[^:/\s]+[.]svg',x.get('id') or '')]
                    if len(matching)!=1:
                        raise Blocked('Original SVG media not uniquely READY in Wix: '+asset)
                    media_id=matching[0]['id']
                    if "import { SvgImage }" not in first:
                        first="import { SvgImage } from '@origami-wrappers/wixEditorElements/svgimage'\n"+first
                    if "import { svg }" not in first:
                        first="import { svg } from '@wix/origami-runtime'\n"+first
                    children.append('                <SvgImage id="{id}" className="{id}" displayMode="fit" svgId={{svg(media.getShapeUrl(\'wix:image://v1/{mid}\').url, \'{mid}\')}} />'.format(id=cid,mid=media_id))
                    continue
                if not name.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.webp')):
                    raise Blocked('Unsupported source image type '+name)
                # Official upload-media scanner needs exported-compatible multiline Image.
                children.append('''                <Image
                    id="{id}"
                    className="{id}"
                    displayMode="fill"
                    image={{{{
                        name: {name},
                        uri: {url},
                        width: 1,
                        height: 1,
                        alt: 'Original source image',
                        type: 'Builder.Image',
                    }}}}
                />'''.format(id=cid, name=repr(name), url=repr(asset)))
            elif e['type'] == 'text':
                tag = e.get('tag')
                tag = tag if tag in ('p', 'h1', 'h2', 'h3', 'h4') else 'p'
                content = f'<{tag}>{html.escape(e.get("text") or "", quote=False)}</{tag}>'
                children.append(f'                <WRichText id="{cid}" className="{cid}" richText={{{{ id: "data-{cid}", type: "Builder.RichText", html: {json.dumps(content, ensure_ascii=False)} }}}} />')
                for style_key, is_mobile in (('desktopStyle', False), ('mobileStyle', True)):
                    css = source_text_style_css(e.get(style_key) or {})
                    if not css:
                        continue
                    rule = f'.{cid} {{ {css}; }}'
                    if is_mobile:
                        sty += '\n' + mobile_at_rule + '\n' + rule + '\n}\n'
                    else:
                        sty += '\n' + rule + '\n'
            else:
                raise Blocked('Unsupported source type '+str(e['type']))
        # Static source vector overlays are native Wix Line or SvgImage.
        # Each captured viewport is independent: two Wix nodes may represent
        # one donor selector when Desktop/Mobile geometry differs. Native
        # readback must verify each one; no resize/URL or position guesses.
        source_vectors=[v for v in recipe.get('sourceVectors',[]) if
                        v.get('ownerScope')=='page-flow' and
                        v.get('ownerSection')==sec['sourceSelector']]
        for vi,vector in enumerate(source_vectors):
            view=vector.get('view')
            if view not in (expected_view,'mobile-390'):
                raise Blocked('Unobserved vector viewport '+str(view))
            rect=vector.get('rect')
            if not isinstance(rect,dict) or not all(
                 isinstance(rect.get(n),(int,float)) for n in ('x','y','width','height')):
                raise Blocked('Missing measured original SVG geometry '+str(vector.get('sourceSelector')))
            source_section=sec['desktopSection' if view==expected_view else 'mobileSection']
            gx=rect['x']-source_section['x']
            gy=rect['y']-source_section['y']
            if view==expected_view:
                geometry={'centerX':gx-source_section['width']/2,
                          'y':gy,'w':rect['width'],'h':rect['height']}
                vector_desktop,vector_mobile=geometry,None
            else:
                geometry={'x':gx,'y':gy,'w':rect['width'],'h':rect['height']}
                vector_desktop,vector_mobile=None,geometry
            cid=f'ldv-v{idx:03d}-{vi:03d}'
            dr.append(css_element(cid,vector_desktop,desktop_width))
            mr.append(css_element(cid,vector_mobile,390))
            component=vector.get('nativeComponent')
            if component=='SvgImage':
                matching=[x for x in (vector_files or []) if
                    x.get('assetSha256')==vector.get('assetSha256') and
                    x.get('mediaType')=='VECTOR' and
                    x.get('operationStatus')=='READY' and
                    re.fullmatch(r'[^:/\s]+[.]svg',x.get('id') or '')]
                if len(matching)!=1:
                    raise Blocked('Original inline SVG media missing or ambiguous '+str(vector.get('sourceSelector')))
                media_id=matching[0]['id']
                if "import { SvgImage }" not in first:
                    first="import { SvgImage } from '@origami-wrappers/wixEditorElements/svgimage'\n"+first
                if "import { svg }" not in first:
                    first="import { svg } from '@wix/origami-runtime'\n"+first
                children.append('                <SvgImage id="{id}" className="{id}" displayMode="fit" svgId={{svg(media.getShapeUrl(\'wix:image://v1/{mid}\').url, \'{mid}\')}} />'.format(id=cid,mid=media_id))
            elif component=='Line':
                if "import { Line }" not in first:
                    first="import { Line } from '@origami-wrappers/wixEditorElements/line'\n"+first
                children.append(f'                <Line id="{cid}" className="{cid}" />')
                # Source se-line XML is a 1 px solid black line. Wix Line
                # takes width/height from source measured geometry above.
                sty += f'\n.{cid} {{ --preset:horizontal; --lineColor:#000000; --lineSize:1px; --type:Solid; }}\n'
            else:
                raise Blocked('No native Wix component for source vector '+str(component))
        video_props, video_opacity_desktop = video_background_props(sec, video_files, desktop_width)
        _, video_opacity_mobile = video_background_props(sec, video_files, 390)
        sec_js.append(f'''        <Section id="{sid}" className="{sid}">
            <InternalContainer id="{ic}" className="{ic}" backgroundLayer={{[<Background id="{bg}" className="{bg}"{video_props} />]}}>
{chr(10).join(children)}
            </InternalContainer>
        </Section>''')
        if video_props:
            sty += f'\n.{bg} {{ --backgroundMediaOpacity:{num(video_opacity_desktop)}; }}\n'
            sty += '\n'+mobile_at_rule+'\n'+f'.{bg} {{ --backgroundMediaOpacity:{num(video_opacity_mobile)}; }}'+'\n}\n'
        dr.append(css_section(sid, ic, bg, hd, row, desktop_width))
        mr.append(css_section(sid, ic, bg, hm, row, 390))
        for bp in (desktop_width, 390):
            color = paint(sec, bp)
            if color:
                rule = f'.{bg} {{ --backgroundImage:none; --backgroundColor:{color}; --backgroundColorOpacity:1; }}'
                if bp != 390:
                    sty += '\n' + rule + '\n'
                else:
                    sty += '\n' + mobile_at_rule + '\n' + rule + '\n}\n'
    newjsx = first + '\n'.join(sec_js) + '\n' + last
    desktop = update_page_grid(desktop, expected_id, footer.group(1), ds,
                               footer_height=measured_footer_height(recipe, expected_view))
    mobile = update_page_grid(mobile, expected_id, footer.group(1), ms,
                              require_footer=False, allow_missing_page=True,
                              footer_height=measured_footer_height(recipe, 'mobile-390'))
    newlayout = (desktop + '\n' + ''.join(dr) + '\n' + mobile_at_rule
                 + mobile + '\n' + ''.join(mr) + '\n}\n')
    unmapped = json.loads((folder/'unmapped.json').read_text())
    removed_section_ids = set(re.findall(r'<Section\s+id="([^"]+)"', s[a:b]))
    for component_id, data in list((unmapped.get('components') or {}).items()):
        if component_id not in removed_section_ids:
            # Existing Wix Page/Header/Footer/global metadata are not part of
            # the deleted section set. Preserve verbatim.
            continue
        if not isinstance(data,dict) or set(data) != {'anchors'}:
            raise Blocked('Unknown unmapped data on removed Section: ' + component_id)
        del unmapped['components'][component_id]
    (folder/'unmapped.json').write_text(json.dumps(unmapped, indent=2))
    (folder/'structure.jsx').write_text(newjsx)
    (folder/'layout.css').write_text(newlayout)
    (folder/'style.css').write_text(sty)
    (Path(root).parent/(page+'-localdesign-transfer-manifest.json')).write_text(json.dumps({
        'source': recipe['source'], 'sha256': recipe['sha256'],
        'pageId': expected_id, 'items': originals
    }, indent=2))
    print(json.dumps({'status': 'WORKSPACE_ONLY_NO_IMPORT', 'pageId': expected_id,
                      'sections': len(sec_js), 'elements': len(ids),
                      'images': sum(e['type']=='image' for x in recipe['sections'] for e in x['elements'])}))


def finalize_media(root, page, allow_home=False):
    p = get_page(root, page, allow_home=allow_home) / 'structure.jsx'
    s = p.read_text()
    pat = r'(<Image\s[\s\S]*?\bimage=\{\{)([\s\S]*?)(\}\}\s*/>)'
    count = 0
    def replacement(match):
        nonlocal count
        body = match.group(2)
        def fld(key):
            m = re.search(r'\b'+re.escape(key)+r':\s*[\'"]([^\'"]+)[\'"]', body)
            if m:
                return m.group(1)
            m = re.search(r'\b'+re.escape(key)+r':\s*(\d+)', body)
            return m.group(1) if m else None
        uri, name, w, h = [fld(k) for k in ('uri', 'name', 'width', 'height')]
        if not uri or not re.fullmatch(r'[^:/\s]+\.(jpg|jpeg|gif|png|webp)', uri, re.I):
            raise Blocked('Original media not imported as Wix ID; run official upload-media')
        if not all((name, w, h)):
            raise Blocked('Missing official image metadata')
        if 'url:' in body:
            return match.group()
        url = f'wix:image://v1/{uri}/{name}#originWidth={w}&originHeight={h}'
        body += f'\n                        url: media.getCroppedImageUrl({url!r},0,0,0,0,{w},{h},{{name:{name!r},autoEncode:true,devicePixelRatio:1}}),\n'
        count += 1
        return match.group(1)+body+match.group(3)
    s = re.sub(pat, replacement, s)
    p.write_text(s)
    print(json.dumps({'status': 'MEDIA_NATIVE_FINALIZED_NO_IMPORT', 'images': count}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=('compile', 'finalize-media'))
    parser.add_argument('--recipe')
    parser.add_argument('--export', required=True)
    parser.add_argument('--page', required=True)
    parser.add_argument('--page-id')
    parser.add_argument('--allow-replace-page', action='store_true')
    parser.add_argument('--allow-home-target', action='store_true', help='Only for an explicitly approved existing Wix Home page')
    parser.add_argument('--video-media-manifest', help='JSON {files:[official READY Wix file descriptors]}')
    parser.add_argument('--vector-media-manifest', help='JSON {files:[sourceUrl, id, operationStatus READY, mediaType VECTOR]}')
    args = parser.parse_args()
    try:
        if args.action == 'compile':
            if not args.recipe or not args.page_id:
                raise Blocked('Require --recipe and --page-id')
            manifest = json.loads(Path(args.video_media_manifest).read_text()) if args.video_media_manifest else {}
            if manifest and (not isinstance(manifest,dict) or not isinstance(manifest.get('files'),list)):
                raise Blocked('Video media manifest must contain files[]')
            vector_manifest = json.loads(Path(args.vector_media_manifest).read_text()) if args.vector_media_manifest else {}
            if vector_manifest and (not isinstance(vector_manifest,dict) or not isinstance(vector_manifest.get('files'),list)):
                raise Blocked('Vector media manifest must contain files[]')
            compile_page(json.loads(Path(args.recipe).read_text()),
                         args.export, args.page, args.page_id, args.allow_replace_page,
                         manifest.get('files',[]), allow_home=args.allow_home_target,
                         vector_files=vector_manifest.get('files',[]))
        else:
            finalize_media(args.export, args.page, allow_home=args.allow_home_target)
    except (Blocked, KeyError, TypeError, ValueError) as e:
        parser.exit(2, 'BLOCKED: '+str(e)+'\n')


if __name__ == '__main__':
    main()
