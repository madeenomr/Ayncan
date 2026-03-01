import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from processing.extract_audio import extract_audio
from processing.remove_music import remove_music
from processing.merge_audio_video import merge_audio_video

def process_video(video_path):

    print("1) Extracting audio...")
    audio_path = "audio.wav"
    extract_audio(video_path, audio_path)

    print("2) Removing music...")
    separated_dir = remove_music(audio_path)

    vocals_path = os.path.join(
        separated_dir, "htdemucs", "audio", "vocals.wav"
    )

    if not os.path.exists(vocals_path):
        raise FileNotFoundError("Vocals file not generated")

    print("3) Merging clean audio with video...")
    output_video = "final.mp4"
    merge_audio_video(video_path, vocals_path, output_video)

    print("Done successfully")
    return output_video


if __name__ == "__main__":
    video = "input.mp4"

    if not os.path.exists(video):
        print("Please put input.mp4 next to main.py")
        sys.exit(1)

    process_video(video)
