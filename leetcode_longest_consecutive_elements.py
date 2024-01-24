
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
def longestConsecutive(nums):
    nums = list(set(nums))
    nums.sort()
    res= 0
    fnl = []
    for i in range(len(nums)-1 ):
        if nums[i+1] - nums[i] == 1: 
            res += 1 
        else:
            fnl.append(res)
            res = 0 
        fnl.append(res)
    if len(fnl) == 0:
        return 0
    
    else:

        return max(fnl) + 1 
    
print(longestConsecutive([0,0]))