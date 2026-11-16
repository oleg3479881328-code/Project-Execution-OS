#!/usr/bin/env python3
"""LocalDesign v2.4 full-page normalization for the EXISTING Wix native adapter.

No Wix credentials, browser controller, page mutation, source downloads or publishing.
This is a fail-closed, source-agnostic upstream Recipe stage, not a parallel Wix editor.
"""
import argparse
import hashlib
import json
import re
import zipfile
from pathlib import Path

SCHEMA = 'localdesign.wix-page-recipe.v1'
CAPTURE = 'localdesign.site-fingerprint.v2.4'
TEXT_TAGS = {'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'span', 'a', 'button', 'label', 'li'}


class Blocked(ValueError):
    pass


def rect(node):
    r = node.get('rect') or {}
    try:
        return {k: float(r[k]) for k in ('x', 'y', 'width', 'height')}
    except (TypeError, ValueError, KeyError) as e:
        raise Blocked(f'Invalid rectangle for {node.get("selector")}: {e}')


def normalize_float(value):
    return round(float(value), 3)


def read_zip(file):
    with zipfile.ZipFile(file) as z:
        if 'site-fingerprint.json' not in z.namelist():
            raise Blocked('Missing site-fingerprint.json')
        fingerprint = json.loads(z.read('site-fingerprint.json'))
        if 'wix-origami/origami-source-contract.json' in z.namelist():
            contract = json.loads(z.read('wix-origami/origami-source-contract.json'))
            if contract.get('schema') != 'localdesign.origami-source-contract.v1':
                raise Blocked('Unsupported Origami source contract')
            fingerprint['_origamiSourceContract'] = contract
    if fingerprint.get('schema') != CAPTURE:
        raise Blocked('Expected ' + CAPTURE)
    pages = fingerprint.get('pages', [])
    if len(pages) != 1:
        raise Blocked('Exactly one source page required per recipe')
    views = pages[0].get('views', {})
    desktop_keys = [key for key in ('desktop-1280', 'desktop-1920') if key in views]
    if len(desktop_keys) != 1:
        raise Blocked('Require exactly one supported observed desktop view: desktop-1280 or desktop-1920')
    for required in (desktop_keys[0], 'mobile-390'):
        v = views.get(required)
        if not v or v.get('status') != 'observed' or v.get('data', {}).get('truncated'):
            raise Blocked('Missing complete observed ' + required)
        if not v['data'].get('nodes'):
            raise Blocked('Empty DOM capture at ' + required)
    return fingerprint, views


def visible(n):
    if not n or not n.get('visible'):
        return False
    r = rect(n)
    return r['width'] > .1 and r['height'] > .1


def direct_sections(views, requested, origami_contract=None):
    """Conservatively detect broad top-level DOM sections, including mobile-only menu.
    An ambiguous layout must provide explicit source selector order, never guesses.
    """
    desktop = views[next(key for key in ('desktop-1280', 'desktop-1920') if key in views)]['data']
    nodes = desktop['nodes']
    by_selector = {n['selector']: n for n in nodes}
    if len(by_selector) != len(nodes):
        raise Blocked('Duplicate source selectors in desktop capture')
    if requested:
        missing = [s for s in requested if s not in by_selector]
        if missing:
            raise Blocked('Section selectors absent: ' + ', '.join(missing))
        return requested
    vw = float(desktop['viewport']['width'])
    raw = []
    # Prefer source scanner's explicit native-ready section candidates, but
    # validate every selector against the actual observed DOM. It is a hint,
    # never a target import instruction.
    if origami_contract:
        pages = origami_contract.get('pages', [])
        if len(pages) != 1:
            raise Blocked('Origami source contract must describe exactly one page')
        origin = pages[0].get('byViewport', {}).get('desktop-'+str(int(vw)), {})
        suggested = origin.get('sectionCandidates', [])
        names = [x.get('sourceSelector') for x in suggested]
        if len(names) != len(set(names)) or any(not isinstance(x, str) or x not in by_selector for x in names):
            raise Blocked('Origami source section candidates do not match measured DOM')
        if len(names) >= 2:
            # Mobile-only menu, where measured, is a separate responsive layer.
            mobile_names = [x.get('sourceSelector') for x in
                pages[0].get('byViewport', {}).get('mobile-390', {}).get('sectionCandidates', [])
                if x.get('sourceSelector') not in names]
            mobile_nodes = {n['selector']: n for n in views['mobile-390']['data']['nodes']}
            mobile_names = [x for x in mobile_names if x in by_selector and x in mobile_nodes
                and visible(mobile_nodes[x]) and not visible(by_selector[x])
                and rect(mobile_nodes[x])['y'] <= 1.0]
            return mobile_names + names
    for n in nodes:
        sel = n.get('selector', '')
        if not re.fullmatch(r'(div|section|header|footer|main)#[A-Za-z0-9_-]+', sel):
            continue
        if not n.get('visible') or n.get('styles', {}).get('position') == 'fixed':
            continue
        r = rect(n)
        if r['width'] < vw * .70 or r['height'] < .75:
            continue
        raw.append((sel, r))
    # Reject same-frame nested background / painted view layers as sections.
    # They remain available to painted_background() and source-layer checks.
    candidates = {name: bounds for name, bounds in raw}
    def nested_same_frame(name, bounds):
        node = by_selector[name]
        parent = (node.get('relations') or {}).get('parentSelector')
        visited = set()
        while parent and parent not in visited:
            visited.add(parent)
            if parent in candidates:
                outer = candidates[parent]
                if all(abs(bounds[k]-outer[k]) <= 2 for k in ('x','y','width','height')):
                    return True
            parent = (by_selector.get(parent, {}).get('relations') or {}).get('parentSelector')
        return False
    raw = [(name,bounds) for name,bounds in raw if not nested_same_frame(name,bounds)]
    raw.sort(key=lambda p: (p[1]['y'], -p[1]['width'], p[0]))
    tall = max((r['height'] for _, r in raw), default=0)
    filtered = [(s, r) for s, r in raw if r['height'] <= tall * .8]
    if not filtered:
        raise Blocked('No source sections. Supply --sections file')
    selected = []
    end = None
    for sel, r in filtered:
        y, bottom = r['y'], r['y'] + r['height']
        if end is None or y >= end - 1.0:
            selected.append((sel, r))
            end = bottom
        elif abs(y - selected[-1][1]['y']) <= 1.0:
            raise Blocked('Ambiguous overlapping section candidates; supply --sections')
    if not selected:
        raise Blocked('Section detection failed')
    mv = views['mobile-390']['data']
    for node in reversed(mv['nodes']):
        selector = node.get('selector', '')
        if selector not in by_selector or not re.fullmatch(r'(div|section|header|footer|main)#[A-Za-z0-9_-]+', selector):
            continue
        if not visible(node) or visible(by_selector[selector]):
            continue
        r = rect(node)
        if r['width'] >= float(mv['viewport']['width']) * .7 and r['height'] >= 1 and r['y'] <= 1 and r['height'] <= 300:
            selected.insert(0, (selector, r))
    return [s for s, _ in selected]


def is_descendant(selector, parent):
    return selector.startswith(parent + ' > ')


def painted_background(section, all_nodes):
    """Preserve computed covering descendants, not just transparent outer section."""
    sr = rect(section)
    potential = []
    for n in all_nodes:
        if n is not section and not is_descendant(n['selector'], section['selector']):
            continue
        if not visible(n):
            continue
        color = n.get('styles', {}).get('backgroundColor')
        image = n.get('styles', {}).get('backgroundImage', 'none')
        if (not color or color in ('transparent', 'rgba(0, 0, 0, 0)')) and image in ('none', None):
            continue
        r = rect(n)
        if abs(r['x'] - sr['x']) <= 2 and abs(r['y'] - sr['y']) <= 2 and r['width'] >= sr['width'] - 2 and r['height'] >= sr['height'] - 2:
            potential.append({'selector': n['selector'], 'color': color, 'image': image,
                              'position': n.get('styles', {}).get('backgroundPosition'),
                              'size': n.get('styles', {}).get('backgroundSize')})
    values = {(x['color'], x['image']) for x in potential}
    return {'status': 'AMBIGUOUS' if len(values) > 1 else 'OBSERVED' if potential else 'NOT_OBSERVED',
            'candidates': potential}


def capture_geometry(node, sec, desktop):
    if not visible(node):
        return None
    r, s = rect(node), rect(sec)
    base = {'y': normalize_float(r['y'] - s['y']),
            'w': normalize_float(r['width']), 'h': normalize_float(r['height'])}
    if desktop:
        base['centerX'] = normalize_float(r['x'] - s['x'] - s['width'] / 2)
    else:
        base['x'] = normalize_float(r['x'] - s['x'])
    return base


def normalize(fp, views, section_selectors):
    selectors = direct_sections(views, section_selectors, fp.get('_origamiSourceContract'))
    desktop_key = next(key for key in ('desktop-1280', 'desktop-1920') if key in views)
    dn = views[desktop_key]['data']['nodes']
    mn = views['mobile-390']['data']['nodes']
    dmap = {x['selector']: x for x in dn}
    mmap = {x['selector']: x for x in mn}
    source = fp['source']
    if not (source.startswith('https://') or source.startswith('http://')):
        raise Blocked('Invalid source URL')
    out, unsupported = [], []
    # Visually attached layers can live under a separate DOM id; e.g. footer_0.
    section_set = set(selectors)
    attached = {s: [] for s in selectors}
    for root in dn:
        name = root.get('selector', '')
        if name in section_set or not re.fullmatch(r'(div|section)#[A-Za-z0-9_-]+', name):
            continue
        if not visible(root) or root.get('styles', {}).get('position') == 'fixed':
            continue
        rr = rect(root)
        hosts = []
        for secname in selectors:
            section_node = dmap.get(secname)
            if not visible(section_node):
                continue
            sr = rect(section_node)
            if (sr['x']-2 <= rr['x'] <= sr['x']+sr['width'] and
                sr['y']-2 <= rr['y'] < sr['y']+sr['height'] and
                rr['width'] <= sr['width']+2 and rr['height'] > 5 and
                any(is_descendant(n['selector'], name) and n.get('assets') for n in dn)):
                hosts.append(secname)
        if len(hosts) == 1:
            attached[hosts[0]].append(name)
        elif len(hosts) > 1:
            unsupported.append({'selector': name, 'reason': 'ambiguous detached visual layer ownership', 'hosts': hosts})
    for sel in selectors:
        sd, sm = dmap.get(sel), mmap.get(sel)
        if not sd or not sm or (not visible(sd) and not visible(sm)):
            raise Blocked('Section absent from both breakpoints: ' + sel)
        roots = [sel] + attached[sel]
        descendants = [n for n in dn if any(is_descendant(n['selector'], parent) for parent in roots)]
        mobile_only = [n for n in mn if any(is_descendant(n['selector'], parent) for parent in roots) and n['selector'] not in dmap]
        candidate = {n['selector']: n for n in descendants + mobile_only}
        elements = []
        for name, n in candidate.items():
            d, m = dmap.get(name), mmap.get(name)
            if not visible(d) and not visible(m):
                continue
            src = d if visible(d) else m
            # Native video is a dynamic background/foreground layer, never a
            # static Wix Image or a zero-size <source> component.
            if src.get('tag') == 'video':
                continue
            desktop_assets = list(dict.fromkeys((d or {}).get('assets', [])))
            mobile_assets = list(dict.fromkeys((m or {}).get('assets', [])))
            assets = list(dict.fromkeys(desktop_assets + mobile_assets))
            children = [x for x in candidate if is_descendant(x, name) and ((dmap.get(x) or mmap.get(x) or {}).get('text') or '').strip()]
            text = (src.get('text') or '').strip()
            typ = 'text' if src.get('tag') in TEXT_TAGS and text and not children else 'image' if assets else None
            if typ is None:
                continue
            asset = None
            if typ == 'image':
                if len(assets) > 1:
                    # Same Showit media identity may have observed size-qualified URLs
                    # such as /1600/HASH/shared/name.jpg and /800/HASH/shared/name.jpg.
                    # Only collapse a proven same stable source identity; retain exact
                    # observed URLs separately for media provenance and visual QA.
                    from urllib.parse import urlsplit
                    def source_identity(url):
                        p = urlsplit(url)
                        return (p.scheme, p.netloc, re.sub(r'^/[0-9]+/', '/', p.path), p.query)
                    if len(desktop_assets) != 1 or len(mobile_assets) != 1 or len(assets) != 2 or source_identity(assets[0]) != source_identity(assets[1]):
                        unsupported.append({'selector': name, 'reason': 'multiple source asset URLs (unmatched)', 'assets': assets})
                        continue
                asset = desktop_assets[0] if desktop_assets else assets[0]
                if not (asset.startswith('https://') or asset.startswith('http://')):
                    unsupported.append({'selector': name, 'reason': 'source asset URL not HTTP(S)'})
                    continue
            keys = ('fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight',
                    'letterSpacing', 'textAlign', 'color', 'textTransform', 'opacity',
                    'objectFit', 'objectPosition', 'zIndex', 'position', 'transform')
            elements.append({'sourceSelector': name, 'type': typ, 'tag': src.get('tag'),
                             'text': text if typ == 'text' else None, 'asset': asset,
                             'mobileAsset': mobile_assets[0] if typ == 'image' and len(mobile_assets) == 1 else None,
                             'assetVariants': assets if typ == 'image' else [],
                             'desktop': capture_geometry(d, sd, True),
                             'mobile': capture_geometry(m, sm, False),
                             'desktopStyle': {k: d['styles'].get(k) for k in keys if d and k in d['styles']},
                             'mobileStyle': {k: m['styles'].get(k) for k in keys if m and k in m['styles']}})
        # Recover the original MP4 from a visible <video>, including old v2.5
        # captures where its only URL sits in a 0x0 child <source>.
        video_selectors = [name for name in candidate
                           if ((dmap.get(name) or mmap.get(name) or {}).get('tag') == 'video')
                           and (visible(dmap.get(name)) or visible(mmap.get(name)))]
        dynamic = []
        for name in video_selectors:
            def observed_video(node, nodes, section):
                if not visible(node):
                    return None, None
                evidence = node.get('videoEvidence') or {}
                found = [evidence.get('sourceUrl')] if evidence.get('sourceUrl') else []
                found += [a for a in node.get('assets', []) if a.endswith(('.mp4','.webm'))]
                found += [a for child in nodes
                          if is_descendant(child['selector'], name)
                          and child.get('tag') == 'source'
                          for a in child.get('assets', []) if a.endswith(('.mp4','.webm'))]
                urls = list(dict.fromkeys(found))
                if len(urls) != 1:
                    raise Blocked('Video has zero/multiple distinct sources: '+name)
                style = node.get('styles') or {}
                old_evidence = node.get('imageEvidence') or {}
                layer = node.get('layerEvidence') or {}
                opacity = float(layer.get('parentOpacity') or style.get('opacity') or 1)
                if not 0 <= opacity <= 1:
                    raise Blocked('Invalid video opacity for '+name)
                nr, sr = rect(node), rect(section)
                state = {'rect': {'x':normalize_float(nr['x']-sr['x']),
                    'y':normalize_float(nr['y']-sr['y']),
                    'w':normalize_float(nr['width']), 'h':normalize_float(nr['height'])},
                    'opacity':opacity,
                    'objectFit':evidence.get('objectFit') or style.get('objectFit'),
                    'autoplay':bool(evidence.get('autoplay',old_evidence.get('autoplay'))),
                    'loop':bool(evidence.get('loop',old_evidence.get('loop'))),
                    'muted':bool(evidence.get('muted',old_evidence.get('muted')))}
                return urls[0], state
            url_d, state_d = observed_video(dmap.get(name), dn, sd)
            url_m, state_m = observed_video(mmap.get(name), mn, sm)
            if url_d and url_m and url_d != url_m:
                raise Blocked('Responsive video asset identity differs for '+name)
            dynamic.append({'type':'video','sourceUrl':url_d or url_m,
                            'desktop':state_d,'mobile':state_m,
                            'provenance':'LOCALDESIGN_CAPTURED_VIDEO_SOURCE'})
        if len(dynamic) > 1:
            unsupported.append({'selector':sel,'reason':'multiple dynamic videos in section not proven native'})
        out.append({'sourceSelector': sel, 'desktopSection': rect(sd), 'mobileSection': rect(sm),
                    'attachedVisualLayers': attached[sel],
                    'desktopBackground': painted_background(sd, dn),
                    'mobileBackground': painted_background(sm, mn),
                    'elements': elements, 'dynamicLayers':dynamic})
    viewsinfo = {k: {'viewport': v['data'].get('viewport'), 'capturedAt': v['data'].get('capturedAt'),
                     'nodeCount': len(v['data']['nodes'])} for k,v in views.items() if v.get('status') == 'observed'}
    result = {'schema': SCHEMA, 'source': source, 'sourceSchema': CAPTURE,
              'desktopWidth': int(views[desktop_key]['data']['viewport']['width']),
              'viewports': viewsinfo, 'sections': out, 'unsupported': unsupported,
              'acceptance': 'RECIPE_ONLY_NOT_WIX_IMPORTED'}
    canonical = json.dumps(result, sort_keys=True, ensure_ascii=False, separators=(',', ':'))
    result['sha256'] = hashlib.sha256(canonical.encode()).hexdigest()
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fingerprint', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--sections', help='Optional JSON array of exact source section selectors, in order')
    args = parser.parse_args(argv)
    try:
        fp, views = read_zip(args.fingerprint)
        wanted = json.loads(Path(args.sections).read_text()) if args.sections else None
        if wanted is not None and (not isinstance(wanted, list) or not all(isinstance(s, str) for s in wanted)):
            raise Blocked('--sections must be JSON array of selector strings')
        recipe = normalize(fp, views, wanted)
        Path(args.out).write_text(json.dumps(recipe, indent=2, ensure_ascii=False))
        print(json.dumps({'schema': recipe['schema'], 'sections': len(recipe['sections']),
                          'elements': sum(len(s['elements']) for s in recipe['sections']),
                          'unsupported': len(recipe['unsupported']), 'output': args.out}))
    except (Blocked, ValueError, KeyError, zipfile.BadZipFile) as e:
        parser.exit(2, 'BLOCKED: ' + str(e) + '\n')


if __name__ == '__main__':
    main()
