# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11

def triangle(row,col,arr):
    if row == len(arr):
        return 0
    else:
        return min(arr[row][col] + triangle(row+1,col,arr),arr[row][col] + triangle(row+1,col+1,arr))

print(triangle(0,0,[[2],[3,4],[6,5,7],[4,1,8,3]]))