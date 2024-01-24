# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
list1 = [[1],[1,1]]

depth = 10

for i in range(depth-2):
    list1.append([1])
list1_d = list1[::]

for count, i in enumerate(list1):
    if count < 1:
        continue
    for j in range(len(i)):
        try:
            list1_d[count+1].append(i[j] + i[j+1])
        except IndexError:
            pass
    try:
        list1_d[count+1].append(1)
    except IndexError:
        pass

print(list1_d)

for i in list1_d:
    print(i)
               
