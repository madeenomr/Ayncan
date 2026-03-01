import torch
import torchaudio
import os

def enhance_audio(input_audio_path, output_audio_path="enhanced.wav"):
    """
    تحسين جودة الصوت باستخدام نموذج بسيط لإزالة الضوضاء
    """
    if not os.path.exists(input_audio_path):
        raise FileNotFoundError("Input audio not found")

    # تحميل الصوت
    waveform, sample_rate = torchaudio.load(input_audio_path)

    # نموذج إزالة الضوضاء بسيط (يمكن تطويره لاحقًا)
    # هنا مثال: normalize الصوت
    waveform = waveform / waveform.abs().max()

    # حفظ الملف المحسن
    torchaudio.save(output_audio_path, waveform, sample_rate)

    return output_audio_path


if __name__ == "__main__":
    enhance_audio("vocals.wav")
    print("Audio enhanced successfully")
