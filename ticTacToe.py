import os;

board = []
for i in range(11):
    board.append(str(i))

def drawBoard():
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

def askSides():
    print("Choose Your Sides")
    player1 = ""
    while not(player1 == "X" or player1 == "O"):    
        print("Player 1, Choose : (X or O) >> ")
        player1 = input().upper()
    print("Player 1 is "+player1)
    player2 = ""
    if(player1 == "X"):
        player2 = "O"
    else:
        player2 = "X"
    print("player 2 is "+player2)
    
    return [player1,player2]

def askMove():
    validMoves = []
    for i in range(11):
        validMoves.append(str(i))
    move = 0
    while not(move in validMoves):
        print("Make a move >> " )
        move = input()
    return int(move)

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def gameController():
    drawBoard()
    sides = askSides()
    turn = "p1"
    p1choice = sides[0]
    p2choice = sides[1]
    gamePlaying = True
    while(gamePlaying):
        if(turn == "p1"):
            print("\nPlayer 1 Turn \n")
            moveIndex = askMove()
            board[moveIndex] = p1choice
            os.system('CLS')
            drawBoard()
            if(isWinner(board,p1choice)):
                print("Player 1 Won")
                print("Press O to exit")
                again = int(input())
                if(again == 1):
                    gamePlaying = False
                else:
                    gamePlaying = False
                    
            turn = "p2"
        elif(turn == "p2"):
            print("\nPlayer 2 Turn \n")
            moveIndex = askMove()
            board[moveIndex] = p2choice
            os.system('CLS')
            drawBoard()
            if(isWinner(board,p2choice)):
                print("Player 2 Won")
                print("Press O to exit")
                again = int(input())
                if(again == 0):
                    gamePlaying = False
                else:
                    gamePlaying = False
            turn = "p1"
gameController()
