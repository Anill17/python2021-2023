list1 = [14,3,27,4,5,15,1]

def sequence(arr,idx):
    if idx >= len(arr):
        return 0
    else:
        return max(sequence(arr,idx+1), sequence(arr, idx+2) + arr[idx]) 

print(sequence([4,2,3,5,1,6,7],0))
print(sequence([3,15,17,23,11,3,4,5,17,23,34,17,18,14,12,55],0))
########## optimized solution with dp ########

def outer(arr):

    dp = [-1 for _ in range(len(arr)+1)] ### instead of making a 3d array i used 2d array for better space optimization

    return sequence(arr,0,dp)

def sequence(arr,idx,dp):
    
    if idx >= len(arr):
        return 0
    if dp[idx] != -1:
        return dp[idx]
    else:
        dp[idx] = max(sequence(arr,idx+1,dp), sequence(arr, idx+2,dp) + arr[idx]) 
        print(dp)
        return dp[idx]
    

#print(outer([14,3,27,4,5,15,1]))
# print(outer([3,15,17,23,11,3,4,5,17,23,34,17,18,14,12,55]))

#  [3,15,17,23,11,3,4,5,17,23,34,17,18,14,12,55]