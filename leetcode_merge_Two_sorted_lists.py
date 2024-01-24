list1 = [1,2,4]
list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
res = list()
for i in list1:
    for j in list2:
        if i < j: 
            res.append(i)
        elif i == j:
            res.append(i)
            res.append(j)
        else:
            res.append(j)
        break
print(res)