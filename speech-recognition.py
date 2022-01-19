from urllib.request import urlopen
from requests import Request, Session
import requests
from speech_recognition import UnknownValueError
import speech_recognition as sr
from gtts import gTTS
import json
import urllib
from urllib import *
import os
import pprint
from time import time,ctime
t = time()
import pyttsx3
engine = pyttsx3.init()
newsAPI = 'TOKEN'
language = 'tr'
commands = ['news']
r = sr.Recognizer()
session = Session()

with sr.Microphone() as source:
    print("Speak Anything :")
    engine.setProperty('voice', 64)
    audio = r.listen(source)
    text = r.recognize_google(audio, language='tr-TR')
    print('You just said {}'.format(text))
    try:
        news_url = f'https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey={newsAPI}'
        if ('Jarvis' or 'jarvis' in text) and ('Haberler' or 'haberler' in text):
            response = session.get(news_url)
            data = json.loads(response.text)
            for x in range(1,9):
                engine.say(data['articles'][x]['title'])
                engine.runAndWait()
            #if command not in commands:
        else:
            engine.say("I could not understand you sir.", language)
            engine.runAndWait()
    except UnknownValueError:
        engine.say("I could not understand sorry.")
        engine.runAndWait()


# Language we want to use




