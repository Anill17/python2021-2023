#nums = [-1,2,1,-4] target = 0
def threeSumClosest(nums,target):
    dict1 = {}
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    dict1[nums[i]] -= 1
                    dict1[nums[j]] -= 1
                    dict1[nums[k]] -= 1
                    if dict1[nums[i]] >= 0 and dict1[nums[j]] >= 0 and dict1[nums[k]] >= 0:

                        return (nums[i],nums[j],nums[k])
                
print(threeSumClosest([-1,0,2,4,-1,4,8,16],6))