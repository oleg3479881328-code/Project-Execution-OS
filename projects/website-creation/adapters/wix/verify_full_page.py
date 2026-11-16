#!/usr/bin/env python3
"""Readback audit: LocalDesign full-page recipe vs fresh official Wix Origami export.

Strict source COVERAGE + static native geometry/paint contract, independent
Desktop 1280 and Mobile 390. Does NOT replace browser/visual QA.
"""
import argparse
import html
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Blocked(ValueError):
    pass


def n(v):
    return round(float(v), 3)


def rule(css, ident):
    m = re.search(r'(?m)^\s*\.'+re.escape(ident)+r'\s*\{([^{}]*)\}', css)
    return {k.strip(): v.strip() for k,v in re.findall(r'([\w-]+)\s*:\s*([^;}\n]+)', m.group(1))} if m else None


def px(v):
    if v is None:
        return None
    m = re.fullmatch(r'(-?\d+(?:\.\d+)?)px', v)
    return n(m.group(1)) if m else None


def block_elements(section):
    found = []
    for m in re.finditer(r'<(Image|WRichText)\b([\s\S]*?)/>', section):
        head = m.group(2)
        idm = re.search(r'\bid="([^"]+)"', head)
        if not idm:
            raise Blocked('Native element without ID')
        if m.group(1) == 'Image':
            asset = re.search(r'\bname:\s*[\'"]([^\'"]+)[\'"]', head)
            kind = 'image'
            body = asset.group(1) if asset else ''
            if not re.search(r'\buri:\s*[\'"][^:/\s]+\.(?:jpg|jpeg|gif|png|webp)[\'"]', head, re.I):
                raise Blocked('Native image lacks Wix Media ID: '+idm.group(1))
        else:
            val = re.search(r'\bhtml:\s*([\'"])(.*?)\1', head, re.S)
            kind = 'text'
            body = html.unescape(re.sub(r'<[^>]+>', '', val.group(2))).strip() if val else ''
        found.append({'kind': kind, 'id': idm.group(1), 'payload': body})
    return found


