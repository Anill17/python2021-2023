def func(digits):
    ct = 0 
    for i in range(len(nums)-1,-1,-1):
        if nums[i] == 9:
            ct += 1
        else:
            nums[i] += 1
            break

    for i in range(len(nums)-1,-1,-1):
        
        if ct == 0:
            break
        elif ct != 0:
            nums[i] = 0 
            ct -= 1

    if nums[0] == 0:
        nums.insert(0,1)
        

    return nums 

print(func([1,0,9,9]))