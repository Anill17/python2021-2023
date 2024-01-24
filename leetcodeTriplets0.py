nums = [-1,0,1,2,-1,-4]
d = dict()
for i in nums:
    if i not in d:
        d[i] = 0 
for i in nums:
    while i in nums:
    
        nums.remove(i)
        if i in nums:
            d[i] += 1

f_list = []
list1= []
for i in range(len(nums)):
    for j in range(len(nums)):
        for k in range(len(nums)):
            if nums[i] + nums[j] + nums[k] == 0 # character countitites should be the same in the list, use dict to reveive that :
                list1.append(nums[i])
                list1.append(nums[j])
                list1.append(nums[k])
                f_list += list1
                list1.clear()
print(f_list)