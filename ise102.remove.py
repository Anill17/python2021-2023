list1 = [1,1,2,2,33]
dummy = list()
for i in range(len(list1)):
    for j in range(i+1,len(list1)-1):
        if list1[i] == list1[j]:
            dummy.append(list1[j])
            list1[j],list1[j+1] = list1[j+1],list1[j]
dummy = set(dummy)



for i in range(len(dummy)):
    list1.pop()
print(list1)

            
            
            