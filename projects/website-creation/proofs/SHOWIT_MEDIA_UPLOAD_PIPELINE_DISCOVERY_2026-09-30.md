# Showit Media Upload Pipeline Discovery — 2026-09-30

Status: CAPTURE PROVEN / DIRECT API REPLAY NOT YET LIVE-PROVEN

## What was captured
A clean HAR was recorded while uploading one new local image file through the Showit media library.

Uploaded file observed in this capture:
- filename normalized by Showit: `stationery.png`
- width: 1024
- height: 1536
- size: 2444621 bytes
- aspect ratio returned by Showit: 0.66667

## Observed upload pipeline
1. `POST https://api.showit.com/useruploads`
   - JSON body contains filename, size, width, height, and folder_id.
   - Response creates an asset record immediately and returns:
     - `asset_id`
     - normalized filename / asset_name
     - width / height / size / aspect_ratio
     - asset `key`
     - `upload_id`
     - a short-lived presigned S3 PUT URL
     - required upload headers such as Content-Type.

2. Browser sends the raw image bytes with `PUT` to the returned presigned S3 URL under the Showit uploads bucket.
   - For this capture the request Content-Type was `image/png`.
   - S3 returned HTTP 200 and an object ETag.

3. `POST https://api.showit.com/useruploads/<upload_id>/complete`
   - Request body was `{}`.
   - Response confirmed the upload and returned the same asset_id plus a file_id and metadata.

4. Showit then loaded the generated preview from its static media CDN using a URL shaped like:
   - `/v2/<user_id>/<asset_id>/<filename>/preview`

## Architectural implication
New-media upload is separate from page JSON save. The complete path is now understood as:

`local file bytes -> create upload record -> presigned S3 PUT -> complete upload -> asset key -> graphic.content -> page save`

Existing-asset binding had already been proven separately by assigning `graphic.content` and performing one page save.

## Security note
The HAR contained a time-limited signed S3 URL and temporary AWS signing material. Those values are intentionally not copied into this durable proof.

## Remaining acceptance test
Run the upload flow programmatically without using the Showit media picker UI. Acceptance requires:
- create upload record succeeds,
- bytes are PUT to the returned presigned URL,
- complete endpoint succeeds,
- returned asset becomes visible through Showit/static preview,
- asset can then be bound to a graphic element and survives readback/reload.
