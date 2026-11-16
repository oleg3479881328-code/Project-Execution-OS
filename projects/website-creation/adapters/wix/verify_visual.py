#!/usr/bin/env python3
"""Pixel visual gate for existing LocalDesign -> native Wix Studio Two pipeline.

Uses Pillow (existing mature image toolkit); does not fake visual acceptance from
DOM geometry. Source: owner fingerprint ZIP screenshot. Target: Playwright saved
full-page PNG. Normalizes only the observed Wix host banner height, not design.
"""
import argparse
import io
import json
import zipfile
from pathlib import Path

try:
    from PIL import Image, ImageChops, ImageStat
except ImportError as e:
    raise SystemExit('BLOCKED: Install the standard Pillow library for visual pixel QA') from e


def analyze(src, target, banner_px, pixel_threshold, allowed_bad_ratio):
    if banner_px < 0:
        raise ValueError('platform banner offset must be nonnegative')
    t = target.convert('RGB')
    if banner_px:
        if banner_px >= t.height:
            raise ValueError('observed Wix platform banner is taller than target screenshot')
        t = t.crop((0, banner_px, t.width, t.height))
    s = src.convert('RGB')
    same_width = s.width == t.width
    same_height = s.height == t.height
    common_w, common_h = min(s.width, t.width), min(s.height, t.height)
    if common_w == 0 or common_h == 0:
        raise ValueError('empty visual screenshot')
    # Do not resize or shift the donor design to force a similarity score.
    x = s.crop((0, 0, common_w, common_h))
    y = t.crop((0, 0, common_w, common_h))
    delta = ImageChops.difference(x, y)
    stats = ImageStat.Stat(delta)
    histogram = delta.convert('L').histogram()
    bad = sum(histogram[pixel_threshold+1:])
    ratio = bad / (common_w * common_h)
    return {
        'sourceSize': list(s.size),
        'targetSizeAfterBannerStrip': list(t.size),
        'measuredBannerPx': banner_px,
        'overlapSize': [common_w, common_h],
        'sameWidth': same_width,
        'sameHeight': same_height,
        'pixelThreshold': pixel_threshold,
        'badPixelRatio': round(ratio, 6),
        'allowedBadRatio': allowed_bad_ratio,
        'rgbMeanAbsoluteDifference': [round(v, 4) for v in stats.mean],
        'status': ('VISUAL_PIXEL_PASS' if same_width and same_height and ratio <= allowed_bad_ratio
                   else 'VISUAL_PIXEL_FAIL'),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--fingerprint', required=True)
    parser.add_argument('--screenshots', required=True)
    parser.add_argument('--out', required=True)
    parser.add_argument('--banner-px', type=int, default=0,
                        help='Observed target platform chrome height only; not a design adjustment')
    parser.add_argument('--threshold', type=int, default=12)
    parser.add_argument('--allowed-bad-ratio', type=float, default=.01)
    args = parser.parse_args()
    if not 0 <= args.threshold < 256 or not 0 <= args.allowed_bad_ratio <= 1:
        parser.error('threshold must be [0,255] and allowed-bad-ratio [0,1]')
    results = {}
    with zipfile.ZipFile(args.fingerprint) as z:
        for viewport in ('desktop-1280', 'mobile-390'):
            name = 'screenshots/' + viewport + '.png'
            if name not in z.namelist():
                parser.exit(2, 'BLOCKED: Source screenshot missing '+name+'\n')
            target = Path(args.screenshots) / (viewport + '.png')
            if not target.is_file():
                parser.exit(2, 'BLOCKED: Target screenshot missing '+str(target)+'\n')
            with Image.open(io.BytesIO(z.read(name))) as source_im, Image.open(target) as wix_im:
                results[viewport] = analyze(source_im, wix_im, args.banner_px,
                                            args.threshold, args.allowed_bad_ratio)
    result = {'schema': 'localdesign.wix-visual-qa.v1', 'viewports': results,
              'status': 'VISUAL_PASS' if all(v['status']=='VISUAL_PIXEL_PASS' for v in results.values())
                        else 'VISUAL_FAIL',
              'pixelEvidenceOnly': True,
              'fontsAndInteractions': 'separate acceptance gates',
              'noResizingOrForgedAlignment': True}
    Path(args.out).write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))
    if result['status']!='VISUAL_PASS':
        raise SystemExit(1)


if __name__=='__main__':
    main()