def verify(recipe, export, page):
    if recipe.get('schema') != 'localdesign.wix-page-recipe.v1':
        raise Blocked('Wrong source recipe schema')
    if recipe.get('unsupported'):
        raise Blocked('Unmapped source feature(s) exist')
    folder = Path(export)/'packages/site-app/src/pages'/page
    structure = (folder/'structure.jsx').read_text()
    layout = (folder/'layout.css').read_text()
    style = (folder/'style.css').read_text()
    desktop_width = recipe.get('desktopWidth', 1280)
    if desktop_width not in (1280, 1920):
        raise Blocked('Unsupported source desktopWidth: '+str(desktop_width))
    media = re.search(r'@media\s*\(--variants-[^)]+\)\s*\{', layout)
    if not media:
        raise Blocked('Readback Wix mobile breakpoint missing')
    desktop, mobile = layout[:media.start()], layout[media.end():]
    actual = list(re.finditer(r'<Section\s+id="([^"]+)"[\s\S]*?</Section>', structure))
    issues = []
    matched = images = texts = 0
    def err(msg):
        issues.append(msg)
    def near(have, want, desc):
        if have is None or abs(have-n(want)) > .02:
            err(f'{desc}: expected {want} got {have}')
    if len(actual) != len(recipe['sections']):
        err(f'Sections: expected {len(recipe["sections"])} got {len(actual)}')
    for si, src in enumerate(recipe['sections']):
        if si >= len(actual):
            break
        sid = actual[si].group(1)
        section = actual[si].group()
        # Dynamic layers are explicitly normalized separately from the
        # geometrically fixed Image/WRichText children.
        dynamic = src.get('dynamicLayers') or []
        if dynamic:
            if len(dynamic) != 1 or dynamic[0].get('type') != 'video':
                err(f'{sid}: unsupported native dynamic layer count/type')
            else:
                bg = re.search(r'<Background\s+id="([^"]+)"([^>]*)/>', section)
                if not bg or 'videoMedia=' not in bg.group(2):
                    err(f'{sid}: missing native Background.videoMedia')
                else:
                    name = unquote(urlsplit(dynamic[0]['sourceUrl']).path.rsplit('/',1)[-1])
                    if name not in bg.group(2) or 'wix:video://v1/' not in bg.group(2):
                        err(f'{sid}: native video Wix Media source name/id mismatch')
                    for bp, media_opacity in ((desktop_width, dynamic[0].get('desktop')), (390, dynamic[0].get('mobile'))):
                        expected_opacity = float(media_opacity['opacity']) if media_opacity else 0.0
                        selector = bg.group(1)
                        matches = re.findall(r'\.'+re.escape(selector)+r'\s*\{[^{}]*--backgroundMediaOpacity:\s*(\d+(?:\.\d+)?)',style)
                        if not any(abs(float(got)-expected_opacity)<.002 for got in matches):
                            err(f'{sid}: missing saved {bp} native video opacity {expected_opacity}')
        components = block_elements(section)
        expected = src['elements']
        if len(components) != len(expected):
            err(f'{src["sourceSelector"]}: expected {len(expected)} elements got {len(components)}')
        for bp, css in ((desktop_width, desktop), (390, mobile)):
            sr = rule(css, sid)
            if not sr:
                err(f'{sid}: missing section CSS {bp}')
                continue
            near(px(sr.get('height')), src['desktopSection' if bp != 390 else 'mobileSection']['height'],
                 f'{sid} section height {bp}')
        for ei, e in enumerate(expected):
            if ei >= len(components):
                continue
            comp = components[ei]
            if comp['kind'] != e['type']:
                err(f'{sid} element {ei} kind mismatch')
                continue
            if comp['kind'] == 'image':
                want = unquote(urlsplit(e['asset']).path.rsplit('/', 1)[-1])
                if comp['payload'].lower() != want.lower():
                    err(f'{sid} element {ei} original media name mismatch {want}/{comp["payload"]}')
                images += 1
            else:
                source_text = re.sub(r'\s+', ' ', e.get('text') or '').strip()
                target_text = re.sub(r'\s+', ' ', comp['payload']).strip()
                if source_text != target_text:
                    err(f'{sid} element {ei} text differs')
                texts += 1
            for bp, css, key in ((desktop_width, desktop, 'desktop'), (390, mobile, 'mobile')):
                gr = e.get(key)
                r = rule(css, comp['id'])
                if not r:
                    err(f'{comp["id"]}: missing CSS for {bp}')
                    continue
                if gr is None:
                    if r.get('visibility') != 'hidden':
                        err(f'{comp["id"]}: expected hidden at {bp}')
                    continue
                for k,dst in (('w','width'),('h','height'),('y','margin-top')):
                    near(px(r.get(dst)), gr[k], f'{comp["id"]} {k} {bp}')
                if bp == 390:
                    near(px(r.get('margin-left')), gr['x'], f'{comp["id"]} mobile x')
                else:
                    m = re.fullmatch(r'calc\(50% ([+-]) (\d+(?:\.\d+)?)px\)', r.get('margin-left', ''))
                    if not m:
                        err(f'{comp["id"]}: missing centered offset')
                    else:
                        near(float(m.group(2))*(1 if m.group(1)=='+' else -1),
                             gr['centerX'], f'{comp["id"]} offsetX')
            matched += 1
    return {'status': 'READBACK_CSS_PASS' if not issues else 'READBACK_CSS_FAIL',
            'sourceSections': len(recipe['sections']), 'readbackSections': len(actual),
            'sourceElements': sum(len(s['elements']) for s in recipe['sections']),
            'matchedElements': matched, 'nativeImages': images, 'nativeTexts': texts,
            'issues': issues, 'browserQA': 'NOT_RUN', 'visualQA': 'NOT_RUN', 'published': False}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--recipe', required=True)
    parser.add_argument('--readback', required=True)
    parser.add_argument('--page', required=True)
    parser.add_argument('--out')
    args = parser.parse_args()
    try:
        data = verify(json.load(open(args.recipe)), args.readback, args.page)
        if args.out:
            Path(args.out).write_text(json.dumps(data, indent=2))
        print(json.dumps(data, indent=2))
        if data['status'] != 'READBACK_CSS_PASS':
            raise SystemExit(1)
    except (Blocked, OSError, ValueError, KeyError) as e:
        parser.exit(2, 'BLOCKED: '+str(e)+'\n')


if __name__ == '__main__':
    main()
