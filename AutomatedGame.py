'''
Author: endlessutopia7 2022.08.21

A very simple automated simulation of Chinese Go without AI.
Looks like two amateur children ;-)
'''

import PieceAliveAPI
import time
import random

BOARD_SIZE = 19

STAR_POINTS_SET = [
    (4, 4),
    (4, 10),
    (4, 16),
    (10, 4),
    (10, 10),
    (10, 16),
    (16, 4),
    (16, 10),
    (16, 16)
]

def placePiece(piece, i, j, board):
    board[i][j] = piece

def printBoard(board):
    for x in board:
        print(" ".join(x))
        
def __validateLocation(i):
    return i in range(1, BOARD_SIZE + 1)
    
if __name__ == '__main__':
    board = [["." for i in range(BOARD_SIZE)] for j in range(BOARD_SIZE)]

    print("Beginning board: ")
    printBoard(board)
    print("Press Ctrl-C to quit simulation (as workaround)")
    
    blackTurn = True
    turnCount = 1

    currentPieceType = ""
    
    try:
        while True:
            # for first pieces, just go towards star points
            if turnCount <= 9:
                currentPiece = random.choice(STAR_POINTS_SET)
                currentPieceX, currentPieceY = currentPiece[0], currentPiece[1]

                STAR_POINTS_SET.remove(currentPiece)

            # for the rest, place piece randomly
            else:
                while currentPieceType != ".":
                    currentPieceX = random.randint(1, BOARD_SIZE)
                    currentPieceY = random.randint(1, BOARD_SIZE)
                    
                    # if piece already exists, just retry
                    currentPieceType = board[currentPieceX - 1][currentPieceY - 1]
            
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
            if turnCount == 10:
                del(STAR_POINTS_SET)

            time.sleep(3)
    except KeyboardInterrupt:
        print("Game over, please count the pieces manually to decide the winner.")
        printBoard(board)