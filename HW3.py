# Created on Aug 8, 2019
# @author: Yuliya_Naychuk

import sys
import re
import operator

NO_GUESSES = "I don't know any word of a given length..."
ONE_MORE_TRY = 'Would you like to play one more time? (y/n): '
YES = 'Y'
BYE = 'Bye, see you next time! :)'
WELCOME ='Welcome to a Guessing Word Game!'
THINK_A_WORD = "Think of a word and enter it's length: "
POSITIONS_OF_AVAILABLE_LETTERS ='\n If letter(s): "{}" is available in the hidden word, \n please enter comma separated position(s) counting from 0, \n or just press Enter if the letter is absent: '
EMPTY_STRING = ''
COMMA = ','
DOT = '.'
GUESSED_WORD = 'I guess the hidden word is: "{}"'
CANT_GUESS = "You won! Can't guess the word matching specified letters"
NO_TRIES_LEFT = "No more tries left, so you're probably cheating!"
PATH_TO_DATABASE = 'D:\Python\hangman_list\hangman_list.txt'

def searchWords(textFile):
    text = re.findall (r'\w+', textFile.read().lower())
    return text   

def splitWord(word): 
    return [char for char in word]

def sumFreq(d):
    sumFreq = 0
    for key in d:
        sumFreq += d[key]
    return sumFreq
        
def searchUniqueWords(inputList,givenWordLength):       
    listSet = set(inputList) 
    uniqueWordsList = sorted(list(listSet))
    possibleWordsMatchedReg = [el.lower() for el in uniqueWordsList if len(el) == givenWordLength] 
    if possibleWordsMatchedReg==[]:
        print (NO_GUESSES)
        newGame()
    else:
        return possibleWordsMatchedReg

def getCharFrequency(wordSubset):
    wordsString = EMPTY_STRING.join(wordSubset)
    result = {}
    freq = {}
    sumFreqChars =0
    for char in wordsString:
        try:
            result[char] +=1  # If char already in result dictionary, increase its count
            sumFreqChars +=1                    
        except KeyError:
            result[char] = 1  # If char not in result dict yet, start counting it
            sumFreqChars +=1                   
    for char in result:
        freq[char]=round(result[char]*100/sumFreqChars,2)

    result = sorted(freq.items(), key=operator.itemgetter(1), reverse=True) 
    return result

def newGame():
    answer = input(ONE_MORE_TRY).upper()
    if answer.startswith(YES):
        startGame()
    else:
        print(BYE)
        sys.exit() 

def startGame():
    if len(sys.argv) < 2:        
        with open(PATH_TO_DATABASE) as f:
            print(WELCOME)
            givenWordLength = int(input(THINK_A_WORD))
            searchExpr = DOT * givenWordLength
            wordSubset = searchUniqueWords(searchWords(f),givenWordLength)  # Select words with given length  
            triedChars = []
            GameOn = True
            while GameOn:
                charCounts = getCharFrequency(wordSubset)
                for x in range(len(charCounts)):
                    charCounts = getCharFrequency(wordSubset)
                    mostFreqChar = charCounts[x][0] # Get most frequent char
                    if mostFreqChar in triedChars:
                        continue  # Try next char if such a char already played
                    else:
                        triedChars.append(mostFreqChar)
                    occurencesList = input(POSITIONS_OF_AVAILABLE_LETTERS.format(mostFreqChar)).split(COMMA)
                    if occurencesList != [EMPTY_STRING]:  # if some positions entered, form regexp for further word's filtering
                        searchExpr = list(searchExpr)  # convert regexp from string to list for modification
                        for pos in occurencesList:
                            searchExpr[int(pos)] = mostFreqChar
                        searchExpr = EMPTY_STRING.join(searchExpr)  # convert regexp back from list to string
                        r = re.compile(searchExpr)
                        wordSubset = list(filter(r.match, wordSubset))
                        if len(wordSubset) == 1:
                            print(GUESSED_WORD.format(wordSubset[0]))
                            newGame()
                        elif len(wordSubset) == 0: 
                            print(CANT_GUESS)
                            newGame()
                        else:
                            break  # There're still words to guess, retry with new char frequencies on new wordSubset
                    else:
                        if x == len(charCounts):
                            print(NO_TRIES_LEFT)
                            sys.exit()
                        continue  # if nothing entered, than no char the word includes, so repeat with next most popular char
    else:
        with open(sys.argv[1], 'r') as f:            
            searchWords(f)                
 
if __name__ == '__main__':
    startGame()
