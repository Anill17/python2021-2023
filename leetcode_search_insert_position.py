def searchInsert(nums,target):
    l, r = 0, len(nums)-1
    mid = (l + r) // 2 
    if target > nums[-1]:
        return len(nums)
    elif target < nums[0]:
        return 0 
    else:
        while l <= r:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = r - 1
            else:
                l = l + 1
            mid = (l + r) // 2
        return r + 1
print(searchInsert([1,3,5,6], 2))

