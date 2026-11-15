#!/usr/bin/env bash
# Execute only in authenticated official Wix Studio Two/Origami environment.
# LocalDesign Fingerprint -> native test Wix page -> official readback QA.
set -euo pipefail
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
