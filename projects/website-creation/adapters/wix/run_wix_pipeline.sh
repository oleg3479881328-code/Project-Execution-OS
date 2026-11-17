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
  HOME_PAGE_ARGS=()
  if [[ "$WIX_TARGET_PAGE" == "(home)" ]]; then
    [[ "${APPROVED_REPLACE_HOME:-}" == "YES" &&
       "${WIX_HOME_APPROVED_SITE_ID:-}" == "$WIX_SITE_ID" ]] ||
      { echo "BLOCKED: Home requires APPROVED_REPLACE_HOME=YES and exact WIX_HOME_APPROVED_SITE_ID" >&2; exit 3; }
    HOME_PAGE_ARGS+=(--allow-home-target)
    [[ "$WIX_TARGET_PAGE_ID" != "" ]] || { echo "BLOCKED: Home Page ID required" >&2; exit 3; }
  else
    [[ "$WIX_TARGET_PAGE" =~ ^[a-z0-9-]+$ && "$WIX_TARGET_PAGE" != home ]] ||
      { echo "BLOCKED: invalid page folder, use (home) for explicit approved Home" >&2; exit 3; }
  fi
  HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
  WORK="${WIX_WORK_DIR:-$(mktemp -d)}"
  mkdir -p "$WORK"
  trap 'printf "QA workspace: %s\n" "$WORK"' EXIT
  # Owner-approved editable native Wix default behavior is the normal draft path.
  # A source-unmapped ledger remains mandatory; no silent source deletion.
  PARTIAL_NATIVE_ARGS=()
  if [[ "${WIX_NATIVE_DEFAULTS:-YES}" == "YES" &&
        "${WIX_ALLOW_PARTIAL_NATIVE_DRAFT:-YES}" == "YES" ]]; then
    PARTIAL_NATIVE_ARGS+=(--allow-partial-native-draft)
  fi
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
  python3 - "$WORK/recipe.json" "$WORK/source-unmapped-report.json" "${WIX_ALLOW_PARTIAL_NATIVE_DRAFT:-YES}" "${WIX_NATIVE_DEFAULTS:-YES}" <<'PY'
import json,sys,collections
r=json.load(open(sys.argv[1]))
unsupported=r.get('unsupported') or []
partial=(sys.argv[3]=='YES' and sys.argv[4]=='YES')
with open(sys.argv[2],'w') as f:
  json.dump({'schema':'peos.wix-source-unmapped.v1',
    'source':r['source'],'sourceHash':r.get('sha256'),
    'status':'PARTIAL_MANUAL_REFINEMENT' if unsupported else 'SOURCE_COVERED',
    'sourceObjectCoverage':r.get('sourceObjectCoverage'),
    'unmappedCount':len(unsupported),'unmapped':unsupported,
    'reasons':dict(collections.Counter(x.get('reason') for x in unsupported))},
    f,ensure_ascii=False,indent=2)
if unsupported and not partial:
  raise SystemExit('BLOCKED: mandatory source objects need exact native mapping; '
                   'use owner-authorized experimental partial mode')
images=[e['asset'] for s in r['sections'] for e in s['elements'] if e['type']=='image']
if not images or any(not isinstance(url,str) or url.startswith(('https://','http://')) is False for url in images):
  raise SystemExit('BLOCKED: exact source image evidence incomplete')
print('SOURCE_VERIFIED',len(r['sections']),'sections',
      sum(len(s['elements']) for s in r['sections']),'elements',
      len(images),'images','unmappedRetained',len(unsupported))
PY
  # Source completeness is independent of correct element coordinates.
  # An uncaptured donor video/canvas/iframe must block import instead of
  # generating a misleading GEOMETRY_ASSETS_PASS on an incomplete page.
  if node "$HERE/audit_source_layers.mjs" "$WORK/recipe.json" "$WORK/source-layer-audit.json" "$WORK/enriched-recipe.json"; then
    mv "$WORK/enriched-recipe.json" "$WORK/recipe.json"
  elif [[ "${#PARTIAL_NATIVE_ARGS[@]}" -gt 0 && -s "$WORK/source-layer-audit.json" ]]; then
    # Only an observed incomplete visual layer can downgrade to editable
    # static Wix default. Network/browser/tool failure still stops execution.
    python3 - "$WORK/source-layer-audit.json" <<'PY'
