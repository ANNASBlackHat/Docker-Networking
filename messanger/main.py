import requests
from flask import Flask
app = Flask(__name__)

@app.route('/who')
def who():
    return 'Hey this is Messager api running inside docker!'

@app.route('/call')
def ping():
    r = requests.get('http://pos/who')
    return r.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
