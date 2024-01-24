def jump(arr,ct):
    curr = arr[0]
    for i in range(1,len(arr)):
        if curr == 0:
            return False
        curr = curr -1
        ct += 1
        
        
        curr = max(curr,arr[i])

    return (True,ct)

print(jump([2,3,1,1,4],0))
