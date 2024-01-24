def matrix_mult(m1,m2): # 1,3 x 3,1
    if len(m1[0]) != len(m2):
        print("cannot be multiplied")
        return 
    else:
        res = [[0 for i in range(len(m1))] for i in range(len(m2[0]))]
        for i in range(len(m1)):
            for j in range(len(m2[0])):
                for k in range(len(m2)):
                    res[i][j] += m1[i][k] * m2[k][j]
    

        return res
print(matrix_mult([[1,2,3],[4,5,6]],[[10,11],[20,21],[30,31]]))