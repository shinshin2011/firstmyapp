from flask import Flask, render_template
import requests
from pprint import pprint
app = Flask(__name__)
API_HOST = 'https://api.bitkub.com'
@app.route('/')
def index():
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    sym = 'THB_XRP'
    data = result[sym]
    last = data['last']
    #print(data)
    print(last)
    return render_template("myapp.html", mydata=last)


if (__name__) == "__main__":
    app.run(host='0.0.0.0')
