import numpy as np
import sounddevice as sd


def is_sound_playing_windows():
    duration = 1000  # in seconds
    recording = sd.rec(int(duration), channels=2, blocking=True)
    volume_norm = np.linalg.norm(recording) * 10
    res = int(volume_norm)
    # print("res", res >= 3)
    return res >= 3
