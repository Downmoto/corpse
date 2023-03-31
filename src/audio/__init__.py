import wave
import sys
import pyaudio
from pathlib import Path


class Recorder:
    def __init__(self,
                 chunk: int = 1024,
                 record_channels: int = 1 if sys.platform == 'darwin' else 2,
                 record_format: int = pyaudio.paInt16,
                 rate: int = 44100,
                 filename: Path = Path('output')) -> None:
        self.CHUNK: int = chunk
        self.FORMAT: int = record_format
        self.CHANNELS: int = record_channels
        self.RATE: int = rate
        self.recording = False
        self.p = pyaudio.PyAudio()
        
        self.filename: Path = filename

    def start(self):
        if not self.recording:
            self.wf = wave.open(str(self.filename), 'wb')
            self.wf.setnchannels(self.CHANNELS)
            self.wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
            self.wf.setframerate(self.RATE)
            
            def callback(in_data, frame_count, time_info, status):
                #file write should be able to keep up with audio data stream (about 1378 Kbps)
                self.wf.writeframes(in_data) 
                return (in_data, pyaudio.paContinue)
            
            self.stream = self.p.open(format = self.FORMAT,
                                       channels = self.CHANNELS,
                                       rate = self.RATE,
                                       input = True,
                                       stream_callback = callback)
            self.stream.start_stream()
            self.recording = True
                
    def stop(self):
        if self.recording:
            self.stream.stop_stream()
            self.stream.close()
            self.wf.close()
            
            self.recording = False
            
            
class Player:
    def __init__(self) -> None:
        pass
            