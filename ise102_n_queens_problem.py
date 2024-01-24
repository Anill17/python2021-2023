board =  [[0,0,0,0],
         [0,0,0,0],
         [0,0,0,0],
         [0,0,0,0]]
n = len(board)

def solve_n_queens():
    global board
    if solve(0):
        printer()
    else:
        print("no solution")

def solve(col_idx):
    global board
    if col_idx == n:
        return True
    for row_idx in range(n):
        if is_place_valid(row_idx,col_idx):
            board[row_idx][col_idx] = 1
            if solve(col_idx+1):
                return True
        
            board[row_idx][col_idx] = 0 ### backtracking
    return False


def is_place_valid(row_idx,col_idx):
    global board
    for i in range(n):
        if board[row_idx][i] == 1:
            return False
   
    j = col_idx

    for i in range(row_idx,-1,-1):
        if i < 0:
            break
        if board[i][j] == 1:
            return False
        j -= 1
    j = col_idx

    for i in range(row_idx,n):
        if j < 0:
            break
        if board[i][j] == 1:
            return False
        j -= 1
    
    return True
def printer():
    for i in board:
        print(i)

solve_n_queens()
