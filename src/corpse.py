from audio.audio import Audio
from pathlib import Path

def main() -> int:
    audio: Audio = Audio()
    
    file: Path = Path('./output.wav') 
    
    audio.play(file)

    return 0





if __name__ == '__main__':
  main()