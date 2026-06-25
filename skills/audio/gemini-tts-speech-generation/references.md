# Gemini TTS Speech Generation — References

## Official Source

- Gemini API speech generation / TTS documentation: https://ai.google.dev/gemini-api/docs/speech-generation?hl=ru

## Source Snapshot

- Source checked: 2026-06-24.
- Documentation last-updated marker observed: 2026-06-22 UTC.
- Source owner: Google AI for Developers.
- Source topic: Gemini API text-to-speech generation.

## Extracted Operating Facts

These notes are source-derived constraints for this skill. Re-check the official source before implementation because the Gemini TTS surface is preview-stage and can change.

- Gemini API TTS converts text input into audio output for one or more speakers.
- Gemini TTS is promptable with natural-language direction for style, accent, pace, and tone.
- Gemini API TTS is different from Gemini Live API: use TTS for precise scripted playback; use Live API for interactive, unstructured audio sessions.
- TTS models accept text-only input and generate audio-only output.
- The official examples use `response_format: { type: "audio" }` and `generation_config.speech_config`.
- The official examples decode returned base64 audio data and save WAV output.
- Single-speaker generation uses one voice configuration.
- Multi-speaker generation requires matching speaker names in the transcript and speaker voice configuration; the documented limit is up to 2 speakers.
- Streaming generation uses `stream: true` and must be checked against current model support before use.
- As observed in the source snapshot, supported models listed include `Gemini 3.1 Flash TTS Preview`, `Gemini 2.5 Flash Preview TTS`, and `Gemini 2.5 Pro Preview TTS`.
- The prompting guide recommends building a performance prompt with audio profile, scene, director notes, sample context, transcript, and optional audio tags.
- Audio tags such as `[whispers]`, `[laughs]`, `[sighs]`, `[excited]`, and `[shouting]` can guide delivery.
- For non-English transcripts, the documentation recommends using audio tags in English for best results.
- The documented context-window limit for a TTS session is 32,000 tokens.
- Long text quality can degrade after several minutes of generated speech; chunk long transcripts.
- The model can occasionally return text tokens instead of audio tokens, producing server errors; implementation should include retry logic.
- Vague prompts can cause false prompt-classifier behavior, request rejection, or reading style instructions aloud; use clear TTS framing and transcript boundaries.

## Related Official Sources To Re-check When Implementing

- Gemini model list: https://ai.google.dev/gemini-api/docs/models
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini API rate limits: https://ai.google.dev/gemini-api/docs/rate-limits
- Gemini Live API overview: https://ai.google.dev/gemini-api/docs/live
- Gemini audio understanding guide: https://ai.google.dev/gemini-api/docs/audio

## Governance Notes

- This skill is a candidate central skill.
- It is not active until reviewed under Project Execution OS governance.
- It is intentionally Gemini-specific and should not be expanded into a generic TTS provider comparison skill.
