import random
from flask import Flask
from flask import render_template
from flask import session,json
from flask import request
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    letter = request.args.get('guess')
    if letter and 'catlives' in session:
        catlives = Catlives(session['catlives'])
        catlives.guess(letter)
    else:
        catlives = Catlives()
    session['catlives'] = catlives.serialize()
    #return catlives.serialize()
    return render_template('catlives.html',letters=catlives.answer, guess=catlives.guessedLetter, isCorrect=catlives.CorrectorIncorrect, wrongLetters=''.join(catlives.wrongLetters), alreadyGuessed=catlives.alreadyGuessed, guesses=catlives.numberOfGuesses, win=catlives.hasWon, loss=catlives.hasLost, word=catlives.word)

@app.route('/rs')
def reset():
    session.clear()
    return "session reset"

class Catlives:

    def __init__(self,data=None):
        if data is None:
            self.guessedLetter = ""
            self.guessedLetters = []
            self.wrongLetters = []
            self.word = self.selectWord()
            self.wordLetters = list(self.word)
            self.wordLettersRemaining = list(set(self.wordLetters))
            self.answer = [''] * len(self.wordLetters)
            self.numberOfGuesses = 9
            self.CorrectorIncorrect = True
            self.alreadyGuessed = False
            self.hasWon = False
            self.hasLost = False
            self.fillPunctuation()
        else:
            self.unserialize(data)

    def loadDictionary(self):
        with open('yv_phrase_dict.txt') as dictionary:
            word = dictionary.read().split("\n")
        return word

    def serialize(self):
        return json.dumps(self.__dict__)

    def unserialize(self,data):
        data = json.loads(data)
        for key, value in data.items():
            setattr(self,key,value)

    def selectWord(self):
        word = self.loadDictionary()
        return word[random.randint(0,len(word)-1)]

    def guess(self,letter):
        self.guessedLetter = letter
        self.alreadyGuessed = self.checkIfGuessed(input=letter)
        if self.alreadyGuessed == True:
            return True
        self.guessedLetters.append(letter)
        self.guessedLetters.sort()
        self.CorrectorIncorrect = self.checkIfCorrect(letter)
        if not self.CorrectorIncorrect:
            self.wrongLetters.append(letter)
        self.fillInTheBlanks(letter)
        self.hasWon = self.checkForWin()
        self.hasLost = self.checkForLoss()

    def checkIfGuessed(self,input):
        for guessedLetter in self.guessedLetters:
            if input == guessedLetter:
                return True

    def checkIfCorrect(self,input):
        isCorrect = False
        if input in self.wordLetters:
            self.wordLettersRemaining.remove(input)
            isCorrect = True
        else:
            isCorrect = False
        return isCorrect

    def fillPunctuation(self):
        index=0
        while index < len(self.wordLettersRemaining):
            if not self.wordLettersRemaining[index].isalpha():
                self.fillInTheBlanks(self.wordLettersRemaining[index])
                self.wordLettersRemaining.remove(self.wordLettersRemaining[index])
            index += 1

    def fillInTheBlanks(self,input):
        index=0
        while index < len(self.wordLetters):
            if input == self.wordLetters[index]:
                self.answer[index] = input
            index += 1

    def checkForWin(self):
        if len(self.wordLettersRemaining) == 0:
            return True

    def checkForLoss(self):
        if self.CorrectorIncorrect == False:
            self.numberOfGuesses = self.numberOfGuesses - 1
            if self.numberOfGuesses == 0:
                return True
            return False
