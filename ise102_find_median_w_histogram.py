list1 = [1,2,3,4,5,5,5,6,7,7,8,10,1,3,3]

def bubble_sort(elements):
    for i in range(len(elements)):
        switch = False
        for j in range(len(elements)-i-1):
            if elements[j] > elements[j+1]:
                elements[j],elements[j+1] = elements[j+1],elements[j]
                switch = True

    if switch == False:
        return elements

    

### finding median with the help of historgram ###
def find_median(list1):
    ct = 0
    sorted_list = bubble_sort(list1)
    num_dict = {}
    median_idx = ((len(sorted_list)) // 2) ## for odd
    dummy = 0 

    for i in sorted_list:
        if i not in num_dict:
            num_dict[i] = 1
        else:
            num_dict[i] += 1

    dict_keys = list(num_dict.keys())

    ###printing the median###
    for a, i in enumerate(num_dict):
        print(dict_keys[a],end=" ")
        print("*" * num_dict[i])
        print("\t")


    for a, i in enumerate(num_dict):
        dummy += num_dict[i]
        if dummy > median_idx:
            return i
        if dummy == median_idx and len(list1) % 2 == 0:
            return ((i + dict_keys[a+1]) / 2)
    
print(find_median(list1))
        

        
        

    

    
