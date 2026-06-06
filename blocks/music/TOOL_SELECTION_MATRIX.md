# Music Tool Selection Matrix

Status: candidate
Updated: 2026-06-06

## Purpose

Route each music job to the smallest suitable existing solution before custom implementation.

| Need | Default candidate | Alternative | Notes |
|---|---|---|---|
| Local full-song generation | ACE-Step 1.5 | stable-audio-tools | First local baseline to test. Supports UI, Python, REST, CLI, editing, stems, LoRA, metadata control, and long durations. |
| Cloud songs with vocals | Eleven Music | Google Lyria 3 Pro | Validate the active subscription terms before product use. |
| Cloud clips and structured songs | Google Lyria 3 Clip / Pro | Eleven Music | Useful for Gemini API workflows and image-conditioned generation. |
| Cloud real-time interactive music | Google Lyria RealTime | Magenta RealTime 2 | Experimental WebSocket path. Validate availability and latency before commitment. |
| Local real-time interactive music | Magenta RealTime 2 | Google Lyria RealTime | Best suited to Apple-Silicon-oriented experiments; offline NVIDIA inference is also documented. |
| Licensed background-music API for SaaS | SOUNDRAW API | Loudly, Beatoven | Prefer provider-backed commercial terms when legal simplicity matters. |
| Enterprise stems, playlists, streams | Loudly Music API | SOUNDRAW | Loudly advertises text-to-music, parameter control, stems, playlists, AI radio, and WAV export. |
| Background music and SFX API | Beatoven maestro API | SOUNDRAW | Beatoven advertises background music, SFX, and commercial clearance. |
| Editable composition with MIDI influence | AIVA | ACE-Step plus Basic Pitch | AIVA supports style models, audio or MIDI influence, editing, and downloads. Rights vary by plan. |
| Stem separation | ACE-Step native separation | Demucs / UVR5 | Prefer native separation when adequate. Demucs is a fallback utility. |
| Audio-to-MIDI | Spotify Basic Pitch | specialized transcription tools | Best used on one isolated instrument at a time. |
| MIDI manipulation | pretty_midi | DAW scripting | Use for tempo, chroma, transposition, creation, and export. |
| Audio analysis | Essentia | librosa | Review Essentia AGPLv3 implications before proprietary embedding. |
| Loudness normalization | FFmpeg loudnorm | pyloudnorm | Use FFmpeg for batch pipelines and pyloudnorm for Python workflows. |
| Reference mastering prototype | Matchering | DAW or engineer | Useful prototype; not a universal replacement for professional mastering. |
| Research donor | AudioCraft | stable-audio-tools | Useful for experiments; check code and checkpoint licenses separately. |

## Rules

1. Do not use one model for every music task.
2. Check model-weight licenses separately from code licenses.
3. Check the active provider plan before promising commercial rights.
4. Treat Suno and Udio as market benchmarks until their project-specific terms and integration path are separately validated.
5. Keep experimental models in the test lane until validation passes.

## Sources

- https://github.com/ace-step/ACE-Step-1.5
- https://github.com/magenta/magenta-realtime
- https://ai.google.dev/gemini-api/docs/music-generation
- https://ai.google.dev/gemini-api/docs/realtime-music-generation
- https://elevenlabs.io/docs/overview/capabilities/music
- https://soundraw.io/api
- https://www.loudly.com/music-api
- https://www.beatoven.ai/api
- https://www.aiva.ai/technology
- https://github.com/facebookresearch/demucs
- https://github.com/spotify/basic-pitch
- https://github.com/craffel/pretty-midi
- https://github.com/MTG/essentia
- https://github.com/csteinmetz1/pyloudnorm
- https://ffmpeg.org/ffmpeg-filters.html
- https://github.com/sergree/matchering
- https://github.com/facebookresearch/audiocraft
- https://github.com/Stability-AI/stable-audio-tools
