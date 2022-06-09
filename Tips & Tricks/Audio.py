# Converting Text into Audio
from gtts import gTTS

from playsound import playsound

audio = r'C:\Users\Ankit Singh\Desktop\Programs\panda.mp3'
language = 'en'
sp = gTTS(text="Helo Welcome to your pc ",lang=language,slow=True)
sp.save(audio)
playsound(audio)
