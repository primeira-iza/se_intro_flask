from flask import Flask
app = Flask(__name__)

moje_imie = input("What's your name? ")
moje_hobby = input("What's your hobby? ")

@app.route('/')
def hello_world():
    return 'Hello, World ' + moje_imie + ' !'

@app.route('/kto')
def kto():
    return moje_imie


@app.route('/wiadomosc')
def wiadomosc():
    return 'Hello, World!'

@app.route('/hobby')
def wiadomosc():
    return moje_hobby
