# n = 4
# list1 = list()

# for i in range(n):
#     list1.append([])
# for i in range(n):
#     for j in range(i+1):
#         list1[i].append(0)


list1 = [[34], [12,0],[0,4,0],[5,3,0,0]]
list1_d = list1[::]

try:
    for i in range(len(list1)):
        for j in range(i+1):
            if list1[i][j] != 0 and list1[i+1][j] != 0:
                list1_d[i+1][j+1] = list1[i][j] - list1[i+1][j]
            elif list1[i][j] != 0 and list1[i+1][j+1] != 0 : 
                list1_d[i+1][j] = list1[i][j] - list1[i+1][j+1]
            else :
                continue

    for i in range(len(list1)-1,-1,-1):
        for j in range(i):
            if list1[i][j] != 0 and list1[i][j+1] != 0:
                list1_d[i-1][j] = list1[i][j] + list1[i][j+1]
except IndexError:
    pass
print(list1_d)


