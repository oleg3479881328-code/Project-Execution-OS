#!/usr/bin/env python3
"""Apply owner-approved native Wix theme defaults AFTER existing PEOS compile.

Not a renderer: the existing compile_full_page.py owns all native element
creation, geometry and media. This pass changes ONLY text font-family in the
generated target page's style.css and records source effects ignored by the
native baseline. Never mutates globals, images, sections or coordinates.
"""
import argparse
import json
import re
from pathlib import Path
from full_page_recipe import read_zip

SCHEMA = 'localdesign.wix-page-recipe.v1'


class NativeDefaultsBlocked(ValueError):
    pass


def family_key(value):
    return str(value).split(',')[0].strip().strip("\"'").lower()


def wix_theme_fonts(theme_css):
    """Native fonts explicitly configured in current Wix theme; no inference."""
    result = {}
    for name, shorthand in re.findall(
        r'--wst-(heading-[1-6]|paragraph-[1-3])-font\s*:\s*([^;]+);',
        theme_css
    ):
        # Wix theme standard shorthand: weight, font-size/line-height, family
        match = re.search(r'/[^\s]+\s+(.+)$', shorthand.strip())
        if not match:
            continue
        family = match.group(1).strip().strip("\"'")
        if re.fullmatch(r"[A-Za-z0-9 _-]+", family):
            result[name] = family
    return result


def default_theme_font(tag, fonts):
    token = ('heading-' + tag[1]) if re.fullmatch(r'h[1-6]', str(tag)) else 'paragraph-1'
    return fonts.get(token)


def measured_effects(node):
    style = node.get('styles') or {}
    effects = []
    for key in ('animationName', 'transform', 'filter', 'clipPath',
                'mixBlendMode', 'boxShadow'):
        value = style.get(key)
        if value and str(value).strip().lower() not in (
            'none', 'normal', 'initial', 'inherit', 'unset',
            'matrix(1, 0, 0, 1, 0, 0)', 'rgba(0, 0, 0, 0)'
        ):
            effects.append({'property': key, 'sourceValue': str(value)})
    return effects


