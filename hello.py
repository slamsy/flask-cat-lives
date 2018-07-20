import random
from flask import Flask
from flask import render_template
from flask import session,json
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    hangman = Hangman()
    session['hangman'] = hangman.serialize()
    #return hangman.serialize()
    return render_template('hello.html',letters=hangman.answer)

@app.route('/rest')
def rest():
    return render_template('hello.html', letters=['a','s','d',''])

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/<letter>')
def guess(letter):
    hangman = Hangman(session['hangman'])
    hangman.guess(letter)
    #hangman = json.loads(session['hangman'])
    #return json.dumps(hangman)
    return hangman.serialize()
    #hangman = session['hangman']
    return render_template('hello.html',letters=hangman.answer)

class Hangman:

    words = ["youtube","fantastic","test","bowels","alone","mercy"]
    def __init__(self,data=None):
        if data is None:
            self.guessedLetters = []
            self.word = self.selectWord()
            self.wordLetters = list(self.word)
            self.wordLettersRemaining = list(set(self.wordLetters))
            self.answer = [''] * len(self.wordLetters)
            self.numberOfGuesses = 6
        else:
            self.unserialize(data)

    def serialize(self):
        return json.dumps(self.__dict__)

    def unserialize(self,data):
        data = json.loads(data)
        for key, value in data.items():
            setattr(self,key,value)

    def selectWord(self):
        return self.words[random.randint(0,len(self.words)-1)]

    def guess(self,letter):
        self.checkIfGuessed(letter) #moved to top
        self.guessedLetters.append(letter)
        self.guessedLetters.sort() #why?
        self.checkIfCorrect(letter)
        self.fillInTheBlanks(letter)
        self.checkForWin()
        self.checkForLoss(letter)

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
    
    def checkForLoss(self, input):
        if self.checkIfCorrect() == False:
            self.numberofGuesses = self.numberOfGuesses - 1
        if self.numberOfGuesses == 0:
            return False #Mourning ASCII
