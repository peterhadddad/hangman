import time
import random
import math
import string
name=input("Enter your name: ")
print("Good Luck! " + name+'\n')
time.sleep(1)
print("************************")
print("--------HANGMAN---------")
print("************************")
print(" ")

string='-'
global chances
chances=5
alphabet=[]
wordsAvailable=["lucky","galaxy","cat","dog","matrix","nightclub","star","travel"]


def findWord(tableWord):
    length=len(tableWord)
    randomWord=tableWord[math.floor(random.random()*length)]
    return randomWord

def alphabetGenerator(alphabet,string):
    start = ord(string)
    for i in range(26):
        alphabet.append(chr(start + i))
    return alphabet

def splitString(table):
    stringSplit=[]
    for i in range(len(table)):
        stringSplit.append(table[i])
    return stringSplit

def switchString(stringMystery,letter,word):

    stringTable=splitString(stringMystery)
    for i in range(len(word)):
        if letter== word[i]:
            stringTable.remove(stringTable[i])
            stringTable.insert(i,letter)

    stringJoin=''.join(stringTable)
    stringMystery = stringJoin
    return stringMystery


def hangMan(chances, word):
    if chances == 4:
        time.sleep(1)
        print("   _____ \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(chances) + " guesses remaining\n")
    if chances == 3:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(chances) + " guesses remaining\n")

    if chances == 2:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |      \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(chances) + " guesses remaining\n")

    if chances == 1:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |      \n"
              "  |      \n"
              "__|__\n")
        print("Wrong guess. " + str(chances) + " guesses remaining\n")

    if chances == 0:
        time.sleep(1)
        print("   _____ \n"
              "  |     | \n"
              "  |     |\n"
              "  |     | \n"
              "  |     O \n"
              "  |    /|\ \n"
              "  |    / \ \n"
              "__|__\n")
        print("Wrong guess. You are hanged!!!\n")
        print("The word was: " + word)

def game():
    global chances
    chosenWord = findWord(wordsAvailable)
    wordString = string * len(chosenWord)
    alphabetGenerator(alphabet, 'a')

    while (chances > 0):
        letter = input("Choose a letter: ")
        if letter in alphabet:
            if letter in chosenWord:

                wordString = switchString(wordString, letter, chosenWord)

                print("Great Job!")
                print(" ")
                print(wordString)

                alphabet.remove(letter)

                if wordString == chosenWord:
                    time.sleep(1)
                    print("************************")
                    print("YOU DID IT \n")
                    time.sleep(1)
                    print("GOODBYE! \n")
                    break


            else:
                chances -= 1
                hangMan(chances, chosenWord)
                if chances == 0:
                    break
        else:
            print("Choose a tiny letter")


game()
