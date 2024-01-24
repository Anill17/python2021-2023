# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

def subsets(nums):
    res = []
    subset = []
    def dfs(i) :
        if i >= len(nums):
            res.append(subset.copy())
            return
        # decision to include nums [il
        subset.append(nums[i])
        dfs(i + 1)
        # decision NOT to include nums [i]
        subset.pop()
        dfs(i + 1)
    dfs(0)
    res.sort()
    return res



### dersteki çözüm ###
def gen_subsets(l):
    if len(l) == 0:
        return [[]]
    smaller = gen_subsets(l[:-1])
    extra = l[-1:]
    new = []
    for small in smaller:
        new.append(small+extra)
    return smaller + new




### dersteki diğer çözüm ###

def subsets_2(l):
    doubles = []
    res = [[]]
    for i in range(len(l)):
        res.append([l[i]])
        for j in range(i+1,len(l)):
            doubles.append([l[i],l[j]])
            res.append([l[i],l[j]])
    
    for i in doubles: # ikili listeler
        for j in l: # listedeki elemanlar
            if j not in i and j > i[-1]:
                i.append(j)
                # if i not in res:
                res.append(i)
   #res.sort()
    return res
        
print(subsets([1,2,3,4,5]))
print("================================================================")
print(subsets_2([1,2,3,4,5]))


def check(l): # to check all three funcitons give the same results
    x = subsets(l)
    y = gen_subsets(l)
    if x == y:
        return True
    return False
print(check([1,2,3,4,5]))