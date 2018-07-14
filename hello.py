import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    x = Hangman()
    return x.f()

@app.route('/hello')
def hello():
    return str(random.randint(1,5))

class Hangman:

    i=12345
    words = ["youtube","fantastic","test","bowels","alone","mercy"]

    def f(self):
        return self.words[random.randint(0,len(self.words)-1)]

