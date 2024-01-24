# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7

grid = [[1,3,1],[1,5,1],[4,2,1]]
def minpath(i,j):
    memo= {}
    global grid
    if i < 0 or j < 0:
        return float("inf")
    if i == 0 and j== 0:
        return grid[i][j]
    
    else:
        if (i,j) in memo:
           return memo[(i,j)]
        else:
            memo[(i,j)] = grid[i][j] + min(minpath(i-1,j), minpath(i,j-1))
            return memo[(i,j)]
        
    
print(minpath(len(grid)-1,len(grid[0])-1))

