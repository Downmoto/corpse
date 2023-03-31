from pynput import keyboard
from audio import Recorder


class KeyboardEventListener(keyboard.Listener):
    def __init__(self, r: Recorder, p):
        super().__init__(on_press=self.on_press, on_release=self.on_release)  # type: ignore
        self._r = r
        self._p = p

    def on_press(self, key):
        if key is None:
            pass
        elif isinstance(key, keyboard.Key):
            if key.ctrl:
                self._r.start()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            if key.char == 'q':  # press q to quit
                if self._r.recording:
                    self._r.stop()
                return False  # this is how you stop the listener thread
            if key.char == 'p' and not self._r.recording:
                self._p.start()

    def on_release(self, key):
        if key is None:  # unknown event
            pass
        elif isinstance(key, keyboard.Key):  # special key event
            if key.ctrl:
                self._r.stop()
        elif isinstance(key, keyboard.KeyCode):  # alphanumeric key event
            pass
