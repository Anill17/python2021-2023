x = int(input("please enter the depth : ", ))

for i in range(x-1):
    for j in range(x-i-1):
        print(" ",end="")
    for j in range(i+1):
        print(j,end="")
    for j in range(i):
        print(i-j-1,end="")
    print("")
for i in range(x-2,-1,-1):
    for j in range(x-i):
        print(" ",end="")
    for j in range(i-1):
        print(j,end="")
    for j in range(i):
        print(i-j-1,end="")
    print("")
#  diamond shape 
