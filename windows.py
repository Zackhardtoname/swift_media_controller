import numpy as np
import sounddevice as sd


def is_sound_playing_windows():
    duration = 1000  # in seconds
    recording = sd.rec(int(duration), channels=2, blocking=True)
    volume_norm = np.linalg.norm(recording) * 10
    res = int(volume_norm)
    # print("res", res >= 3)
    return res >= 3


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("|" * int(volume_norm))


if __name__ == '__main__':
    with sd.Stream(callback=print_sound):
        sd.sleep(100000)
