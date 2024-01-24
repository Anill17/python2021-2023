def merge(left, right):
    result = []

    i,j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i+= 1
        else:
            result.append(right[j])
            j+= 1 

    
    while i < len(left):
        result.append(left[i])
        i+= 1
        
    while j < len(right):
        result.append(right[j])
        j += 1 

    return result
    

def merge_sort(l):

    if len(l) <2 :
        return l[:]
    
    else:
        middle = len(l) // 2

        left = merge_sort(l[:middle])
        right= merge_sort(l[middle:])
        return merge(left,right)
    


print(merge_sort([1,2,5,3,6,8,9]))