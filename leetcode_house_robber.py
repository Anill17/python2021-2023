def rob(arr,idx):
    if idx >= len(arr):
        return 0
    
    else:
        return max(arr[idx]+ rob(arr,idx+2),rob(arr,idx+1))



print(rob([2,7,9,3,1],0))