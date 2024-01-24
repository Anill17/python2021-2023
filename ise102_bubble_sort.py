def bubble_sort(list1):
    for i in range(len(list1)):
        switch = False
        for j in range(len(list1)-i-1):
            if list1[j] > list1[j+1]:
                list1[j],list1[j+1] = list1[j+1],list1[j]
                switch = True

    if switch == False:
        return list1

print(bubble_sort([1,3,5,7,9,4,8,2,0]))