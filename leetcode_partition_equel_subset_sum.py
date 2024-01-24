def canPartition(arr, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False

    if arr[n-1] > sum:
        return canPartition(arr, n-1, sum)
    
    return canPartition(arr, n-1, sum-arr[n-1]) or canPartition(arr,n-1,sum)


def findPartion(arr, n):
   
    sum = 0
    for i in range(0, n):
        sum += arr[i]
    
    if sum % 2 != 0:
        return False
 
    else:
        return canPartition(arr, n, sum // 2)

print(findPartion([1,4,7,3,15],5))