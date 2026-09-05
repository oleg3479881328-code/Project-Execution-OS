# Whisper Transcribe AI — Connected Integration

Status: ACTIVE integration / PILOT validation
Last verified: 2026-09-05

## Purpose

Use the connected Whisper Transcribe AI app as an Existing-Solution-First path for turning YouTube URLs and uploaded audio/video into transcript data that ChatGPT can analyze.

This integration closes a practical research gap: a YouTube video can be converted into searchable text with timestamps without requiring the owner to manually copy subtitles or download/re-upload media first.

## Proven Connection Evidence — 2026-09-05

Connected app: `Whisper Transcribe AI`.

Test source:

`https://m.youtube.com/watch?v=QngK6ftj3Ug`

Observed workflow:

```text
YouTube URL
-> connected Whisper Transcribe AI transcription job
-> processing
-> completed result
-> transcript text + paragraph timestamps + subtitle entries + detected duration
-> ChatGPT analysis / fact-check / project capture
```

The provider accepted the YouTube URL directly and returned a completed transcript package with timestamped text.

## Important Validation Limitation

The first test video reported a total duration of 558 seconds (9:18), but the returned transcript package covered only about the first 60 seconds.

Therefore:

- the integration itself is proven connected and operational;
- URL submission and transcript-result retrieval are proven;
- full-length transcript completeness is **not yet validated**;
- agents must compare transcript coverage/timestamps against media duration before treating a result as a complete-video transcript;
- a partial transcript must never be summarized as if it represented the entire video.

## Recommended Routing

For YouTube research or analysis:

```text
1. Try platform/native transcript or captions when readily accessible.
2. If direct transcript access is unavailable, blocked, or throttled, use connected Whisper Transcribe AI on the URL.
3. Verify transcript coverage against the reported video duration.
4. If coverage is incomplete and the full video matters, escalate to another supported path such as local/media-file Whisper or Faster-Whisper where rights and source access permit.
5. Only then perform full-video summary, claim extraction, fact-checking, or durable project capture.
```

For owned/uploaded audio or video, Whisper Transcribe AI may also be used as a convenient connected-app transcription path when local processing is unnecessary.

## Best Uses

- YouTube research intake;
- long-form video and interview analysis;
- extracting claims, instructions, products, tools, and workflow steps;
- fact-check preparation;
- timestamped notes;
- subtitle/caption preparation;
- turning video/audio sources into structured project knowledge;
- rapid analysis when YouTube page text or captions are inaccessible from the normal web path.

## Relationship To Reusable Capability Library

This connected SaaS integration is **not** the same thing as an implemented Project Execution OS `media.transcribe` executable capability block.

`media.transcribe` remains an `idea` in `capability-library/REGISTRY.md` until the reusable block itself is implemented and passes its required tests.

Whisper Transcribe AI is now a provider/ready-solution candidate that the future `media.transcribe` routing layer can call or emulate alongside local Whisper/Faster-Whisper paths.

## Existing Solution First Rule

Do not build custom YouTube transcript scraping or a new transcription service merely because direct web access to a video transcript fails.

First reuse the connected provider path. Build or adapt only for a demonstrated remaining gap such as transcript completeness, provider limits, privacy, cost, offline operation, or deterministic batch processing.

## Security / Data Boundary

Do not send confidential or rights-restricted media to an external transcription provider unless project policy permits it.

For sensitive, private, or locally controlled media, prefer an approved local transcription route when required.

## Related Nodes

- `docs/RESEARCH_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `blocks/youtube/READY_SOLUTIONS.md`
- `blocks/video-production/READY_SOLUTIONS.md`
- `blocks/video-production/REFERENCES.md`
- `capability-library/REGISTRY.md`

## Final Rule

Treat Whisper Transcribe AI as a useful connected transcription tool across projects, but verify transcript completeness before relying on it as evidence for an entire video.