# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

def topKfrequent(nums,k):
    d = dict()
    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1 
    d = sorted(d,key=d.get,reverse=True) ## sorting the dict by the values ### a = sorted(d.items(), key=lambda x: x[1])    ## also works
    return d[:k]
print(topKfrequent([1,1,1,2,2,3],2))