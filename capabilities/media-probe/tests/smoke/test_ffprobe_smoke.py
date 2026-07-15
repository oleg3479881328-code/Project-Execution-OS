import shutil
import wave
from pathlib import Path

import pytest

from peos_media_probe import ArtifactRef, BlockContext, BlockRequest, MediaProbeBlock


@pytest.mark.skipif(shutil.which("ffprobe") is None, reason="ffprobe is not installed")
def test_real_ffprobe_can_probe_generated_wav(tmp_path: Path) -> None:
    audio = tmp_path / "tone.wav"
    sample_rate = 8000
    frame_count = 800

    with wave.open(str(audio), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b"\x00\x00" * frame_count)

    result = MediaProbeBlock().run(
        BlockRequest(
            request_id="smoke-1",
            input_artifacts=(
                ArtifactRef(
                    artifact_id="wav-1",
                    kind="audio",
                    uri=audio.as_uri(),
                    mime_type="audio/wav",
                ),
            ),
        ),
        BlockContext(workspace=tmp_path, timeout_seconds=10.0),
    )

    assert result.status == "success", result.to_dict()
    probe = result.output_artifacts[0].metadata["probe"]
    assert probe["audio_stream_count"] == 1
    assert probe["primary_audio"]["sample_rate_hz"] == sample_rate
    assert probe["duration_seconds"] == pytest.approx(frame_count / sample_rate, rel=0.02)
