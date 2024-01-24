### horizantel ###
list1 = [1,1,1,1,4,4,4,2,2,2,3,3,4,4,5]
dict1 = {}
for i in range(len(list1)):
    if list1[i] not in dict1:
        dict1[list1[i]] = 1
    else:
        dict1[list1[i]] += 1


my_keys = list(dict1.keys())

my_keys.sort()

sorted_dict1 = {i: dict1[i] for i in my_keys}

print(sorted_dict1)

for i in sorted_dict1:
    
    print(i, "*" * sorted_dict1[i])
    print()


print("################################################################")
### vertical ###

list2 = []
for i in dict1:
    list2.append(dict1[i])
print(list2)
dict1_keys = list(dict1.keys())
print_list = []


dict1_keys.sort()

sorted_dict1 = {i: dict1[i] for i in dict1_keys}

for i in range(max(list2), 0, -1):
    
    line = ""
    for j in list2:
        if j >= i:
            line += "*"
        line += "\t"
        
    print_list.append(line)

for line in print_list:
    print(line)
line = " "
for i in dict1_keys:
    line += str(i) 
    line += "\t"
print(line)
