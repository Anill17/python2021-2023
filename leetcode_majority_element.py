dict1 = dict()
def majority(nums):
    for i in nums:
        if i not in dict1.keys():
            dict1[i] = 1 
        else:
            dict1[i] += 1
        
    max1 =  max(dict1.values())
    for i in dict1.keys():
        if dict1[i] == max1:
            return i 
print(majority([2,2,1,1,1,2,2]))