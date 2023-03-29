import wave
import sys

import pyaudio


class Audio:
    def __init__(self,
                 chunk=1024,
                 channels=1 if sys.platform == 'darwin' else 2,
                 _format=pyaudio.paInt16,
                 rate=44100) -> None:
        self.CHUNK = chunk
        self.FORMAT = _format
        self.CHANNELS = channels
        self.RATE = rate