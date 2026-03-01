import subprocess
import os

def extract_audio(video_path, output_audio_path):
    if not os.path.exists(video_path):
        raise FileNotFoundError("Video file not found")

    command = [
        "ffmpeg",
        "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "44100",
        "-ac", "2",
        output_audio_path
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_audio_path


if __name__ == "__main__":
    video = "input.mp4"
    output = "audio.wav"
    extract_audio(video, output)
    print("Audio extracted successfully.")
