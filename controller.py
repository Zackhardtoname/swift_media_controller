
from pynput.keyboard import Key, Listener, Controller
import subprocess

keyboard = Controller()


def tap(key):
    keyboard.press(key)
    keyboard.release(key)


def is_sound_playing():
    res = subprocess.getoutput("pacmd list-sink-inputs | grep -c 'state: RUNNING'")
    # print(res)
    return "0" != res


def on_press(key):
    print('{0} pressed'.format(key))
    # sound_playing = is_sound_playing()
    if key != Key.pause and sound_playing:
        keyboard.tap(Key.pause)


def on_release(key):
    # print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
