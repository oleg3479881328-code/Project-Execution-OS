# Showit Image Placeholder Proof — 2026-09-30

Status: `PROVEN LIVE`

## Result

A native empty Showit image/graphic placeholder was created programmatically inside `API PAGE — HERO` and saved through the established whole-page save path.

Accepted evidence:
- target block ID: `z2QpLNLUl`;
- new element index: `3`;
- previous target elements: `3`;
- total target elements after save: `4`;
- old ETag: `0a7adf22622a980a70660c21467fde87`;
- new ETag: `c16086bd3a5c2ecce5f12881b6347732`;
- readback passed on attempt 1;
- 15 unrelated Canvas verified unchanged;
- API write count: `1`;
- editor reload succeeded;
- target Canvas UI count: `1`;
- `graphic` layer UI count: `1`;
- final marker: `SHOWIT EMPTY IMAGE PLACEHOLDER — PROOF COMPLETED`.

Generated element shape:

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

After reload, Showit rendered its normal gray striped placeholder with `Double click to add an image`, proving the generated model is interpreted as a native image placeholder rather than merely stored JSON.

## Architecture consequence

`text elements + empty graphic/image placeholders → Showit JSON compiler → one whole-page save` is now `PROVEN LIVE` on an existing page.

Asset upload and asset binding remain separate unproven capabilities.

## Next proof

Inspect one already-populated Showit `graphic` element and compare its `content` object with the proven empty placeholder. Then bind an already-existing asset to the API-created placeholder before researching upload.
