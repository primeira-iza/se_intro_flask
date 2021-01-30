from flask import Flask
from flask import request
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

# http://127.0.0.1:5000/oblicz?l1=10&l2=20&op=plus
@app.route('/oblicz')
def oblicz():
    l1_arg = request.args.get('l1')
    if l1_args is None:
        return 'brak argumentu l1'
    l1 = int(l1_arg)

    l2_arg = request.args.get('l2')
    l2 = int(l2_arg)
    op = request.args.get('op')
    if op == 'plus':
        s = l1 + l2
        return f'{s}'
    return ""
