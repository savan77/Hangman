#Desc : Popular Hangman Game Using Python.
#Author : Savan Visalpara

import random


#whether user has guessed a word correctly or not.
def isWordGuessed(secretWord, lettersGuessed):
    
    for char in secretWord:
        if not(char in lettersGuessed):
            return False  
    return True

#returns a string Ex. - ( a_ e_ _ ) (To show correct guesses in original word)
def getGuessedWord(secretWord,lettersGuessed):
    list2=[]
    for char in secretWord:
        if char in lettersGuessed:
            list2.append(char)
        else:
            list2.append('_ ')
    str1=''.join(list2)
    return str1    


#Which letters are avilable to user to guess from.
def getAvailableLetters(lettersGuessed):
    #letters will be a string, containing all alphabets in lowercase.
    import string
    letters=string.ascii_lowercase

    AvailableLetters=''
    for char in letters:
        avail_char=''
        if not (char in lettersGuessed):
            avail_char=char
        AvailableLetters+=avail_char
    return AvailableLetters


def hangman(secretWord):
    
    #welcome message to user.
    print 'Welcome to the game Hangman!'
    print 'I am thinking of a word that is',len(secretWord) ,'letters long.'
    print '-----------'
    
    #Maximum number of guesses...(it may be vary as per requirement)
    guesses=8
    lettersGuessed=[]

    #run a loop until guesses is zero or word has been guessed correctly.
    while(guesses>0 and not isWordGuessed(secretWord,lettersGuessed)):
        print 'You have',guesses,'guesses left'
        print 'Available letters:',getAvailableLetters(lettersGuessed)
        g=raw_input("Please guess a letter: ")
        g=g.lower()
        
        #checking - whether letter is already used to guess or not.
        if g in lettersGuessed:
            print "Oops! You've already guessed that letter:",guessed
        else:
            lettersGuessed.append(g)
            guessed=getGuessedWord(secretWord,lettersGuessed)
            if g in secretWord:
                print 'Good guess:',guessed
            else:
                guesses-=1
                print 'Oops! That letter is not in my word:',guessed
        
        print '-----------'

    #checking - whether word is being guessed or not.
    if(isWordGuessed(secretWord,lettersGuessed)):
        print 'Congratulations, you won!'
    else:
        print 'Sorry you ran out of guesses. The word was',secretWord
        print ''



files=open('words.txt','r')

#storing each word of words.txt to list named words.
data=files.read()
words=data.split()

#generating random numbers from words.txt
secretWord=random.choice(words)

#calling hangman function for further process.
hangman(secretWord)
