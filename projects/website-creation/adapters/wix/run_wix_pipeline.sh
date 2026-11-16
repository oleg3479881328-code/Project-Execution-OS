#!/usr/bin/env bash
# Execute only in authenticated official Wix Studio Two/Origami environment.
# LocalDesign Fingerprint -> native test Wix page -> official readback QA.
set -euo pipefail
# Reuse the existing pipeline: whole page is an opt-in mode; old one-section mode remains.
if [[ "${WIX_MODE:-section}" == "full-page" ]]; then
  : "${WIX_SITE_ID:?Set existing Wix site ID}"
  : "${FINGERPRINT_ZIP:?Set LocalDesign Fingerprint ZIP}"
  : "${WIX_TARGET_PAGE:?Set exact existing Wix page folder}"
  : "${WIX_TARGET_PAGE_ID:?Set page ID from current export}"
  : "${PREVIEW_URL:?Set an official Wix draft/preview URL before target mutation; browser QA is mandatory}"
  [[ "${APPROVED_REPLACE_PAGE:-}" == "YES" ]] || { echo "BLOCKED: require APPROVED_REPLACE_PAGE=YES" >&2; exit 3; }
  [[ "$WIX_TARGET_PAGE" =~ ^[a-z0-9-]+$ && "$WIX_TARGET_PAGE" != home ]] || { echo "BLOCKED: explicit non-home target required" >&2; exit 3; }
  HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  WORK="${WIX_WORK_DIR:-$(mktemp -d)}"
  mkdir -p "$WORK"
  trap 'printf "QA workspace: %s\n" "$WORK"' EXIT
  RECIPE_ARGS=(--fingerprint "$FINGERPRINT_ZIP" --out "$WORK/recipe.json")
  [[ -n "${WIX_SOURCE_SECTIONS:-}" ]] && RECIPE_ARGS+=(--sections "$WIX_SOURCE_SECTIONS")
  python3 "$HERE/full_page_recipe.py" "${RECIPE_ARGS[@]}"
  # The observed desktop width, not a fixed legacy 1280, is the build and QA contract.
  python3 - "$WORK/recipe.json" <<'PY'
import json,sys
r=json.load(open(sys.argv[1]));w=r.get('desktopWidth',1280)
if w not in (1280,1920) or 'desktop-'+str(w) not in r.get('viewports',{}):
    raise SystemExit('BLOCKED: source desktop width is not an observed supported viewport')
if 'mobile-390' not in r.get('viewports',{}):
    raise SystemExit('BLOCKED: mobile-390 viewport missing')
print('SOURCE_VIEWPORTS_VERIFIED',w,390)
PY
  python3 - "$WORK/recipe.json" <<'PY'
import json,sys
r=json.load(open(sys.argv[1]))
if r.get('unsupported'):
  raise SystemExit('BLOCKED: unsupported source layers '+json.dumps(r['unsupported'][:3]))
images=[e['asset'] for s in r['sections'] for e in s['elements'] if e['type']=='image']
if not images or any(not url.startswith(('https://','http://')) for url in images):
  raise SystemExit('BLOCKED: exact source image evidence incomplete')
print('SOURCE_VERIFIED',len(r['sections']),'sections',sum(len(s['elements']) for s in r['sections']),'elements',len(images),'images')
PY
  # Source completeness is independent of correct element coordinates.
  # An uncaptured donor video/canvas/iframe must block import instead of
  # generating a misleading GEOMETRY_ASSETS_PASS on an incomplete page.
  node "$HERE/audit_source_layers.mjs" "$WORK/recipe.json" "$WORK/source-layer-audit.json" "$WORK/enriched-recipe.json"
  mv "$WORK/enriched-recipe.json" "$WORK/recipe.json"
  # Native Video MP4 is imported by the official Wix Media Manager API, not
  # Origami upload-media (which only scans image props in this CLI version).
  # Readback-ready file descriptors must match the donor's *exact* source URL.
  python3 - "$WORK/recipe.json" "${WIX_VIDEO_MEDIA_MANIFEST:-}" <<'PY'
import json,sys
r=json.load(open(sys.argv[1]))
videos=[l['sourceUrl'] for s in r['sections'] for l in s.get('dynamicLayers',[]) if l['type']=='video']
if videos:
  if not sys.argv[2]:
    raise SystemExit('BLOCKED: original source videos require WIX_VIDEO_MEDIA_MANIFEST with official READY Media Manager descriptors')
  m=json.load(open(sys.argv[2]))
  f=[x.get('file',x) for x in m.get('files',[])]
  for source in videos:
    matches=[x for x in f if x.get('sourceUrl')==source and x.get('operationStatus')=='READY' and x.get('mediaType')=='VIDEO']
    if len(matches)!=1:raise SystemExit('BLOCKED: exact source video not READY or ambiguous '+source)
print('SOURCE_VIDEO_MEDIA_VERIFIED',len(videos))
PY
  VIDEO_MEDIA_ARGS=()
  [[ -n "${WIX_VIDEO_MEDIA_MANIFEST:-}" ]] && VIDEO_MEDIA_ARGS+=(--video-media-manifest "$WIX_VIDEO_MEDIA_MANIFEST")
  wix origami export-site --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json | tee "$WORK/export-result.json"
  python3 "$HERE/compile_full_page.py" compile --recipe "$WORK/recipe.json" \
    --export "$WORK/wix-site" --page "$WIX_TARGET_PAGE" \
    --page-id "$WIX_TARGET_PAGE_ID" --allow-replace-page "${VIDEO_MEDIA_ARGS[@]}"
  # Official upload-media resolves Image wrapper definition.ts from installed
  # dependencies. Without yarn install it silently detects zero images.
  (cd "$WORK/wix-site" && yarn install)
  wix origami upload-media --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json | tee "$WORK/media-result.json"
  python3 - "$WORK/media-result.json" "$WORK/recipe.json" <<'PY'
