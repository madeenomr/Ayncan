import subprocess
import os

def merge_audio_video(video_path, audio_path, output_path):

    if not os.path.exists(video_path):
        raise FileNotFoundError("Video file not found")

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-i", audio_path,
        "-c:v", "copy",
        "-map", "0:v:0",
        "-map", "1:a:0",
        output_path
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_path


if __name__ == "__main__":
    video = "input.mp4"
    audio = "audio.wav"
    output = "final.mp4"

    merge_audio_video(video, audio, output)
    print("Video created successfully.")
