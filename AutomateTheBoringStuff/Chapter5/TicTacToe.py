def printBoard(board):
    print('\n' + board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-|-|-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-|-|-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def checkWinner(board, letter):
    return((board['1'] == letter and board['2'] == letter and board['3'] == letter) or # across the top
           (board['3'] == letter and board['4'] == letter and board['5'] == letter) or # across the middle
           (board['4'] == letter and board['5'] == letter and board['6'] == letter) or # across the bottom
           (board['1'] == letter and board['4'] == letter and board['5'] == letter) or # down the left
           (board['2'] == letter and board['5'] == letter and board['8'] == letter) or # down the middle
           (board['3'] == letter and board['6'] == letter and board['9'] == letter) or # down the right
           (board['1'] == letter and board['5'] == letter and board['9'] == letter) or # diagonal
           (board['5'] == letter and board['5'] == letter and board['7'] == letter) # diagonal
    )

theBoard = {'1': '1', '2': '2', '3': '3',
            '4': '4', '5': '5', '6': '6',
            '7': '7', '8': '8', '9': '9'}

openMoves = ['1','2','3','4','5','6','7','8','9']
turn = 'X'

for i in range(9):
    printBoard(theBoard)
        
    while True:
        move = input('\nTurn for ' + turn + '. Move on which space: ')
        if move in openMoves:
            openMoves.remove(move)
            break
        else:
            print('That space is already taken. Please try again.')
    
    theBoard[move] = turn

    if checkWinner(theBoard, turn):
        print('Player ' + turn + ' has won the game!')
        break
    else:
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'

printBoard(theBoard)

# http://inventwithpython.com/chapter10.html