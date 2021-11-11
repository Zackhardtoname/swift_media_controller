from pynput.keyboard import Key, Listener, Controller, KeyCode
from windows import is_sound_playing_windows
from linux import is_sound_playing_linux
import os


def get_system_name():
    if os.name == 'nt':
        return "win"

    return "linux"


system_name = get_system_name()
keycode = KeyCode()
keyboard = Controller()

if system_name == "win":
    stop_key = keycode.from_vk(178)
else:
    stop_key = keycode.from_vk(269025045)
excluded_keys = {stop_key, Key.left, Key.right, Key.space, Key.enter}

# personalize
excluded_keys.add(keycode.from_char('f'))


def tap(key):
    keyboard.press(key)
    keyboard.release(key)


def on_press(key):
    print('{0} pressed'.format(key))
    if system_name == "win":
        sound_playing = is_sound_playing_windows()
        # print(sound_playing)
    else:
        sound_playing = is_sound_playing_linux()
    # print("sound_playing", sound_playing)
    if key not in excluded_keys and sound_playing:
        tap(stop_key)


def on_release(key):
    # print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        pass
        # return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
