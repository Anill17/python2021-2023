def containsDuplicate(nums):
    dict1= dict()
    for i in nums:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    
    list1 = dict1.values()

    for i in list1:
        if i > 1:
            return True
    return False

print(containsDuplicate([1,2,3,1]))