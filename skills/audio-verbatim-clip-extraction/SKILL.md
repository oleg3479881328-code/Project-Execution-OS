# Audio Verbatim Clip Extraction Skill

## Purpose

Create a reliable editing package from an audio recording by using an external transcription system when the active agent cannot directly or confidently transcribe the source audio.

## Lifecycle State

`candidate`

## Trigger

Use this skill when the task requires exact spoken fragments from an audio recording, especially:

- poems, lyrics, hooks, quotes, or memorable phrases;
- a specific speaker's authentic words;
- montage-ready clips for reels, songs, shorts, podcasts, interviews, or documentaries;
- speaker separation and precise timestamps;
- external transcription through Gemini or another capable system.

## Do Not Use

Do not use this skill when:

- a rough summary is sufficient;
- the audio has already been transcribed with trustworthy timestamps;
- the task does not require verbatim language or source-accurate clips.

## Inputs

- original audio file;
- target speaker name or role;
- requested fragment type;
- intended use;
- optional language and context.

## Workflow

1. Preserve the original audio unchanged.
2. Verify and record the source duration, filename, size, and checksum where available.
3. Send the complete recording to an external transcription system capable of processing the full file.
4. Request a full transcript with speaker labels.
5. Require exact start and end timestamps using millisecond precision.
6. Require verbatim transcription without grammar correction, paraphrase, or normalization.
7. Mark unclear words and alternate interpretations explicitly.
8. Extract every relevant fragment from the target speaker.
9. Preserve repeated takes and variants separately.
10. Record overlap from other speakers and confidence for each clip.
11. Rank the strongest clips for the intended output.
12. Produce a clean montage sheet and JSON clip manifest.
13. Cross-check timestamp consistency across all outputs.
14. Compare the transcript-reported duration against the actual source duration.
15. Return the original audio and all derived files together.

## Mandatory Output Package

- `source_audio.*`
- `full_transcript.md`
- `target_speaker_clips.md`
- `montage_sheet.txt`
- `clips.json`
- `quality_control.md`

## Minimum Clip Schema

```json
{
  "id": 1,
  "start": "00:00.000",
  "end": "00:00.000",
  "speaker": "",
  "text_verbatim": "",
  "type": "",
  "confidence": "high|medium|low",
  "other_voice_overlap": false,
  "usable_for_edit": true
}
```

## Accuracy Rules

- Never invent missing words.
- Never silently improve speech.
- Never merge lines spoken at different times.
- Never attribute another speaker's words to the target speaker.
- Preserve multilingual speech and code-switching.
- Preserve alternate takes.
- Flag duration mismatches before cutting source media.
- Keep timestamps identical across transcript, tables, montage sheet, and JSON.

## Failure Behavior

Transcription failure must not remove the source audio from the handoff. Return the original file plus a visible failure report describing what failed and what remains available.

## Validation Checklist

- source audio is present;
- full recording was processed;
- source duration and reported duration match;
- speaker labels are consistent;
- target-speaker fragments are verbatim;
- repetitions are retained;
- timestamps are internally consistent;
- montage sheet and JSON contain the same clips;
- unclear audio is labeled;
- original audio and derived files are packaged together.

## Demonstrated Pattern

The workflow was validated on a conversation containing Marusya's original song lyrics and spoken phrases. External transcription produced speaker-separated text, repeated lyric takes, exact time ranges, ranked clips, a montage sheet, and JSON. The receiving agent could then use Marusya's authentic voice and words in a reel instead of recreating the material.

## Status Boundary

This artifact is registered as a candidate skill. It becomes active only after review under the Project Execution OS skill lifecycle and review standards.
