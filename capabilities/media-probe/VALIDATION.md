# media.probe Validation Record

## Candidate Validation

Date: 2026-07-15

Status tested: `0.1.0 candidate`

## Environment

```text
Operating environment: Linux container
Python: 3.13.5
pytest: 9.0.2
ffprobe: 7.1.3-0+deb13u1
```

## Installation Command

```bash
python -m pip install -e '.[dev]'
```

Result: success.

## Automated Test Command

```bash
pytest -q
```

Result:

```text
6 passed in 0.30s
```

Coverage exercised:

- ffprobe rational frame-rate parsing;
- normalized video and audio metadata;
- successful capability result envelope;
- preservation of existing artifact metadata;
- workspace boundary rejection;
- structured `ffprobe_not_found` failure;
- real ffprobe execution against a generated WAV fixture.

## Manual CLI Smoke Test

A 0.1-second mono WAV file at 8000 Hz was generated with Python's standard `wave` module.

Command shape:

```bash
peos-media-probe <generated-sample.wav> --pretty
```

Verified result:

```json
{
  "status": "success",
  "block_id": "media.probe",
  "block_version": "0.1.0",
  "duration_seconds": 0.1,
  "sample_rate_hz": 8000,
  "warnings": [
    "No video stream was detected."
  ]
}
```

## GitHub CI

Workflow added:

```text
.github/workflows/media-probe-tests.yml
```

The workflow runs the package tests on Python 3.12 and 3.13 and installs ffmpeg/ffprobe before the real smoke test.

CI status must be checked on the pull request before merge.

## Candidate Conclusion

The evidence is sufficient to promote `media.probe` from `idea` to `candidate`.

It is not sufficient for `validated` because the block has not yet been integrated into a real application workflow.

## Remaining Validation

- run a native Windows smoke test;
- test representative MP4/H.264/AAC input;
- test variable-frame-rate input;
- integrate into one real application workflow;
- confirm the contract remains suitable when `media.clip` becomes the second capability consumer.
