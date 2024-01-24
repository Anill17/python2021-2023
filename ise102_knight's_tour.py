board = [[-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1],
         [-1,-1,-1,-1,-1,-1,-1,-1]]

n = len(board)     
x_moves = [2,1,-1,-2,-2,-1,1,2]
y_moves = [1,2,2,1,-1,-2,-2,-1]

def solve_problem():
    global board
    board[0][0] = 0 ### starting point
    if solve(1,0,0):    ## first one is counter second one is row and the third one is column
        printer(board)
    else:
        print("there is no feasible solution")

def solve(step_ct,x,y):
    global board
    global n 
    if step_ct == n*n:
        return True
    
    for move_index in range(len(x_moves)):
        next_x = x + x_moves[move_index]
        next_y = y + y_moves[move_index]
        if is_valid_move(next_x,next_y):
            board[next_x][next_y] = step_ct

            if solve(step_ct+1,next_x,next_y):
                return True ### bu true ne işe yarıyor
            
            board[next_x][next_y] = -1 ### backtracking ###
    return False
def is_valid_move(x,y):
    global board
    global n 
    if x < 0 or x >= n:
        return False
    if y < 0 or y >= n:
        return False
    if board[x][y] > -1:
        return False
    
    return True

def printer(board):
    for i in board:
        print(i)

solve_problem()