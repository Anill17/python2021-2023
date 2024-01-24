inp = input("please enter a number: ", )
sum = 0
ct = 0
while int(inp) != 1 and ct < 10:
    ct+= 1 
    for i in range(len(inp)):
        sum += (int(inp[i]))**2
        inp = sum 
        sum = 0 
        if inp == 1:
            print("true")
            break
        else:
            print("false")
