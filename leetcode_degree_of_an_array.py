
def degree(nums):
    dict1 = {}
    list1 = list()
    idx = list()
    res = list()
    res_dict = dict()
    res_list = list()
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    print(dict1)
    max_val = max(dict1.values())
    print(max_val)
    for i in dict1:
        if dict1[i] == max_val:
            list1.append(i)

    print(list1)

    for i in list1:
        for j in range(len(nums)-1,-1,-1):
            if nums[j] == i:
                res_dict[i] = (nums.index(i),j)
                break
    print(res_dict)
    
    for i in res_dict:
        res_list.append(res_dict[i][-1]-res_dict[i][0])
    
    return min(res_list) + 1

print(degree([1,2,2,3,1,4,2]))
