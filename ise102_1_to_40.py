list1 = [1,3,9,27,-27,-9,-3,-1]
res = list()
sum = 0 
for i in list1:
    for j in list1:
        for k in list1:
            for l in list1:
                sum = i + j + k +l
                if 1 < i + j + k + l < 40:
                    res.append([i,j,k,l,sum])
print(res)

