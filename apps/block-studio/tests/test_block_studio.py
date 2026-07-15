import shutil
import wave
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from peos_block_studio.app import create_app
from peos_block_studio.catalog import build_catalog, parse_registry
from peos_block_studio.storage import ExecutionStorage, sanitize_filename


def repo_root() -> Path:
    return Path(__file__).resolve().parents[3]


def test_registry_and_manifest_build_catalog() -> None:
    rows = parse_registry(repo_root() / "capability-library" / "REGISTRY.md")
    assert any(row["Block ID"] == "media.probe" for row in rows)

    catalog = build_catalog(repo_root())
    probe = next(item for item in catalog if item.block_id == "media.probe")
    assert probe.status == "candidate"
    assert probe.version == "0.1.0"
    assert probe.provider == "ffprobe"
    assert probe.installed is True
    assert probe.interactive is True


def test_health_and_catalog(tmp_path: Path) -> None:
    client = TestClient(create_app(repo_root=repo_root(), runtime_root=tmp_path / "runtime"))
    health = client.get("/api/health")
    assert health.status_code == 200
    assert health.json()["local_only"] is True

    blocks = client.get("/api/blocks")
    assert blocks.status_code == 200
    probe = next(item for item in blocks.json() if item["block_id"] == "media.probe")
    assert probe["interactive"] is True


@pytest.mark.skipif(shutil.which("ffprobe") is None, reason="ffprobe is not installed")
def test_real_media_probe_upload_and_cleanup(tmp_path: Path) -> None:
    audio = tmp_path / "tone.wav"
    sample_rate = 8000
    frame_count = 800
    with wave.open(str(audio), "wb") as wav_file:
        wav_file.setnchannels(1)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        wav_file.writeframes(b"\x00\x00" * frame_count)

    runtime = tmp_path / "runtime"
    client = TestClient(create_app(repo_root=repo_root(), runtime_root=runtime))
    with audio.open("rb") as handle:
        response = client.post(
            "/api/blocks/media.probe/run",
            files={"file": (audio.name, handle, "audio/wav")},
            data={"timeout_seconds": "10"},
        )
    assert response.status_code == 200, response.text
    payload = response.json()
    assert payload["result"]["status"] == "success"
    probe = payload["result"]["output_artifacts"][0]["metadata"]["probe"]
    assert probe["audio_stream_count"] == 1
    assert probe["primary_audio"]["sample_rate_hz"] == sample_rate
    assert probe["duration_seconds"] == pytest.approx(frame_count / sample_rate, rel=0.02)
    assert any(item["level"] == "progress" for item in payload["logs"])

    preview = client.get(payload["preview_url"])
    assert preview.status_code == 200
    assert preview.content.startswith(b"RIFF")

    deleted = client.delete(f"/api/executions/{payload['execution_id']}")
    assert deleted.status_code == 200
    assert deleted.json() == {"deleted": True}
    assert client.get(payload["preview_url"]).status_code == 404


def test_storage_boundaries(tmp_path: Path) -> None:
    assert sanitize_filename("../My Wedding Video (final).mp4") == "My_Wedding_Video_final_.mp4"
    storage = ExecutionStorage(tmp_path / "runtime")
    with pytest.raises(FileNotFoundError):
        storage.resolve_file("../escape")
