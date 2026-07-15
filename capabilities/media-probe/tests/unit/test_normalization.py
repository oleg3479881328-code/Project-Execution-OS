from peos_media_probe.providers.ffprobe import (
    normalize_ffprobe_payload,
    parse_fraction,
)


def test_parse_fraction() -> None:
    assert parse_fraction("30000/1001") == 30000 / 1001
    assert parse_fraction("25/1") == 25.0
    assert parse_fraction("0/0") is None
    assert parse_fraction("N/A") is None


def test_normalize_ffprobe_payload() -> None:
    payload = {
        "streams": [
            {
                "index": 0,
                "codec_type": "video",
                "codec_name": "h264",
                "width": 1920,
                "height": 1080,
                "avg_frame_rate": "30000/1001",
                "duration": "12.50",
            },
            {
                "index": 1,
                "codec_type": "audio",
                "codec_name": "aac",
                "sample_rate": "48000",
                "channels": 2,
                "duration": "12.48",
                "tags": {"language": "eng"},
            },
        ],
        "format": {
            "format_name": "mov,mp4,m4a,3gp,3g2,mj2",
            "format_long_name": "QuickTime / MOV",
            "duration": "12.50",
            "size": "123456",
            "bit_rate": "79000",
        },
    }

    result = normalize_ffprobe_payload(payload)

    assert result["duration_seconds"] == 12.5
    assert result["size_bytes"] == 123456
    assert result["video_stream_count"] == 1
    assert result["audio_stream_count"] == 1
    assert result["primary_video"]["width"] == 1920
    assert result["primary_video"]["frame_rate_fps"] == 30000 / 1001
    assert result["primary_audio"]["sample_rate_hz"] == 48000
    assert result["primary_audio"]["language"] == "eng"
