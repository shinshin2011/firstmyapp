import googletrans
from googletrans import Translator
from datetime import date, datetime
import speech_recognition as sr
from gtts import gTTS
import playsound
import time
import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/action')
def act():
    print("Hello")
    global text_jp
    print(googletrans.LANGUAGES)
    text1 = 'Hello'
    now = datetime.now()
    print("now =", now)
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("話しして下さい。")
            tts = gTTS(text="お話しして下さい。", lang='ja')
            tts.save(f'./d.mp3')
            playsound.playsound(f'./d.mp3', True)
            audio = r.listen(source)
            os.remove(f'./d.mp3')
        try:
            # Google Web Speech APIで音声認識
            text_jp = r.recognize_google(audio, language="ja-JP")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                  " {0}".format(e))
        else:
            print(text_jp)

        time.sleep(0.5)
        break
    print("完了。")

    text2 = text_jp
    translator = googletrans.Translator()
    text_result = translator.translate(text2, src='auto', dest='th')
    tts = gTTS(text=text_result.text, lang='th')
    tts.save(f'./s.mp3')
    playsound.playsound(f'./s.mp3', True)
    print(text_result.text)
    os.remove(f'./s.mp3')
    return render_template("index.html",myresult = text_result.text)
@app.route('/Thai')
def Thai_action():
    print("Hello")
    global text_jp
    print(googletrans.LANGUAGES)
    text1 = 'Hello'
    now = datetime.now()
    print("now =", now)
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("พูดอะไรหน่อย")
            tts = gTTS(text="พูดอะไรหน่อย", lang='th')
            tts.save(f'./d.mp3')
            playsound.playsound(f'./d.mp3', True)
            audio = r.listen(source)
            os.remove(f'./d.mp3')
        try:
            # Google Web Speech APIで音声認識
            text_jp = r.recognize_google(audio, language="th")
        except sr.UnknownValueError:
            print("Google Web Speech APIは音声を認識できませんでした。")
        except sr.RequestError as e:
            print("GoogleWeb Speech APIに音声認識を要求できませんでした;"
                  " {0}".format(e))
        else:
            print(text_jp)

        time.sleep(0.5)
        break
    print("finished")

    text2 = text_jp
    translator = googletrans.Translator()
    text_result = translator.translate(text2, src='auto', dest='ja')
    tts = gTTS(text=text_result.text, lang='ja')
    tts.save(f'./s.mp3')
    playsound.playsound(f'./s.mp3', True)
    print(text_result.text)
    os.remove(f'./s.mp3')
    return render_template("translate.html",myresult = text_result.text)
if (__name__) == "__main__":
    app.run(host='0.0.0.0')
