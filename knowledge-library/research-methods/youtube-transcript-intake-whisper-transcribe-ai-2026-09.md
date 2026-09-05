# YouTube Transcript Intake via Whisper Transcribe AI

Status: reusable research method / pilot-verified integration
Date: 2026-09-05

## Finding

A connected Whisper Transcribe AI integration is useful as a reusable research intake path for YouTube and uploaded audio/video sources.

It reduces friction between `video URL` and `analyzable text` by allowing ChatGPT to submit supported media URLs for transcription and retrieve timestamped transcript data.

## Why This Matters Across Projects

Many project research tasks depend on videos, demonstrations, tutorials, interviews, product walkthroughs, and creator explanations. Normal web access to YouTube text may fail, captions may be inaccessible, or the page may be throttled.

The connected transcription route provides an Existing-Solution-First fallback before custom scraping, manual subtitle copying, or building a new downloader/transcription pipeline.

## Pilot Evidence

Source tested:

`https://m.youtube.com/watch?v=QngK6ftj3Ug`

Observed result:

- URL submission accepted;
- transcription job processed to completion;
- result returned transcript text;
- paragraph timestamps and subtitle entries were returned;
- media duration was returned as 558 seconds.

## Critical Limitation Found

Although the media duration was 558 seconds (9:18), the returned transcript in the first test covered only about 60 seconds.

Therefore the correct reusable method is not simply `URL -> transcript -> summary`.

It is:

```text
URL
-> obtain transcript
-> verify transcript coverage against media duration
-> classify COMPLETE or PARTIAL
-> only then summarize / fact-check / capture claims
```

A partial transcript must never be treated as evidence for the whole video.

## Recommended Research Routing

```text
1. Platform/native captions or transcript when accessible.
2. Connected Whisper Transcribe AI when native/direct transcript access is unavailable, blocked, or throttled.
3. Verify transcript coverage.
4. If partial and the full source matters, use another approved transcription route such as local/media-file Whisper or Faster-Whisper when rights and access permit.
5. Perform claim extraction, summary, fact-check, and project capture only on verified coverage.
```

## Reuse Decision

Use this connected provider before inventing custom YouTube transcript extraction.

Custom implementation is justified only by a demonstrated remaining gap such as:

- incomplete transcript coverage;
- provider limits;
- privacy/confidentiality;
- offline operation;
- batch automation;
- deterministic reproducibility;
- cost or quota constraints.

## Related System Nodes

- `docs/integrations/whisper-transcribe-ai/README.md`
- `docs/RESEARCH_STANDARD.md`
- `docs/EXISTING_SOLUTION_FIRST_STANDARD.md`
- `blocks/youtube/READY_SOLUTIONS.md`
- `blocks/video-production/READY_SOLUTIONS.md`
- `capability-library/REGISTRY.md`

## Final Rule

Whisper Transcribe AI is now a reusable cross-project research tool, but transcript completeness must be verified before the result is used as whole-video evidence.
