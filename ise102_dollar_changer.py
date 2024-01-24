penny = 1
nickel = 5
dime = 10 
quarter = 25
res = list()

inp = int(input("please enter the bill: ", ))
cents = inp * 100 

for i in range(inp//quarter+25):
    for j in range(inp//dime+10):
        for k in range(inp//nickel+5):
            for l in range(cents+1):
                sum = i + j + k +l
                if sum == cents:
                    res.append([i,j,k,l,sum])
print(res)