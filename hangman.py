# Hangman game

import random, string

HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

words = 'cat dog crazy monkey quantum light python speed strike aircraft shuttle google doodle'.split()

def chooseRandomWord(words):
    return random.choice(words)

def guessLetter(alreadyGuessedLetter):
    """ Asks the user to input a letter."""
    print ('Guess a letter')
    while True:
        guessLetter = raw_input().lower()
        if len(guessLetter)!=1:
            print ('Please Enter a sinle Letter')
        elif guessLetter not in string.ascii_lowercase:
            print ('Please Enter a LETTER')
        elif guessLetter in alreadyGuessedLetter:
            print ('You have already guessed this letter. Choose again.')
        else:
            return guessLetter

def display(word, misGuessedLetter, correctGuessedLetter):
    print (HANGMAN[len(misGuessedLetter)])
    print ('')
    progress = ''
    for letter in word:
        if letter in correctGuessedLetter:
            progress += letter
        else:
            progress += "-"
    print (progress)
    if misGuessedLetter: print ("*{0:s}*".format(misGuessedLetter))
    
def playAgain():
    print ('Do you want to play again? (yes or No)')
    answer = raw_input().lower()
    return answer.startswith('y')

print ("        PT's   H A N G M A N           \n")
misGuessedLetter = ''
correctGuessedLetter = ''
secretWord = chooseRandomWord(words)
gameIsDone = False

while not gameIsDone:
    display(secretWord, misGuessedLetter, correctGuessedLetter)
    print''
    guess = guessLetter(correctGuessedLetter + misGuessedLetter)
    if guess in secretWord:
        correctGuessedLetter += guess
        foundAllLetters = True
        for letter in secretWord:
            if letter not in correctGuessedLetter:
                foundAllLetters = False
                break
        if foundAllLetters:
            print ("Yeah!! You have correctly guessed the word. The word is '{0:s}'".format(secretWord))
            print ('You Have Won!!!')
            gameIsDone = True
    else:
        misGuessedLetter += guess
        if len(misGuessedLetter) == len(HANGMAN)-1:
            display(secretWord, misGuessedLetter, correctGuessedLetter)
            print ('Sorry! The man is dead!! You have run out of guesses.')
            print ("The correct word was '{0:s}'".format(secretWord))
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            misGuessedLetter = ''
            correctGuessedLetter = ''
            gameIsDone = False
            secretWord = chooseRandomWord(words)
