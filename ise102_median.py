### creating the randomized list ###
import random 
list1 = list()

for i in range(50000):
    n = random.randint(1,10)
    list1.append(n)


### avarage ###

avg = sum(list1) / len(list1)
print("{} is the avarage of list1".format(avg))

### median ###
list1.sort()

if len(list1) % 2 == 0:
    median = (list1[(len(list1) // 2)-1] + list1[(len(list1) // 2)]) / 2 
else:
    median = list1[((len(list1)) // 2)]

print("{} is the median of list1".format(median))


###histogram###
scaling_multiplier = 0.01
dict1 = dict()
for i in list1:
    if i not in dict1:
        dict1[i] = 1
    else:
        dict1[i] += 1

for i in dict1:
    if dict1[i] % 2 == 0:
        print(i,end=" ")
        if len(list1) >= 1000:
            print("*" * int(dict1[i] * scaling_multiplier))
            print("\t")
        else:
            print("*" * int(dict1[i]))
    else:
        print(i,end=" ")
        if len(list1) >= 1000:
            print("*" * (int(dict1[i]* scaling_multiplier) + 1))
            print("\t")
        else:
            print("*" * int(dict1[i]))
            print("\t")


