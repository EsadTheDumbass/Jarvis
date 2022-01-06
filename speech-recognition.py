import speech_recognition
import speech_recognition as sr
from gtts import gTTS
# import Os module to start the audio file
import os
from time import time,ctime
t = time()
language = 'tr'

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything :")
    while True:
        audio = r.listen(source)
        text = r.recognize_google(audio)
        print('You just said {}'.format(text))
        try:
            if text == 'Jarvis':
                mytext = f'Hizmetinizdeyim.'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("output.mp3")
                os.system("start output.mp3")
            else:
                mytext = f'Efendim? Sizi duyamadim.'
                myobj = gTTS(text=mytext, lang=language, slow=False)
                myobj.save("output.mp3")
                os.system("start output.mp3")
        except speech_recognition.UnknownValueError:
            mytext = f'Efendim? Sizi duyamadim.'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("output.mp3")
            os.system("start output.mp3")



# Language we want to use




