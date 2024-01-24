def search(nums,target):
    if target not in nums:
        return -1
    elif target == len(nums)-1:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
    
    else:
        nums = nums[target:len(nums)] + nums[0:target]
        for i in range(len(nums)):
            if nums[i] == target:
                return i    
print(search([4,5,6,7,0,1,2],0))