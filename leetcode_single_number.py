dict1 = {}
def singlenumber(nums):
    for i in nums:
        if i not in dict1.keys():
            dict1[i] = 1
        else:
            dict1[i] += 1
    for i in dict1:
        if dict1[i] == 1:
            return i 
print(singlenumber([4,1,2,1,2]))