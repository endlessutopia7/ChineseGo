'''
Author: endlessutopia7 2022.08.21
'''

import PieceAliveAPI

BOARD_SIZE = 19
FIRST_NINE_HINT_X = "Put the x-axis for your piece (\"ul\", \"u\", \"ur\", \"l\", \"c\", \"r\", \"dl\", \"d\", \"dr\" for pieces on star points, \"exit\" for end game): "
NORMAL_HINT_X = "Put the x-axis for your piece, \"exit\" for end game: "
NORMAL_HINT_Y = "Put the y-axis for your piece: "

STAR_POINTS_MAP = {
    "ul": (4, 4),
    "u": (4, 10),
    "ur": (4, 16),
    "l": (10, 4),
    "c": (10, 10),
    "r": (10, 16),
    "dl": (16, 4),
    "d": (16, 10),
    "dr": (16, 16)}

def placePiece(piece, i, j, board):
    board[i][j] = piece

def printBoard(board):
    for x in board:
        print(" ".join(x))
        
def __validateLocation(i):
    return i in range(1, BOARD_SIZE + 1)
    
if __name__ == '__main__':
    board = [["." for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]
    currentHintX = FIRST_NINE_HINT_X

    print("Beginning board: ")
    printBoard(board)
    
    blackTurn = True
    turnCount = 1

    currentPieceType = ""
    
    while True:
        while currentPieceType != ".":
            currentPieceX = input(currentHintX)
            if currentPieceX == "exit":
                break
            currentPieceY = ""
            
            while not (currentPieceX in STAR_POINTS_MAP or __validateLocation(int(currentPieceX))):
                print("Invalid x-axis input!")
                currentPieceX = input(currentHintX)
            
            if currentPieceX in STAR_POINTS_MAP:
                currentPieceX, currentPieceY = STAR_POINTS_MAP[currentPieceX][0], STAR_POINTS_MAP[currentPieceX][1]
            else:
                currentPieceX = int(currentPieceX)
                currentPieceY = input(NORMAL_HINT_Y)
                
                while not __validateLocation(int(currentPieceY)):
                    print("Invalid y-axis input!")
                    currentPieceY = input(NORMAL_HINT_Y)
                    
                currentPieceY = int(currentPieceY)
                
            currentPieceType = board[currentPieceX - 1][currentPieceY - 1]
            if currentPieceType != ".":
                print("Error - piece already exist.")
        
        # For ending game case
        if currentPieceType == "":
            break
        
        placePiece("X" if blackTurn else "O", currentPieceX - 1, currentPieceY - 1, board)
        
        # border judgement
        if currentPieceX - 2 >= 0:
            PieceAliveAPI.isPieceAlive(board, currentPieceX - 2, currentPieceY - 1, True)
        if currentPieceY - 2 >= 0:
            PieceAliveAPI.isPieceAlive(board, currentPieceX - 1, currentPieceY - 2, True)
        if currentPieceX < BOARD_SIZE:
            PieceAliveAPI.isPieceAlive(board, currentPieceX, currentPieceY - 1, True)
        if currentPieceY < BOARD_SIZE:
            PieceAliveAPI.isPieceAlive(board, currentPieceX - 1, currentPieceY, True)
        
        print("Board after step %d: " % turnCount)
        printBoard(board)
        
        # for successful step, turnCount increase by 1
        blackTurn = not blackTurn
        currentPieceType = ""
        turnCount += 1
        
        # remove on hint on star points
        if turnCount == 10:
            STAR_POINTS_MAP = {}
            currentHintX = NORMAL_HINT_X
            
    print("Game over, please count the pieces manually to decide the winner.")
    printBoard(board)