def setZeroes(matrix):
    max_row = len(matrix)-1
    max_col = len(matrix[0])-1
    for row, i in enumerate(matrix):
        for col in range(len(i)):
            if matrix[row][col] == 0:
                set0_row(matrix,row,col,max_row,max_col)
                set0_col(matrix,col,row,max_col,max_row)
                printer(matrix)
                return matrix
            

# def set0_row(matrix,row,col,max_row,max_col):
    
#     if max_row < 0:
#         return matrix 
#     else:
#         matrix[max_row][col] = 0 
#         return set0_row(matrix,row,col,max_row-1,max_col)

# def set0_col(matrix,col,row,max_col,max_row):
#     if max_col < 0:
#         return matrix 
#     else:
#         matrix[max_col][row] = 0
#         return set0_col(matrix,col,row,max_col-1,max_row)

def set0_row(matrix,row,col,max_row,max_col):
    
    for i in range(max_row,-1,-1):
        matrix[row][i] = 0
    return matrix
def set0_col(matrix,col,row,max_col,max_row):
    
    for i in range(max_col,-1,-1):
        matrix[i][col] = 0
    return matrix
def printer(matrix):
    
    for i in matrix:
        print(i)
    
setZeroes([[1,1,1],[1,0,1],[1,1,1]])








#  print(setZeroes([[1,1,1],[1,0,1],[1,1,1]])) ###
#  [[1,0,1],[0,0,0],[1,0,1]] ###