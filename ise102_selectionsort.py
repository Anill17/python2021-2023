def selection(list1):
    for i in range(len(list1)):
        min_idx = i
        for j in range(i+1,len(list1)):
            if list1[j] < list1[min_idx]:
                min_idx = j
        
        list1[min_idx], list1[i] = list1[i],list1[min_idx]
                
    return list1


print(selection([1,3,6,4,8,10,2]))




