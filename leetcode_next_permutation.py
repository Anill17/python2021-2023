def nextPermutation(nums):

    flag = nums[0]
    max1 = max(nums)
    if nums.sort(reverse = True) == nums:
        return nums[::-1]
    
    
    else:
        for a,i in enumerate(nums):
            if a == 0:
                continue
            elif i > flag:
                nums[a],nums[a-1] = nums[a-1],nums[a]
                flag = i
            else:
                flag = i
        
    return nums

print(nextPermutation([3,1,2]))
            
            
        
        
        

    
