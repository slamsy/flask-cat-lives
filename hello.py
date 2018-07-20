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
		self.wordLettersRemaining = set(self.wordLetters)
		self.Answer = []
        self.numberOfGuesses = 6

    def selectWord(self):
        return self.words[random.randint(0,len(self.words)-1)]

    def guess(self,letter):
        self.guessedLetters.append(letter)
        self.guessedLetters.sort()
        self.checkIfGuessed()
        self.checkIfCorrect()
        self.displayAnswer()
        self.checkForWin()
        self.checkForLoss()

	def checkIfGuessed(self,input):
		x = 0
		while x < len(self.guessedLetters)
			if input == self.guessedLetters[x]
				return True #Error
				else x = x + 1
		return False
			
	def checkIfCorrect(self,input):	
		if input in self.wordLetters:
			self.wordLettersRemaining.remove(input)
			return True

	def displayAnswer():
		y = self.wordLetters.index(input)
		if input in self.wordLetters:
			self.Answer.insert(y,input)	

    def checkForWin():
    	if len(self.wordLettersRemaining) == 0
    		return True #Celebratory ASCII
    
    def checkForLoss():
    	if self.checkIfCorrect() == False
        	self.numberofGuesses = self.numberOfGuesses - 1
        if self.numberOfGuesses == 0
        	return False #Mourning ASCII