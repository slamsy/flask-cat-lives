import random
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    x = Hangman()
    x.guess("p")
    return x.selectWord()

@app.route('/hello')
def hello():
    return str(random.randint(1,5))

class Hangman:

    words = ["youtube","fantastic","test","bowels","alone","mercy"]
    def __init__(self):
        self.guessedLetters = []
        self.word = self.selectWord()
        self.wordLetters = list(self.word)
        self.numberOfGuesses = 6

    def selectWord(self):
        return self.words[random.randint(0,len(self.words)-1)]

    def guess(self,letter):
        self.guessedLetters.append(letter)
        self.guessedLetters.sort()
        self.numberofGuesses = self.numberOfGuesses - 1
        self.checkForWin()

    def checkForWin(self):
        return 1
