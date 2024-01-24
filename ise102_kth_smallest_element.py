
def kth_smallest(arr,target):
    smaller = list()
    greater = list()
    pivot = arr[0]
    
    for i in arr:
        if i < pivot:
            smaller.append(i)
        elif i > pivot:
            greater.append(i)

    if len(smaller) == target-1:
        return pivot
    elif len(smaller) <= target:
        return kth_smallest(greater,target)
    
    else:
        return kth_smallest(smaller,target)
    
print(kth_smallest([8,15,6,13,2,7,12,5,9,10],3))
    