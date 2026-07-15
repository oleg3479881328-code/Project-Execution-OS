from pathlib import Path

from peos_media_probe import ArtifactRef, BlockContext, BlockRequest, create_block

media_path = Path("example.mp4").resolve()
result = create_block().run(
    BlockRequest(
        request_id="example-request",
        input_artifacts=(
            ArtifactRef(
                artifact_id="example-media",
                kind="video",
                uri=media_path.as_uri(),
            ),
        ),
    ),
    BlockContext(workspace=media_path.parent),
)
print(result.to_dict())
