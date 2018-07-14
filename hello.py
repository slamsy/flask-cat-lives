from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    x = Hangman()
    return x.f()

@app.route('/hello')
def hello():
    return 'Hello, World'

class Hangman:

    i=12345

    def f(self):
        return 'boo'
