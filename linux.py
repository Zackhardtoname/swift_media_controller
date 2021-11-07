import subprocess


def is_sound_playing_linux():
    res = subprocess.getoutput("pacmd list-sink-inputs | grep -c 'state: RUNNING'")
    # print(res)
    return "0" != res
