from typing import Union

import wave
import sys
import pyaudio
from pathlib import Path


class Audio:
    """
    Audio class


    """

    def __init__(self,
                 chunk: int = 1024,
                 channels: int = 1 if sys.platform == 'darwin' else 2,
                 format: Union[int, float] = pyaudio.paInt16,
                 rate: int = 44100) -> None:
        self.CHUNK: int = chunk
        self.FORMAT: Union[int, float] = format
        self.CHANNELS: int = channels
        self.RATE: int = rate

    def play(self, file: Path):
        """
        Play method
        
        """
        
        with wave.open(str(file), 'rb') as wf:
            p = pyaudio.PyAudio()
            
            stream = p.open(
                format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True
            )
            
            while len(data := wf.readframes(self.CHUNK)):
                stream.write(data)
                
            stream.close()
            p.terminate()
            
            

    def record(self):
        pass