import json,sys
m=json.load(open(sys.argv[1]));r=json.load(open(sys.argv[2]))
expected=sum(e['type']=='image' for s in r['sections'] for e in s['elements'])
if m.get('failed'):
  raise SystemExit('BLOCKED: Wix official upload-media failed '+str(m['failed']))
# Previously imported files can be skipped by Wix: do NOT demand a 1:1
# upload count. finalize-media validates a real Wix URI for EVERY image.
print('MEDIA_UPLOAD_SCAN_PASS',{'sourceImageInstances':expected,'newUploads':len(m.get('uploaded',[]))})
PY
  python3 "$HERE/compile_full_page.py" finalize-media --export "$WORK/wix-site" --page "$WIX_TARGET_PAGE"
  cd "$WORK/wix-site"
  yarn install
  yarn lint && yarn tsc && yarn build
  python3 - "$WIX_TARGET_PAGE" <<'PY'
import subprocess,sys
target='packages/site-app/src/pages/'+sys.argv[1]+'/'
s=subprocess.run(['git','status','--porcelain'],text=True,capture_output=True,check=True).stdout
files=[line[3:] for line in s.splitlines() if line.strip()]
bad=[x for x in files if not x.startswith(target)]
if bad or not files:raise SystemExit('BLOCKED: scope changed outside page or empty '+repr(bad))
print('TARGET_SCOPE_PASS',len(files))
PY
  wix origami import-site --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json | tee "$WORK/import-result.json"
  python3 - "$WORK/import-result.json" "$WIX_TARGET_PAGE" <<'PY'
import json,sys
v=json.load(open(sys.argv[1]));expected='pages/'+sys.argv[2]
if v.get('updated')!=[expected] or v.get('deleted') or v.get('renamed'):
  raise SystemExit('BLOCKED: import scope unexpected '+repr({k:v.get(k) for k in ('updated','deleted','renamed')}))
print('WIX_IMPORTED',v.get('siteRevisions'))
PY
  wix origami export-site --site "$WIX_SITE_ID" -d "$WORK/wix-readback" --json | tee "$WORK/readback-result.json"
  python3 "$HERE/verify_full_page.py" --recipe "$WORK/recipe.json" \
    --readback "$WORK/wix-readback" --page "$WIX_TARGET_PAGE" --out "$WORK/readback-qa.json"
  WIX_TARGET_PAGE="$WIX_TARGET_PAGE" node "$HERE/verify_full_browser.mjs" \
    "$WORK/recipe.json" "$PREVIEW_URL" "$WORK/wix-readback" "$WORK/screenshots" |
    tee "$WORK/browser-qa.json"
  python3 - "$WORK/browser-qa.json" <<'PY'
import json,sys
result=json.load(open(sys.argv[1]))
if result.get('status')!='GEOMETRY_ASSETS_PASS':
  raise SystemExit('BLOCKED: actual browser geometry and assets did not pass')
if result.get('visualPixelParity')!='PASS' or any(v.get('interactions')!='PASS' for v in result['views']):
  print('PARTIAL_ACCEPTANCE: Native geometry/assets passed; visual pixel and interaction QA NOT ACCEPTED.')
else:
  print('FULL_ACCEPTANCE: Visual and interaction gates passed.')
PY
  echo 'No publication. Do not mark one-to-one DONE without screenshot and interaction acceptance.'
  exit 0
fi

: "${WIX_SITE_ID:?Set WIX_SITE_ID}"
: "${FINGERPRINT_ZIP:?Set FINGERPRINT_ZIP}"
: "${SOURCE_SECTION:?Set SOURCE_SECTION, e.g. div#experience}"
: "${WIX_TEST_PAGE:?Set WIX_TEST_PAGE, e.g. blank}"
: "${PREVIEW_URL:?Set PREVIEW_URL from official Wix draft preview}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORK="$(mktemp -d)"
trap 'printf "QA workspace: %s\n" "$WORK"' EXIT

python3 "$HERE/localdesign_wix.py" extract \
  --fingerprint "$FINGERPRINT_ZIP" --section "$SOURCE_SECTION" \
  --out "$WORK/recipe.json"

wix origami export-site --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json

python3 "$HERE/localdesign_wix.py" apply \
  --recipe "$WORK/recipe.json" \
  --wix-export "$WORK/wix-site" --page "$WIX_TEST_PAGE"

cd "$WORK/wix-site"
yarn install
yarn lint
yarn tsc

CHANGED="$(git status --porcelain | awk '{print $2}' | grep '^packages/site-app/src/pages/' | grep -v "^packages/site-app/src/pages/$WIX_TEST_PAGE/" || true)"
if [[ -n "$CHANGED" ]]; then
  echo "BLOCKED: unrelated page changed: $CHANGED" >&2
  exit 3
fi

wix origami import-site --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json | tee "$WORK/import-result.json"
wix origami export-site --site "$WIX_SITE_ID" -d "$WORK/wix-readback" --json

node "$HERE/verify_geometry.mjs" "$WORK/recipe.json" "$PREVIEW_URL" 1280,1920 | tee "$WORK/geometry-qa.json"
echo 'LOCAL_GEOMETRY_PASS (Desktop only); site was not published.'
