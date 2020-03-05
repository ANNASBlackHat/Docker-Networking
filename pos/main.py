import requests
from flask import Flask
app = Flask(__name__)

@app.route('/who')
def who():
    return 'Hey this is POS api running inside docker!'

@app.route('/ping')
def ping():
    r = requests.get('http://messager:5000/who')
    return 'resutl ping by POS : '+r.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
