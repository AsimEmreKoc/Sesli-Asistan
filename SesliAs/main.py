import speech_recognition as sr
import pyaudio
from bs4 import BeautifulSoup
from datetime import datetime
import webbrowser
import time
from gtts import gTTS
from playsound import playsound
import random
import os
import wikipedia
import requests

r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio, language='tr-TR')
        except sr.UnknownValueError:
            print('anlayamadım')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return voice

def response(voice):
    if 'nasılsın' in voice or "ne haber" in voice:
        speak('iyi senden')

    if 'saat kaç' in voice:
        speak(datetime.now().strftime('%H:%M'))

    if 'arama yap' in voice:
        Search = record('ne aramak istersin')
        url = 'https://google.com/search?q='+Search
        webbrowser.get().open(url)
        speak(Search+' için bulduklarım')

    if 'tamamdır' in voice or "görüşürüz" in voice:
        speak('görüşürüz')
        exit()

    if "İnterneti aç" in voice:
        url = "https://www.google.com/"
        speak('hemen açıyorum')
        webbrowser.get().open(url)


    if "YouTube'u aç" in voice or "YouTube aç" in voice:
        url = 'https://www.youtube.com/'
        speak('hemen açıyorum')
        webbrowser.get().open(url)

    if "yutup aç" in voice or "yutupu aç" in voice:
        url = 'https://www.youtube.com/'
        speak('hemen açıyorum')
        webbrowser.get().open(url)

    if "Twitch'i aç" in voice or "Twitch aç" in voice or "mor site" in voice:
        url = "https://www.twitch.tv/"
        speak('hemen açıyorum')

        webbrowser.get().open(url)

    if "YouTube'da arat" in voice or "YouTube'da ara" in voice:
        search = record("YouTube'da ne aramak istersin")
        url ='https://www.youtube.com/results?search_query='+search
        webbrowser.get().open(url)
        speak(search+'için bulduklarım')

    if "araştır" in voice:
        search = record("ne araştırıcaksın")
        url = 'https://tr.wikipedia.org/wiki/'+search
        webbrowser.get().open(url)
        wikipedia.set_lang("tr")
        try:
            arama = wikipedia.summary(search,sentences=2)
            print(arama)
            speak(arama)
        except:
            speak('bulamadım')


    if "uygulama aç" in voice or "Uygulama aç" in voice:
        speak('Hangi uygulamayı açmak istiyorsun')
        runApp = record()
        runApp = runApp.lower()
        print(runApp)
        if 'valorant' in runApp:
            os.startfile('C:\Riot Games\Riot Client\RiotClientServices.exe')
            speak('istediğin uygulamayı açıyorum')
        elif 'paladins' in runApp:
            os.startfile('steam://rungameid/444090')
            speak('istediğin uygulamayı açıyorum')
        elif 'tır oyunu' in runApp:
            os.startfile('steam://rungameid/227300')
            speak('istediğin uygulamayı açıyorum')
        elif 'lol' in runApp:
            os.startfile('C:\Riot Games\Riot Client\RiotClientServices.exe')
            speak('istediğin uygulamayı açıyorum')
        elif 'zoom' in runApp:
            os.startfile('C:\\Users\\Pc\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe')
            speak('istediğin uygulamayı açıyorum')
        else:
            speak('açmak istediğin uygulama listemde yok')

    if "Hangi gündeyiz" in voice or "Bugün günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

        speak(today)


def speak(string):
    tts = gTTS(string, lang='tr')
    rand = random.randint(1,10000)
    file= 'audio-'+str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)

def test(voice):
    if "emre" in  voice or "Emre" in voice:
        speak('efendim')
        voice = record()
        print(voice.capitalize())
        response(voice)

time.sleep(1)
while 1:
    voice = record()
    print(voice)
    test(voice)
