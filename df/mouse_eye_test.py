import deeplabcut
from pathlib import Path

def mouse_eye_test(video_paths: list[Path], project_name: str, project_directory: str):
    scorer = "scorer"
    pretrained_model = "mouse_pupil_vclose"

    deeplabcut.create_pretrained_project(
        project_name,
        scorer,
        [str(video_path) for video_path in video_paths],
        model=pretrained_model,
        working_directory=project_directory,
        copy_videos=True,
        videotype=".mp4",
        analyzevideo=True,
        filtered=False,
        createlabeledvideo=True,
        trainFraction=None,
        engine=deeplabcut.Engine.TF,
    )


if __name__ == "__main__":
    folder_path = Path("/Users/philipqueen/mouse_eye_test/clipped_videos/")
    video_paths = sorted(list(folder_path.glob("*.mp4")))

    project_name = "mouse_pupil_vclose_test"
    directory = folder_path.parent / project_name
    directory.mkdir(exist_ok=True)
    mouse_eye_test(video_paths=video_paths, project_name=project_name, project_directory=str(directory))
