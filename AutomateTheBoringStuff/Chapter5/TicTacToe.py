import random
import time

def printBoard(board):
    print('\n' + board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-|-|-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-|-|-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def computerMove():
    print('\nThe computer is making a move...')
    time.sleep(random.randint(2,5))
    index = random.randint(0, len(openMoves) -1)
    print('\nThe computer chose space ' + openMoves[index] + '.')
    return openMoves[index]

def checkWinner(board, letter):
    return((board['1'] == letter and board['2'] == letter and board['3'] == letter) or # across the top
           (board['4'] == letter and board['5'] == letter and board['6'] == letter) or # across the middle
           (board['7'] == letter and board['8'] == letter and board['9'] == letter) or # across the bottom
           (board['1'] == letter and board['4'] == letter and board['7'] == letter) or # down the left
           (board['2'] == letter and board['5'] == letter and board['8'] == letter) or # down the middle
           (board['3'] == letter and board['6'] == letter and board['9'] == letter) or # down the right
           (board['1'] == letter and board['5'] == letter and board['9'] == letter) or # diagonal
           (board['3'] == letter and board['5'] == letter and board['7'] == letter) # diagonal
    )

theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}

openMoves = ['1','2','3','4','5','6','7','8','9']

print('\n***********************************')
print('***** Welcome to Tic-Tac-Toe! *****')
print('***********************************\n')

while True:
    players = input('1 or 2 players? ')
    if (players != '1') and (players != '2'):
        print('Please enter 1 or 2 to select the number of players.')
    else:
        break

turn = 'X'
player1Name = input('Enter Player 1 Name: ')
player2Name = None
currentPlayer = player1Name
if players == '1':
    player2Name = 'computer'
else:
    player2Name = input('Enter Player 2 Name: ')

for n in range(9):
    printBoard(theBoard)
    
    if currentPlayer == 'computer':
        move = computerMove()
        openMoves.remove(move)
    else:
        while True:
            move = input('\nTurn for ' + currentPlayer + '. Move on which space: ')
            if move in openMoves:
                openMoves.remove(move)
                break
            else:
                print('That space is already taken. Please try again.')
    
    theBoard[move] = turn

    if checkWinner(theBoard, turn):
        if currentPlayer == 'computer':
            print('Oh man! You let the computer beat you!')
        else:
            print('\nPlayer ' + currentPlayer + ' has won the game!')
        break
    else:
        if n == 8:
            print('\nNo winners here! It\'s a draw!')
        elif turn == 'X':
            currentPlayer = player2Name
            turn = 'O'
        else:
            currentPlayer = player1Name
            turn = 'X'

printBoard(theBoard)

# http://inventwithpython.com/chapter10.html