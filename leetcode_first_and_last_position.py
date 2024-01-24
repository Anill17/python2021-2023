# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
nums = [5,7,8,8,8,8,8,8,10]
res = list()

def bisection(l,r,target):
    global nums
    if l < r:
        mid = (r + l) // 2
        if nums[mid] == target:
            return mid
        
        elif nums[mid] < target:
            return bisection(nums,mid+1,r,target)
        
        elif nums[mid] > target:
            return bisection(nums,l,mid - 1,target)
    else:
            return -1 


def searchRange(target):
    global nums
    
    idx = bisection(0,len(nums)-1, 8)
    ctr = idx
    ctl = idx

    for i in range(idx,len(nums)):
        if nums[i] == nums[idx]:
            ctr += 1
        else:
            break
    for i in range(idx-1,-1,-1):
        if nums[i] == nums[idx]:
            ctl -= 1 
        else:
            break
    
    res.append(ctl)
    res.append(ctr-1)
    return res


print(searchRange(8))








