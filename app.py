from flask import Flask, render_template
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    text2 = "สวัสดี สบายดีไหม"
    translator = googletrans.Translator()
    text_result = translator.translate(text2, src='auto', dest='ja')
    return render_template("speech.html", myresult = text_result.text))
@app.route('/action')
def act():
    
    return render_template("index.html",myresult = "Testing")
if (__name__) == "__main__":
    app.run(host='0.0.0.0')
