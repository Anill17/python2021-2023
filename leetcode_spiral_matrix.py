matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
list1= list()
row = len(matrix)
column = len(matrix[row-1])
ctj = 0
cti = 0

# i = 0 
def go_right(list1,ctj,j):
    for j in range(column):
        if matrix[i][j] not in list1:
            list1.append(matrix[i][j])
            ctj += 1 
    j = ctj-1
    
    return list1, j, ctj

# j = 3
def go_down(list1,cti,i): 
    for i in range(len(matrix)):
        if matrix[i][j] not in list1:
            list1.append(matrix[i][j])
            cti += 1
    i = cti-1
    return list1, i, cti
# i = 2 
def go_left(list1,ctj,j):
    for j in range(column-1-1,-1):
        if matrix[i][j] not in list1:
            list1.append(matrix[i][j])
            ctj -= 1
    j = ctj+1
    return list1, j, ctj
# j = 0 
def go_up(list1,cti,i):
    for i in range(row-1,-1,-1):
        if matrix[i][j] not in list1:
            list1.append(matrix[i][j])
            ctj -= 1
    i = cti-1
    return list1, j, cti

while len(list1) != (column**row):
    i = 0 
    j = 0
    go_right(list1,ctj,j)
    print(list1)
    go_down(list1,cti,i)
    print(list1)
    go_left(list1,ctj,j)
    print(list1)
    go_up(list1,cti,i)
    print(list1)


    






        