import random
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    x = Hangman()
    x.guess("p")
    return x.selectWord()

@app.route('/rest')
def rest():
    return render_template('hello.html', letters=['a','s','d',''])

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/<letter>')
def guess(letter):
    return len(letter)

class Hangman:

    words = ["youtube","fantastic","test","bowels","alone","mercy"]
    def __init__(self):
        self.guessedLetters = []
        self.word = self.selectWord()
        self.wordLetters = list(self.word)
        self.wordLettersRemaining = set(self.wordLetters)
        self.answer = [''] * len(self.wordLetters)
        self.numberOfGuesses = 6

    def selectWord(self):
        return self.words[random.randint(0,len(self.words)-1)]

    def guess(self,letter):
        self.checkIfGuessed() #moved to top
        self.guessedLetters.append(letter)
        self.guessedLetters.sort() #why?
        self.checkIfCorrect()
        self.fillInTheBlanks()
        self.checkForWin()
        self.checkForLoss()

    def checkIfGuessed(self,input):
        for guessedLetter in self.guessedLetters:
            if input == guessedLetter: 
                return True #warning message
            
    def checkIfCorrect(self,input): 
        if input in self.wordLetters:
            self.wordLettersRemaining.remove(input)
            return True

    def fillInTheBlanks(self,input):
        index=0
        while index < len(self.wordLetters):
            if input == self.wordLetters[index]:
                self.answer[index] = input
            index += 1

    def checkForWin(self):
        if len(self.wordLettersRemaining) == 0:
            return True #Celebratory ASCII
    
    def checkForLoss(self):
        if self.checkIfCorrect() == False:
            self.numberofGuesses = self.numberOfGuesses - 1
        if self.numberOfGuesses == 0:
            return False #Mourning ASCII