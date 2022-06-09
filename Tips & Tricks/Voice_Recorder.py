# Voice Recorder

import sounddevice
from scipy.io.wavfile import write

fs = 44100          # Sample rate
second = int(input("Enter time duration in seconds: "))

print("Recording.....\n")

record_voice = sounddevice.rec(int(second * fs), samplerate = fs, channels = 2)

sounddevice.wait()

write("Record.wav", fs, record_voice)

print("Finised...\nPlease Check it....")
