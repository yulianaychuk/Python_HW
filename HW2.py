
# Created on Aug 6, 2019
# @author: Yuliya_Naychuk

import random

CHOOSE_POSITION = 'Choose a position: (1-9): '
CONGRAT = ', congratulations! You won!'
DRAW = 'The game ended in a draw...'
EMPTY = ''
FIRST_TURN = 'Player 1, choose x or o: '
LINE = "-------------"
O_MARKER = 'o'
P1 = 'Player 1'
P2 = 'Player 2' 
PLAY_AGAIN_CHOICE = 'Play again? enter y or n '
SLASH = "|"
SPACE = ' '
WELCOME_MSG = 'Welcome to Tic Tac Toe!'
X_MARKER = 'x'
Y ='y'
YOUR_TURN = ", it's your turn!"

def printGameBoard(gameboard): 
    gameboard =  gameboard
    print (LINE)
    for i in range(3):
        print( SLASH, gameboard[0+i*3], SLASH, gameboard[1+i*3], SLASH, gameboard[2+i*3], SLASH)
    print(LINE)
    
def playerInput():
    marker = EMPTY
    while marker != X_MARKER and marker !=O_MARKER:
        marker = input(FIRST_TURN)
    player1 = marker
    if player1 == X_MARKER:
        player2 = O_MARKER
    else:
        player2 = X_MARKER
    return (player1, player2)
  
def makeTurn(gameboard, marker, position):
    gameboard[position-1] = marker
    return gameboard

def ifWonCheck(gameboard, marker):
    j=0
    for i in range(3):
        return ((gameboard[0+i*3] == gameboard[1+i*3] == gameboard[2+i*3] == marker) or
        (gameboard[i+j*3] == gameboard[i+(j+1)*3] == gameboard[i+(j+2)*3] == marker) or 
        (gameboard[0+j*3] == gameboard[1+(j+1)*3] == gameboard[2+(j+2)*3] == marker) or 
        (gameboard[2+j*3] == gameboard[1+(j+1)*3] == gameboard[0+(j+2)*3] == marker)) 
   
def spaceCheck(gameboard, position):
    return gameboard[position-1] == SPACE

def isFullGameboard(gameboard):
    for i in range(1,10):
        if spaceCheck(gameboard, i):
            return False
    return True #board is full#  

def chooseFirstTurn():
    randInt = random.randint(0,1)
    if randInt == 0:
        return P1
    else:
        return P2
    
def playerChoice(gameboard):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not spaceCheck(gameboard, position):
        try:
            position = int(input(CHOOSE_POSITION))
        except ValueError:
            position = 0    
    return position 

def rePlay():
    return input(PLAY_AGAIN_CHOICE).startswith(Y)

def playTheGame(gameboard,turn,playerMarker):
    printGameBoard(gameboard) #show the board  # Player's turn.
    print(turn)
    position = playerChoice(gameboard)
    makeTurn(gameboard,playerMarker,position)           
    if ifWonCheck(gameboard,playerMarker): #check if Player 2 won 
        printGameBoard(gameboard)
        print(turn+ CONGRAT)
        return False                
    elif isFullGameboard(gameboard):
        printGameBoard(gameboard)
        print(DRAW)
        return False        
    else:
        return turn            
    
if __name__ == '__main__':
    print(WELCOME_MSG)
    while True:   
        gameboard = ([SPACE] * 10)[1:]
        printGameBoard(gameboard) 
        player1Marker, player2Marker = playerInput()        
        turn = chooseFirstTurn()
        print(turn + YOUR_TURN)
        gameOn = True   
        while gameOn: # Play the game 
            if turn == P1: #Player 1 Turn
                gameOn = playTheGame(gameboard,turn,player1Marker)
                if turn == gameOn:
                    turn = P2
                else:
                    continue 
            elif turn == P2:
                gameOn = playTheGame(gameboard,turn,player2Marker) 
                if turn == gameOn:
                    turn = P1                
                else:
                    continue 
        if not rePlay():
            break                 