def apply_native_defaults(recipe, fingerprint_zip, export_root, page, allow_partial_draft=False):
    if recipe.get('schema') != SCHEMA or not recipe.get('sections'):
        raise NativeDefaultsBlocked('Complete native recipe required')
    if page == 'home' or not re.fullmatch(r'[a-z0-9-]+|\(home\)', page):
        raise NativeDefaultsBlocked('Invalid exact Wix target page folder')
    root = Path(export_root)
    pagefolder = root / 'packages/site-app/src/pages' / page
    stylefile = pagefolder / 'style.css'
    structurefile = pagefolder / 'structure.jsx'
    themefile = root / 'packages/site-app/src/global/themes/theme.css'
    if not all(f.is_file() for f in (stylefile, structurefile, themefile)):
        raise NativeDefaultsBlocked('Missing official Wix native target page/theme export')
    css = stylefile.read_text()
    structure = structurefile.read_text()
    theme_fonts = wix_theme_fonts(themefile.read_text())
    # Default can inherit Wix native RichText family if the site has no
    # supported Theme font tokens. This is not a hard blocker.
    available = set(map(family_key, theme_fonts.values()))
    fp, views = read_zip(fingerprint_zip)  # Existing source parser; no rescan
    if recipe.get('source') != fp.get('source'):
        raise NativeDefaultsBlocked('Recipe/fingerprint source mismatch')
    desktop = 'desktop-' + str(recipe.get('desktopWidth'))
    if desktop not in views:
        raise NativeDefaultsBlocked('Source desktop viewport mismatch')
    byview = {
        view: {node['selector']: node for node in views[view]['data']['nodes']}
        for view in (desktop, 'mobile-390')
    }
    entries = []
    text_count = 0
    for si, section in enumerate(recipe['sections']):
        for ei, elem in enumerate(section['elements']):
            cid = f'ldv-e{si:03d}-{ei:03d}'
            if elem['type'] == 'text':
                text_count += 1
                if not re.search(r'<WRichText\b[^>]*\bid="' + re.escape(cid) + r'"', structure):
                    raise NativeDefaultsBlocked('Text target ID missing: '+cid)
                rule = re.compile(r'(?P<start>^\s*\.' + re.escape(cid)
                     + r'\s*\{)(?P<body>[^{}]*)(?P<end>\})', re.M)
                matches = list(rule.finditer(css))
                required = [
                    (desktop, elem.get('desktopStyle') or {}),
                    ('mobile-390', elem.get('mobileStyle') or {}),
                ]
                expected = sum(bool(st and st.get('fontFamily')) for _,st in required)
                source_has_style = [
                    (view,st) for view,st in required if st and st.get('fontFamily')
                ]
                if expected and len(matches) != expected:
                    raise NativeDefaultsBlocked('Observed text CSS rule count mismatch: '+cid)
                for (view,st), match in zip(source_has_style, matches):
                    original = str(st['fontFamily'])
                    declared = re.search(r'(?<![-\w])font-family\s*:\s*([^;]+)', match.group('body'))
                    if not declared or family_key(declared.group(1)) != family_key(original):
                        raise NativeDefaultsBlocked('Original font provenance mismatch: '+cid+' '+view)
                # Update from right to left to preserve match offsets.
                for (view,st), match in reversed(list(zip(source_has_style, matches))):
                    original = str(st['fontFamily'])
                    if family_key(original) in available:
                        continue
                    native_font = default_theme_font(elem.get('tag'), theme_fonts)
                    body = match.group('body')
                    if native_font:
                        body = re.sub(r'(?<![-\w])font-family\s*:\s*([^;]+)',
                                      lambda _: 'font-family:' + native_font, body, count=1)
                    else:
                        body = re.sub(r'(?<![-\w])font-family\s*:\s*[^;]+;\s*', '', body, count=1)
                    css = css[:match.start('body')] + body + css[match.end('body'):]
                    entries.append({
                        'sourceSelector': elem['sourceSelector'],
                        'nativeId': cid, 'viewport': view,
                        'component': 'WRichText',
                        'status': 'NATIVE_WIX_DEFAULT',
                        'reason': 'ORIGINAL_FONT_NOT_IN_WIX_SITE_THEME',
                        'original': original,
                        'nativeFont': native_font,
                    })
            for view in (desktop, 'mobile-390'):
                node = byview[view].get(elem['sourceSelector'])
                if not node:
                    continue
                for effect in measured_effects(node):
                    entries.append({
                        'sourceSelector': elem['sourceSelector'],
                        'nativeId': cid, 'viewport': view,
                        'component': 'WRichText' if elem['type']=='text' else 'Image',
                        'status': 'NATIVE_WIX_DEFAULT',
                        'reason': 'UNSUPPORTED_VISUAL_EFFECT_NATIVE_STATIC',
                        'original': effect, 'nativeBehavior': 'WIX_STATIC_DEFAULT',
                    })
    # This optional experimental mode never claims that an omitted source
    # object was built by Wix. The exact original unsupported ledger travels
    # with the editable native draft for manual follow-up.
    source_unmapped=list(recipe.get('unsupported') or [])
    if source_unmapped and not allow_partial_draft:
        raise NativeDefaultsBlocked(
            'Mandatory source-native mappings still unresolved; '
            'pass --allow-partial-native-draft only for an explicitly '
            'authorized experimental partial build')
    stylefile.write_text(css)
    report = {
        'schema': 'peos.wix-native-defaults.v1',
        'source': recipe['source'], 'page': page,
        'textElementsInspected': text_count,
        'nativeDefaults': entries,
        'nativeDefaultCount': len(entries),
        'nativeBuildStatus': ('DRAFT_WITH_UNMAPPED_SOURCE' if source_unmapped else
                              'PASS_WITH_WIX_DEFAULTS' if entries else
                              'NO_DEFAULTS_REQUIRED'),
        'sourceVisualParity': 'PARTIAL' if entries or source_unmapped else 'NOT_ASSESSED',
        'remainingMandatoryBlockers': len(source_unmapped),
        'sourceUnmapped': source_unmapped,
        'sourceObjectCoverage': recipe.get('sourceObjectCoverage'),
        'manualRefinementRequired': bool(entries or source_unmapped),
        'policy': 'Exact native geometry/media preserved; unmapped source not claimed built',
    }
    outfile = root.parent / (page.replace('(', '').replace(')', '') +
                              '-wix-native-defaults-report.json')
    outfile.write_text(json.dumps(report, indent=2, ensure_ascii=False))
    return report


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--recipe',required=True)
    p.add_argument('--fingerprint',required=True)
    p.add_argument('--export',required=True)
    p.add_argument('--page',required=True)
    p.add_argument('--out')
    p.add_argument('--allow-partial-native-draft', action='store_true',
                   help='Authorized experimental import only; all unmapped source objects remain in report')
    args=p.parse_args()
    result=apply_native_defaults(
        json.loads(Path(args.recipe).read_text()),
        args.fingerprint, args.export, args.page,
        allow_partial_draft=args.allow_partial_native_draft)
    if args.out:
        Path(args.out).write_text(json.dumps(result,indent=2,ensure_ascii=False))
    print(json.dumps({
        'nativeDefaults': result['nativeDefaultCount'],
        'nativeBuildStatus':result['nativeBuildStatus'],
        'sourceVisualParity':result['sourceVisualParity'],
        'remainingMandatoryBlockers':result['remainingMandatoryBlockers'],
    }))


if __name__=='__main__':
    main()
