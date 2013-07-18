# Hangman game

import random

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
    wordIndex = random.randint(0,len(words))
    word = words[wordIndex]
    return word

def guessLetter(alreadyGuessedLetter):
    print 'Guess a letter'
    guessLetter = str(raw_input())
    guessLetter = guessLetter.lower()
    if len(guessLetter)!=1:
        print 'Please Enter a sinle Letter'
    elif guessLetter not in 'abcdefghijklmnopqrstuvwxyz':
        print 'Please Enter a LETTER'
    elif guessLetter in alreadyGuessedLetter:
        print 'You have already guessed this letter. Choose again.'
    else:
        return guessLetter

def display(word, misGuessedLetter, HANGMAN, correctGuessedLetter):
    print HANGMAN[len(misGuessedLetter)]
    print ''
    progress = '_'*len(word)
    for i in range(len(word)):
        if word[i] in correctGuessedLetter:
            progress = progress[:i] + word[i] + progress[i+1:]
    print progress
    
def playAgain():
    print 'Do you want to play again? (yes or no)'
    answer = str(raw_input())
    answer = answer.lower()
    return answer.startswith('y')

print "        PT's   H A N G M A N           "
print ''
misGuessedLetter = ''
correctGuessedLetter = ''
secretWord = chooseRandomWord(words)
gameIsDone = False

while True:
    display(secretWord, misGuessedLetter, HANGMAN, correctGuessedLetter)
    print''
    guess = guessLetter(correctGuessedLetter + misGuessedLetter)
    while guess == None:
        guess = guessLetter(correctGuessedLetter + misGuessedLetter)
    if guess in secretWord:
        correctGuessedLetter = correctGuessedLetter + guess
        foundAllLetters = True
        for i in range(0, len(secretWord)-1):
            if secretWord[i] not in correctGuessedLetter:
                foundAllLetters = False
                break
        if foundAllLetters:
            print "Yeah!! You have correctly guessed the word. The word is '", secretWord,"'"
            print 'You Have Won!!!'
            gameIsDone = True
    else:
        misGuessedLetter = misGuessedLetter + guess
        if len(misGuessedLetter) == len(HANGMAN)-1:
            display(secretWord, misGuessedLetter, HANGMAN, correctGuessedLetter)
            print 'Sorry! The man is dead!! You have run out of guesses.'
            print "The correct word was '", secretWord,"'"
            gameIsDone = True
    if gameIsDone:
        if playAgain():
            misGuessedLetter = ''
            correctGuessedLetter = ''
            gameIsDone = False
            secretWord = chooseRandomWord(words)
        else:
            break
