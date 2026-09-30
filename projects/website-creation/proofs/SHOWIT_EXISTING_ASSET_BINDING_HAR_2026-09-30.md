# Showit Existing Asset Binding HAR Discovery — 2026-09-30

Status: `DISCOVERY PROVEN / DIRECT API BINDING NOT YET LIVE-PROVEN`

## Purpose

Capture the exact page-model mutation produced when the owner selects an already-existing image from the Showit media library and assigns it to an empty graphic placeholder.

## Controlled capture

The owner opened the previously API-created empty graphic on `API PAGE — HERO`, opened the Showit image library, cleared Network, selected one existing image, waited for autosave, and exported a HAR with content.

The resulting HAR contained only three relevant requests:

1. `GET https://static.showit.com/400/2veyD7frCmjYoslvP2ftBg/354750/olga_polo_cincinnati_photographersc02941_websize.jpg` → `200 image/jpeg`;
2. `POST https://api.showit.com/designs/ljhcybjw0lbnr_qqyok5ma` → `200`;
3. CORS preflight `OPTIONS` → `204`.

The POST response returned `saved:true` and new ETag `57874ff8db59232d5986a67c840e2451`.

## Exact graphic mutation discovered

Before binding, the API-created placeholder was:

```json
{
  "type": "graphic",
  "visible": "a",
  "content": {},
  "mobile": {"w":280,"h":160,"x":20,"y":480,"a":0},
  "desktop": {"w":300,"h":450,"x":820,"y":100,"a":0},
  "sync": ["gs.t","o","blur","border.rad","shadow.style","trIn.type"]
}
```

After selecting the existing media asset, the geometry/sync/type remained unchanged and only `content` became:

```json
{
  "key": "2veyD7frCmjYoslvP2ftBg/354750/olga_polo_cincinnati_photographersc02941_websize.jpg",
  "aspect_ratio": 0.66688,
  "title": "Olga Polo Cincinnati PhotographerSC02941_websize",
  "type": "asset"
}
```

The same `content` object is present in the already-populated `IRONLINE — SERVICE 01` graphic, confirming that Showit binds an existing library image to a normal graphic through this `content` asset object.

## Architecture consequence

For an already-existing Showit media asset, image binding appears to be a page-model mutation only:

```text
empty graphic
→ set content = { key, aspect_ratio, title, type:"asset" }
→ whole-page authenticated save
→ image is rendered from static.showit.com
```

No separate media-upload request was present in this controlled capture because the selected image already existed in the Showit media library.

## Next acceptance gate

Directly bind an already-existing asset without using the image-picker UI:

```text
current page JSON + ETag
→ find one populated source graphic
→ find one empty target graphic
→ copy only source.content to target.content
→ one authenticated gzip POST
→ durable readback verifies target content exactly
→ reload editor
→ visual QA confirms the image appears in the target graphic
```

If that passes, mark `Showit existing-asset image binding` as `PROVEN LIVE`.

## Security rule

Do not persist any real `authToken` value. Runtime code may read `localStorage.authToken` only inside the already-authenticated owner session and send it only to Showit's API.
