def sudoku():
    board_size = 9 
    min_number = 1
    max_number = 9
    box_size = 3 # 3x3 boxes 9 per sudoku board
    
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0], 
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    
    def run():
        if solve(0,0):
            printer(grid)
            
        else:
            print("there is no feasible solution")
    
    def is_valid(row,col,num):
        box_row_offset = (row // 3) * box_size
        box_col_offset = (col // 3) * box_size
        
        for i in range(board_size):
            if grid[row][i] == num:
                return False

        for i in range(board_size):
            if grid[i][col] == num:
                return False
        
        for i in range(box_size): ## for checking 3x3 box 
            for j in range(box_size):
                if grid[box_row_offset + i][box_col_offset + j] == num:
                    return False
        
        return True
        

    def solve(row,col):
        if row == board_size:
            col += 1
            if col == board_size:
                return True
            else:
                row = 0 
        else:

            if grid[row][col] != 0:
                return solve(row+1,col)
            
            for num in range(min_number,max_number+1):
                if is_valid(row,col,num):
                    grid[row][col] = num
                    
                    if solve(row+1,col):
                        return True
                    else:
                        grid[row][col] = 0 

            return False

    def printer(grid):
        for i in grid:
            print(i)

    run()

sudoku()