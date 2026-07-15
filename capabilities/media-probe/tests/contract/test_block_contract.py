from pathlib import Path

from peos_media_probe import ArtifactRef, BlockContext, BlockRequest, MediaProbeBlock


class FakeProvider:
    provider_id = "ffprobe"

    def probe(self, path: Path, timeout_seconds: float) -> dict[str, object]:
        assert path.name == "sample.bin"
        assert timeout_seconds == 5.0
        return {
            "duration_seconds": 1.25,
            "size_bytes": path.stat().st_size,
            "stream_count": 1,
            "video_stream_count": 1,
            "audio_stream_count": 0,
            "subtitle_stream_count": 0,
            "primary_video": {"codec_name": "fake"},
            "primary_audio": None,
            "streams": [],
        }


def test_success_result_envelope(tmp_path: Path) -> None:
    media = tmp_path / "sample.bin"
    media.write_bytes(b"probe-me")

    block = MediaProbeBlock(provider=FakeProvider())
    result = block.run(
        BlockRequest(
            request_id="req-1",
            input_artifacts=(
                ArtifactRef(
                    artifact_id="art-1",
                    kind="media",
                    uri=media.as_uri(),
                    metadata={"source": "fixture"},
                ),
            ),
            idempotency_key="idem-1",
        ),
        BlockContext(workspace=tmp_path, timeout_seconds=5.0),
    )

    payload = result.to_dict()
    assert payload["status"] == "success"
    assert payload["error"] is None
    assert payload["metadata"]["block_id"] == "media.probe"
    assert payload["metadata"]["block_version"] == "0.1.0"
    assert payload["output_artifacts"][0]["metadata"]["source"] == "fixture"
    assert payload["output_artifacts"][0]["metadata"]["probe"]["duration_seconds"] == 1.25
    assert "No audio stream was detected." in payload["warnings"]


def test_rejects_input_outside_workspace(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    workspace.mkdir()
    outside = tmp_path / "outside.bin"
    outside.write_bytes(b"x")

    result = MediaProbeBlock(provider=FakeProvider()).run(
        BlockRequest(
            request_id="req-2",
            input_artifacts=(
                ArtifactRef(
                    artifact_id="art-2",
                    kind="media",
                    uri=outside.as_uri(),
                ),
            ),
        ),
        BlockContext(workspace=workspace),
    )

    assert result.status == "failed"
    assert result.error is not None
    assert result.error.code == "input_outside_workspace"
