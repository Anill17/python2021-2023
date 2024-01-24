l1 = [2,4,3]
l2 = [5,6,4]
f_list1 = list()
output_list = []
ct = 0 
dif = len(l1) - len(l2)

if len(l1) > len(l2):
    for i in range(dif):
        l2.append(0)

else:
    for i in range(dif):
        l1.append(0)

for i in range(len(l1)):
    sum = l1[i] + l2[i]
    
    if sum >= 10 and i == 0:
        f_list1.append(sum)

    elif sum >= 10 and i != 0 and ct == 0:
        f_list1.append(sum % 10)
        ct += 1
    elif sum >= 10 and i != 0 and ct == 1:
        f_list1.append(sum % 10 + 1)
        ct = 0

        
    else:
        if ct == 1:
            f_list1.append(sum + 1)
            ct = 0 
        else:
            f_list1.append(sum)

#that doesn't work and don't know why 
for i in range(len(f_list1)-1,-1,-1):
    output_list.append(f_list1[i])


print("sum of the numbers: ", output_list)



