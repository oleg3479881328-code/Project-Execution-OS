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
    if fingerprint.get('schema') != CAPTURE:
        raise Blocked('Expected ' + CAPTURE)
    pages = fingerprint.get('pages', [])
    if len(pages) != 1:
        raise Blocked('Exactly one source page required per recipe')
    views = pages[0].get('views', {})
    for required in ('desktop-1280', 'mobile-390'):
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


def direct_sections(views, requested):
    """Conservatively detect broad top-level DOM sections, including mobile-only menu.
    An ambiguous layout must provide explicit source selector order, never guesses.
    """
    desktop = views['desktop-1280']['data']
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
    selectors = direct_sections(views, section_selectors)
    dn = views['desktop-1280']['data']['nodes']
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
            assets = list(dict.fromkeys((d or {}).get('assets', []) + (m or {}).get('assets', [])))
            children = [x for x in candidate if is_descendant(x, name) and ((dmap.get(x) or mmap.get(x) or {}).get('text') or '').strip()]
            text = (src.get('text') or '').strip()
            typ = 'text' if src.get('tag') in TEXT_TAGS and text and not children else 'image' if assets else None
            if typ is None:
                continue
            asset = None
            if typ == 'image':
                if len(assets) > 1:
                    unsupported.append({'selector': name, 'reason': 'multiple source asset URLs', 'assets': assets})
                    continue
                asset = assets[0]
                if not (asset.startswith('https://') or asset.startswith('http://')):
                    unsupported.append({'selector': name, 'reason': 'source asset URL not HTTP(S)'})
                    continue
            keys = ('fontFamily', 'fontSize', 'fontWeight', 'fontStyle', 'lineHeight',
                    'letterSpacing', 'textAlign', 'color', 'textTransform', 'opacity',
                    'objectFit', 'objectPosition', 'zIndex', 'position', 'transform')
            elements.append({'sourceSelector': name, 'type': typ, 'tag': src.get('tag'),
                             'text': text if typ == 'text' else None, 'asset': asset,
                             'desktop': capture_geometry(d, sd, True),
                             'mobile': capture_geometry(m, sm, False),
                             'desktopStyle': {k: d['styles'].get(k) for k in keys if d and k in d['styles']},
                             'mobileStyle': {k: m['styles'].get(k) for k in keys if m and k in m['styles']}})
        out.append({'sourceSelector': sel, 'desktopSection': rect(sd), 'mobileSection': rect(sm),
                    'attachedVisualLayers': attached[sel],
                    'desktopBackground': painted_background(sd, dn),
                    'mobileBackground': painted_background(sm, mn),
                    'elements': elements})
    viewsinfo = {k: {'viewport': v['data'].get('viewport'), 'capturedAt': v['data'].get('capturedAt'),
                     'nodeCount': len(v['data']['nodes'])} for k,v in views.items() if v.get('status') == 'observed'}
    result = {'schema': SCHEMA, 'source': source, 'sourceSchema': CAPTURE,
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
