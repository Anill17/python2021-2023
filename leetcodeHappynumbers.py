num = int(input("please enter the number: ", ))
sum = 0 
while num != 1:
    num = str(num)
    for i in range(len(num)):
        sum += int(num[i])**2
    if sum == 1:
        print("num is happy")
    else:
        print("nope")
        break
    num = sum 
    sum = 0 
