'''
Author: endlessutopia7 2022.08.07
'''

# Decide if a go piece is alive

# Actually similar to the island problem, except adding terminating
# condition when meeting "." as piece is alive
 
OPPONENT_MAP = {"X": "O", "O": "X"}
 
# "X" as black, "O" as white, "." as empty, otherwise invalid
def isPieceAlive(board, i, j, eat = False):
    __validateBoard(board)
  
    if board[i][j] == ".":
      return
    __validatePiece(board[i][j])
    
    visitedNodes = set()
 
    row, column = len(board), len(board[0])
    
    # for BFS search (once found empty spot, stop immediately as piece is alive)
    queue = [(i, j)]
    
    selfPiece = board[i][j]
    opponentPiece = OPPONENT_MAP[selfPiece]
    while len(queue) > 0:
        currentPiece = queue.pop(0)
        if currentPiece in visitedNodes:
            continue
        
        current_i, current_j = currentPiece[0], currentPiece[1]
        visitedNodes.add((currentPiece[0], currentPiece[1]))
        if current_i - 1 >= 0:
            if board[current_i - 1][current_j] == ".":
                return True
                
            if board[current_i - 1][current_j] == selfPiece and (current_i - 1, current_j) not in visitedNodes:
                queue.append((current_i - 1, current_j))
        
        # right
        if current_i + 1 < row:
            if board[current_i + 1][current_j] == ".":
                return True
                
            if board[current_i + 1][current_j] == selfPiece and (current_i + 1, current_j) not in visitedNodes:
                queue.append((current_i + 1, current_j))
        
        # up
        if current_j - 1 >= 0:
            if board[current_i][current_j - 1] == ".":
                return True
                
            if board[current_i][current_j - 1] == selfPiece and (current_i, current_j - 1) not in visitedNodes:
                queue.append((current_i, current_j - 1))
        
        # down
        if current_j + 1 < column:
            if board[current_i][current_j + 1] == ".":
                return True
                
            if board[current_i][current_j + 1] == selfPiece and (current_i, current_j + 1) not in visitedNodes:
                queue.append((current_i, current_j + 1))
    
    print(visitedNodes)
    if eat:
        for x in visitedNodes:
            board[x[0]][x[1]] = "."
            
    return False

def __validateBoard(board):
    if board is None or len(board) == 0 or len(board[0]) == 0: 
        raise Expection("Error - board is empty")
 
    columnSize = len(board[0])
    for i in range(1, len(board)):
        if len(board[i]) != columnSize:
            raise Exception("Error - board shape not rectangle")
 
def __validatePiece(piece):
    if piece not in ("O", "X"):
        raise Exception("Error - incorrect piece type")
