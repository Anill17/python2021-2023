val = int(input("please enter the exact value : ", ))
res = []
wallet = [(1,7),(5,3),(10,1)]
def printer(res):
    print(" i  j  k")
    for i in res:
        print(i)

for i in range(1+1):
    for j in range(3+1):
        for k in range(7+1):
            if i*10 + j*5 + k == val:
                res.append([i,j,k])
printer(res)

