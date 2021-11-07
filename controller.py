from pynput.keyboard import Key, Listener, Controller
from windows import is_sound_playing_windows
from linux import is_sound_playing_linux
import os


def get_system_name():
    if os.name == 'nt':
        return "win"

    return "linux"


system_name = get_system_name()
if system_name == "win":
    stop_key = Key.media_play_pause
else:
    stop_key = Key.pause
keyboard = Controller()


def tap(key):
    keyboard.press(key)
    keyboard.release(key)


def on_press(key):
    # print('{0} pressed'.format(key))
    if system_name == "win":
        sound_playing = is_sound_playing_windows()
        # print(sound_playing)
    else:
        sound_playing = is_sound_playing_linux()
    # print("sound_playing", sound_playing)
    if key != stop_key and sound_playing:
        tap(stop_key)


def on_release(key):
    # print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