import json,sys
a=json.load(open(sys.argv[1]))
if a.get('status')!='BLOCKED_MISSING_SOURCE_LAYERS':
  raise SystemExit('BLOCKED: donor source audit could not be verified')
print('DRAFT_WITH_UNMAPPED_DYNAMIC_SOURCE',len(a.get('missing',[])))
PY
  else
    echo "BLOCKED: mandatory source audit unavailable" >&2
    exit 3
  fi
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
  VECTOR_MEDIA_ARGS=()
  [[ -n "${WIX_VECTOR_MEDIA_MANIFEST:-}" ]] && VECTOR_MEDIA_ARGS+=(--vector-media-manifest "$WIX_VECTOR_MEDIA_MANIFEST")
  wix origami export-site --site "$WIX_SITE_ID" -d "$WORK/wix-site" --json | tee "$WORK/export-result.json"
  python3 "$HERE/compile_full_page.py" compile --recipe "$WORK/recipe.json" \
    --export "$WORK/wix-site" --page "$WIX_TARGET_PAGE" \
    --page-id "$WIX_TARGET_PAGE_ID" --allow-replace-page "${HOME_PAGE_ARGS[@]}" "${PARTIAL_NATIVE_ARGS[@]}" "${VIDEO_MEDIA_ARGS[@]}" "${VECTOR_MEDIA_ARGS[@]}"
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
  python3 "$HERE/compile_full_page.py" finalize-media --export "$WORK/wix-site" --page "$WIX_TARGET_PAGE" "${HOME_PAGE_ARGS[@]}"
  # Owner-approved Wix-native defaults are part of the EXISTING PEOS pipeline.
  # They touch only WRichText font-family in the selected page, preserving
  # source X/Y/W/H, content and original media. No mandatory blocker bypass.
  if [[ "${WIX_NATIVE_DEFAULTS:-YES}" == "YES" ]]; then
    python3 "$HERE/apply_wix_native_defaults.py" --recipe "$WORK/recipe.json" \
      --fingerprint "$FINGERPRINT_ZIP" --export "$WORK/wix-site" \
      --page "$WIX_TARGET_PAGE" --out "$WORK/native-defaults-report.json" "${PARTIAL_NATIVE_ARGS[@]}"
  fi
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
    --readback "$WORK/wix-readback" --page "$WIX_TARGET_PAGE" --out "$WORK/readback-qa.json" "${PARTIAL_NATIVE_ARGS[@]}" "${VECTOR_MEDIA_ARGS[@]}"
  WIX_TARGET_PAGE="$WIX_TARGET_PAGE" node "$HERE/verify_full_browser.mjs" \
    "$WORK/recipe.json" "$PREVIEW_URL" "$WORK/wix-readback" "$WORK/screenshots" |
    tee "$WORK/browser-qa.json"
  python3 - "$WORK/browser-qa.json" "$WORK/native-defaults-report.json" <<'PY'
import json,sys,pathlib
result=json.load(open(sys.argv[1]))
if result.get('status')!='GEOMETRY_ASSETS_PASS':
  raise SystemExit('BLOCKED: actual browser geometry and assets did not pass')
defaults=json.load(open(sys.argv[2])) if pathlib.Path(sys.argv[2]).exists() else {}
if defaults.get('remainingMandatoryBlockers',0):
  print('DRAFT_WITH_UNMAPPED_SOURCE: native Wix page imported/editable;',
        defaults['remainingMandatoryBlockers'],'source mappings require manual refinement;',
        defaults.get('nativeDefaultCount',0),'native Wix font/effect defaults; SOURCE_VISUAL_PARITY=PARTIAL')
elif defaults.get('nativeDefaultCount',0):
  print('PASS_WITH_WIX_DEFAULTS: native import/readback passed but original fonts/effects need optional manual refinement.',
        defaults['nativeDefaultCount'],'source-tracked fallbacks; SOURCE_VISUAL_PARITY=PARTIAL')
elif result.get('visualPixelParity')!='PASS' or any(v.get('interactions')!='PASS' for v in result['views']):
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
