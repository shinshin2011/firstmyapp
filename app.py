from flask import Flask, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/action')
def act():
    global text_jp
    text1 = 'Hello'
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("話しして下さい。")
            audio = r.listen(source)
            
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
    return render_template("index.html",myresult = text_jp)
if (__name__) == "__main__":
    app.run(host='0.0.0.0')
