# Music Block Extended References

Updated: 2026-06-06

## Core Generation References

### ACE-Step 1.5
Source: https://github.com/ace-step/ACE-Step-1.5

Why it matters:
- local full-song generation;
- UI, CLI, Python API, REST API, and VST3 paths;
- reference audio, cover, repaint, stems, metadata control, LoRA, and multilingual lyrics;
- Windows portable package and hardware-tier guidance.

### Magenta RealTime 2
Sources:
- https://magenta.withgoogle.com/magenta-realtime-2
- https://github.com/magenta/magenta-realtime

Why it matters:
- open-weight real-time generation;
- Python JAX / MLX library and C++ streaming engine;
- AUv3, standalone, and example-app paths;
- Apple-Silicon-oriented real-time support and offline NVIDIA inference.

### Google Lyria 3 and Lyria RealTime
Sources:
- https://ai.google.dev/gemini-api/docs/music-generation
- https://ai.google.dev/gemini-api/docs/realtime-music-generation

Why they matter:
- cloud generation through Gemini API;
- short clips and structured full-song workflows;
- custom lyrics, timestamps, image-conditioned generation, WAV and MP3 output;
- experimental WebSocket real-time generation.

### Eleven Music
Sources:
- https://elevenlabs.io/music
- https://elevenlabs.io/docs/overview/capabilities/music

Why it matters:
- managed API candidate;
- songs with vocals and multilingual lyrics;
- section editing, inpainting, and reference-audio workflows;
- MP3 and WAV output.

## Commercial API Candidates

- SOUNDRAW API: https://soundraw.io/api
- Loudly Music API: https://www.loudly.com/music-api
- Beatoven API: https://www.beatoven.ai/api
- AIVA: https://www.aiva.ai/technology

Validate pricing, plan limits, commercial terms, output rights, and product fit before use.

## Utility References

- Demucs: https://github.com/facebookresearch/demucs
- UVR5: https://ultimatevocalremover.com/
- Spotify Basic Pitch: https://github.com/spotify/basic-pitch
- pretty_midi: https://github.com/craffel/pretty-midi
- Essentia: https://github.com/MTG/essentia
- pyloudnorm: https://github.com/csteinmetz1/pyloudnorm
- FFmpeg filters: https://ffmpeg.org/ffmpeg-filters.html
- Matchering: https://github.com/sergree/matchering

## Research Donors

### AudioCraft
Source: https://github.com/facebookresearch/audiocraft

Use as donor material for MusicGen, AudioGen, MAGNeT, MusicGen Style, JASCO, and AudioSeal patterns. Check code and model-weight licenses separately.

### stable-audio-tools
Source: https://github.com/Stability-AI/stable-audio-tools

Use as donor material for training, inference, Gradio prototypes, conditional diffusion, inpainting, and checkpoint-specific license review.

## Final Rule

References are evidence and donor material, not automatic recommendations.