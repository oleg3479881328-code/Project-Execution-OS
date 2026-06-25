---
name: gemini-tts-speech-generation
description: Prepare Gemini API text-to-speech generation packets for scripted speech audio.
category: audio
status: candidate
target_agent: tool-neutral
compatibility:
  - chatgpt
  - codex
  - claude
inputs:
  - speech_script
  - language_or_locale
  - speaker_plan
  - voice_style_requirements
  - implementation_target
outputs:
  - tts_prompt_packet
  - api_generation_plan
  - validation_plan
  - risk_and_limitations_report
safety_level: medium
source: google_gemini_api_speech_generation_docs
review_status: not_reviewed
version: 0.1.0
---

# Gemini TTS Speech Generation

## Purpose

Prepare a reproducible Gemini API text-to-speech generation packet from a script, voice direction, and implementation target.

This skill is for scripted speech output: narration, short-form voiceover, podcast-style dialogue, audiobook fragments, product demos, tutorials, and other text-to-audio tasks where the spoken transcript is known or can be prepared before generation.

## When To Use

Use this skill when the task requires:

- generating speech audio from a written script through Gemini API TTS;
- creating a single-speaker voiceover plan;
- creating a two-speaker dialogue plan;
- converting a content brief into a TTS-ready transcript and director prompt;
- preparing Python, JavaScript, or REST implementation notes for Gemini TTS;
- reviewing a Gemini TTS integration for prompt, model, voice, chunking, retry, or output-handling risks.

## When Not To Use

Do not use this skill when:

- the user needs live interactive audio conversation instead of scripted TTS;
- the task is speech-to-text, audio understanding, dubbing alignment, lip sync, or music generation;
- the task requires cloning or impersonating a real person's voice without explicit rights and disclosure;
- the implementation should be provider-neutral rather than Gemini-specific;
- the request only asks for copywriting and does not require audio-generation planning.

## Required Inputs

- Speech script or content brief.
- Target language or locale, preferably BCP-47 when implementation needs it.
- Speaker count: one speaker or two speakers.
- Speaker names when dialogue is used.
- Desired voice direction: style, tone, accent, pace, energy, emotion, audience, and content context.
- Preferred Gemini TTS model, or permission to select the current documented model.
- Target implementation surface: Python, JavaScript, REST, app backend, prototype, or manual AI Studio test.
- Output requirements: file format, streaming or non-streaming, duration target, chunking needs, storage path, and validation method.

## Outputs

- TTS prompt packet with clear transcript boundary.
- Speaker and voice plan.
- Gemini API generation plan.
- Implementation notes for the selected target surface.
- Audio output handling plan, including base64 decode and WAV/PCM packaging when relevant.
- Chunking and retry policy.
- Validation checklist for listening review and technical review.
- Risk and limitation notes.

## Workflow

```text
1. Confirm the task is scripted text-to-speech, not live interactive audio.
2. Open the current official Gemini speech-generation documentation before implementation.
3. Verify the current supported models, endpoint/API surface, SDK syntax, voices, streaming support, languages, and limitations.
4. Normalize the script: remove unclear markup, preserve intentional pauses, and mark the exact spoken transcript.
5. Choose the speaker plan:
   - one speaker: one voice config;
   - two speakers: speaker names in transcript must match configured speakers.
6. Build the director prompt:
   - audio profile;
   - scene/context;
   - director notes for style, pace, accent, emotion, articulation, and energy;
   - optional sample context;
   - transcript section with a clear start marker.
7. Use audio tags only where they improve delivery, such as [whispers], [laughs], [sighs], [excited], or [shouting]. For non-English transcripts, prefer English audio tags unless current documentation says otherwise.
8. Select implementation mode:
   - Python SDK;
   - JavaScript SDK;
   - REST;
   - AI Studio test before coding.
9. Prepare API configuration:
   - request audio response format;
   - set speech_config with selected voice or speaker/voice pairs;
   - decode returned audio data;
   - save or stream according to the target.
10. Add production guards:
    - split long transcripts into smaller chunks;
    - retry transient failures;
    - handle occasional non-audio or server-error responses;
    - keep API keys outside committed files;
    - require human listening review before publishing.
11. Return the implementation packet and explicitly mark unresolved assumptions or blockers.
```

## Prompt Packet Template

```text
TTS the following script.

# AUDIO PROFILE: <speaker name or narrator profile>
## <short voice archetype>

## THE SCENE
<physical setting, emotional atmosphere, audience, and content situation>

### DIRECTOR'S NOTES
Style: <specific style direction>
Pacing: <pace and rhythm>
Accent: <specific accent or neutral delivery requirement>
Energy: <projection, warmth, seriousness, tension, excitement>
Articulation: <clarity, pauses, emphasis, pronunciation notes>

### SAMPLE CONTEXT
<optional context that helps the model perform naturally>

#### TRANSCRIPT
<exact text to speak>
```

For two-speaker dialogue, the transcript speaker names must match the configured speaker names.

## Constraints

- Treat Gemini TTS as a Gemini-specific adapter skill, not as a universal speech-generation standard.
- Re-check official documentation before implementation because TTS models, preview status, voice names, endpoints, and SDK syntax can change.
- Do not claim an audio file was generated unless an actual API call ran and a concrete output artifact exists.
- Do not commit API keys, tokens, generated private audio, or user-provided sensitive scripts unless the owner explicitly asks for durable storage.
- Do not use this skill to deceptively impersonate a real person or create undisclosed synthetic speech in sensitive contexts.
- Keep prompt direction aligned with the chosen voice; do not ask a mismatched voice to perform an incompatible persona.
- For long content, plan chunking before generation rather than sending a full long-form script in one request.
- For streaming output, verify current model support first.
- Do not exceed the current documented speaker limit without re-checking official documentation.

## Failure Modes

- Model name, endpoint, or SDK syntax is outdated.
- Voice selection is undocumented or no longer supported.
- Speaker names in transcript do not match speaker configuration.
- The prompt is too vague and the model reads style instructions aloud instead of only the transcript.
- The prompt is too complex and constrains delivery unnaturally.
- Long transcript quality degrades because the content was not chunked.
- API returns transient server errors or non-audio/text tokens and no retry handling exists.
- Output audio is claimed but not saved, decoded, or validated.
- Generated voice mismatches the intended age, gender impression, accent, tone, or role.
- Safety or rights review is skipped for real-person voice imitation or sensitive scripts.

## Validation Checklist

- [ ] task is scripted TTS, not live audio conversation;
- [ ] official Gemini speech-generation docs were checked for current model/API details;
- [ ] target model and implementation surface are named;
- [ ] speaker count and speaker names are defined;
- [ ] voice names are taken from the current documented voice list;
- [ ] prompt has a clear transcript boundary;
- [ ] style, accent, pace, and tone instructions are specific but not overconstrained;
- [ ] long scripts have a chunking plan;
- [ ] retry handling is specified for transient failures;
- [ ] API key handling is safe;
- [ ] generated audio must pass human listening review before publication;
- [ ] lifecycle status remains candidate until central review promotes it.

## References

See `references.md`.
