# Music Block Deep Research Report

Date: 2026-06-06
Status: completed research pass

## Executive Conclusion

The music block should not depend on one generator. A complete working system needs five lanes:

1. local generation and editing;
2. managed cloud generation;
3. real-time interactive music;
4. production utilities;
5. rights and provenance review.

## Recommended Default Candidates

### Local baseline: ACE-Step 1.5

Use as the first local full-song candidate because it exposes a web UI, CLI, Python API, REST API, Windows portable package, metadata controls, reference audio, cover generation, repaint, track separation, multitrack generation, Vocal2BGM, quality scoring, and LoRA training.

Source:
https://github.com/ace-step/ACE-Step-1.5

### Cloud song baseline: Google Lyria 3 and Eleven Music

Google Lyria 3 is available through Gemini API. Clip produces 30-second MP3 clips. Pro produces songs lasting a couple of minutes, supports verses, choruses, bridges, controllable duration, timestamps, image input, and WAV output.

Source:
https://ai.google.dev/gemini-api/docs/music-generation

Eleven Music is a managed text-to-music API candidate with vocals or instrumentals, multilingual output, section editing, and music finetunes. Its documentation states that the Music API is available to paid subscribers and that usage depends on music terms by plan.

Source:
https://elevenlabs.io/docs/overview/capabilities/music

### Real-time baseline: Magenta RealTime 2 and Google Lyria RealTime

Magenta RealTime 2 is the local experiment lane: open weights, Python JAX and MLX library, C++ streaming engine, AUv3 and standalone examples, Apple-Silicon real-time support, and offline NVIDIA inference.

Source:
https://github.com/magenta/magenta-realtime

Google Lyria RealTime is the cloud experiment lane: an experimental streaming instrumental-music model using persistent bidirectional low-latency WebSocket connections with interactive control.

Source:
https://ai.google.dev/gemini-api/docs/realtime-music-generation

### Embedded commercial API candidates

Use these when a provider-backed commercial path matters more than local control:

- SOUNDRAW API for apps, SaaS, games, video tools, creator tools, ambient systems, and multi-user generation;
- Loudly Music API for parametric generation, text-to-music, stems, playlists, and continuous streams;
- Beatoven API as a candidate for music and sound-effect generation;
- AIVA for composition workflows where MIDI and plan-dependent rights matter.

Sources:
- https://soundraw.io/api
- https://www.loudly.com/music-api
- https://www.beatoven.ai/api
- https://www.aiva.ai/technology

## Utility Chain

A production-ready block also needs:

- Demucs or UVR5 for fallback stem separation;
- Spotify Basic Pitch for audio-to-MIDI transcription;
- pretty_midi for MIDI analysis and editing;
- Essentia for music descriptors;
- FFmpeg loudnorm and pyloudnorm for normalization;
- Matchering as an optional reference-mastering prototype.

Sources:
- https://github.com/facebookresearch/demucs
- https://ultimatevocalremover.com/
- https://github.com/spotify/basic-pitch
- https://github.com/craffel/pretty-midi
- https://github.com/MTG/essentia
- https://github.com/csteinmetz1/pyloudnorm
- https://ffmpeg.org/ffmpeg-filters.html
- https://github.com/sergree/matchering

## Research Donors, Not Production Defaults

### AudioCraft

Useful donor patterns: MusicGen, AudioGen, MAGNeT, MusicGen Style, JASCO, and AudioSeal. Important boundary: repository code and released weights have different licenses.

Source:
https://github.com/facebookresearch/audiocraft

### stable-audio-tools

Useful for training, fine-tuning, inpainting, Gradio experiments, and checkpoint-specific research.

Source:
https://github.com/Stability-AI/stable-audio-tools

## Rights Boundary

Do not promise legal safety based on the generator name alone. Preserve provider, model version, plan, generation date, prompt, reference inputs, edits, outputs, and current terms evidence.

Suno illustrates why this matters: its official help center states that songs created on Pro or Premier are considered owned by the subscriber with retained commercial-use rights, while songs generated on the free Basic tier remain owned by Suno and are limited to non-commercial use.

Source:
https://help.suno.com/en/articles/2416769

## Files Added To The Music Block

- `TOOL_SELECTION_MATRIX.md`
- `STACK_ARCHITECTURES.md`
- `VALIDATION_GENERATION.md`
- `VALIDATION_REALTIME.md`
- `VALIDATION_UTILITIES.md`
- `RIGHTS_CHECKLIST.md`
- `REFERENCES_EXTENDED.md`

## Final Recommendation

The immediate practical next test is ACE-Step 1.5 on the available Windows machine. The first cloud comparison should use Lyria 3 and Eleven Music. Real-time work should stay in the experimental lane until a product actually requires it.