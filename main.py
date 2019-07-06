import speech_recognition as sr
import pyaudio

key = "c2a8e03922ce491d9223b767f48d8d2e"



def main():
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 3
    filename = "output.wav"





    print(sr.__version__)
    r = sr.Recognizer()
    harvard = sr.AudioFile('test.flac')
    with harvard as source:
        r.adjust_for_ambient_noise(source)
        audio = r.record(source)
    text = r.recognize_google(audio)
    print(text) 
    



# This line is the starting point of the program.
if __name__ == "__main__":
    main()
