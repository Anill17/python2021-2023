def revert(nums):

    l = 0 
    r = len(nums) -1 

    while l < r:
        nums[l],nums[r] = nums[r], nums[l]
        l += 1  
        r -= 1 
    return nums 

print(revert([1,2,3,4,5]))