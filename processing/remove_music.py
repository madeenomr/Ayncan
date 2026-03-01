import subprocess
import os

def remove_music(audio_path, output_dir="separated"):

    if not os.path.exists(audio_path):
        raise FileNotFoundError("Audio file not found")

    os.makedirs(output_dir, exist_ok=True)

    command = [
        "demucs",
        "-n", "htdemucs",
        "--two-stems", "vocals",
        audio_path,
        "-o", output_dir
    ]

    subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    return output_dir


if __name__ == "__main__":
    audio = "audio.wav"
    remove_music(audio)
    print("Music removed successfully")
