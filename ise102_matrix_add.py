def add(m1,m2):
    res = [[0 for i in range(len(m1[0]))] for i in range(len(m2))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            res[i][j] = m1[i][j] + m2[i][j]
          

    return res

print(add([[1,3],[1,0],[1,2]],[[0,0],[7,5],[2,1]]))