# audio_player.py

class AudioFile:

    def __init__(self, filename):
        if not filename.endswith(self.ext):
            raise Exception("Invalid file format")
        self.filename = filename

class MP3File(AudioFile):
    ext = "mp3"
    def play(self):
        print("playing {} as mp3".format(self.filename))

class WavFile(AudioFile):
    ext = "wav"
    def play(self):
        print("playing {} as wav".format(self.filename))

class OggFile(AudioFile):
    ext = "ogg"
    def play(self):
        print("playing {} as ogg".format(self.filename)) 

class FlacFile:
    def __init__(self, filename):
        if not filename.endswith(".flac"):
            raise Exception("Invalid file format")
        self.filename = filename
    
    def play(self):
        print("playing {} as flac".format(self.filename))

def main():        
    ogg = OggFile("myfile.ogg")
    ogg.play()

    mp3 = MP3File("myfile.mp3")
    mp3.play()

    # not_an_mp3 = MP3File("myfile.ogg") 

    flac = FlacFile("myfile.flac")
    flac.play()

if __name__ == '__main__':
    main()    