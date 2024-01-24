import time 
time1 = time.time()

list1 = list()#vehicles heapified
list2 = list()#requests.txt
list3 = list()#vehicles_test.txt
list4 = list()#vehicles



def min_heapify(A,k):
    l = 2 * k + 1
    r = 2 * k + 2

    if l < len(A) and A[l] < A[k]:
        smallest = l
    else:
        smallest = k
    if r < len(A) and A[r] < A[smallest]:
        smallest = r
    if smallest != k:
        A[k], A[smallest] = A[smallest], A[k]
        min_heapify(A, smallest)


def build_min_heap(A):
    n = int((len(A)//2)-1)
    for k in range(n, -1, -1):
        min_heapify(A,k)

def decrease_key(arr,idx, N):
    
    arr[idx][0] = 0 # decrease_key
    while int(float(arr[(idx-1) // 2][0])) > int(float(arr[idx][0])):  #check if the parent is bigger than the child 
        arr[(idx-1) // 2], arr [idx] = arr[idx], arr[(idx-1) // 2] # swap them if the condition is true 
    N -= 1 

def extract(arr,key, N):
 
    # Replace deleted element with last element
    arr[key],arr[-1]= arr[-1],arr[key]

    arr.remove(arr[key])

    # heapify the root node
    N -= 1 
    build_min_heap(arr)
    

def insert(arr, key, N): 

    # Insert the element at end of Heap
    arr.append(key) # key = list
    # Heapify the new node following a
    # Bottom-up approach
    build_min_heap(arr)
    N -= 1

N = int(input("N= ", ))
while N > 0:     
   
    with open("vehicles.txt", "r") as f:
        count = len(f.readlines())
    with open("vehicles.txt", "r") as f:
        for i in range(count):
            line = f.readline()
            read = line.split()
            
            if read != ['key', 'value', 'vehicle_id', 'location', 'distance', 'speed']:
                speed = int(read[-1])
                distance = int(float(read[-2]))
                
                timee = distance / speed
                timee = str(time1)
                read.insert(0, timee)
                list1.append(read)
                build_min_heap(list1)


    with open("vehicles.txt", "w") as f:
        first_line = "key value vehicle_id location distance speed"
        f.writelines(first_line)
        f.writelines("\n")

        for i in range(len(list1)):
            element = " ".join(list1[i])
            f.writelines(element)
            f.writelines("\n")


##taks1_done##

    with open("requests.txt", "r") as f:
        count1 = len(f.readlines())
    with open("requests.txt", "r") as f:
        for i in range(count1):
            line = f.readline()
            read = line.split()
            if read != ["location", "distance", "lucky_number"]:
                list2.append(read)
    
    for i in range(count1):
        if list2[i][-1] == "0":
            with open("vehicles.txt", "r") as fp, open("call_history_1000.txt", "w") as f:
                for j in range(count):
                    line = fp.readline()
                    read = line.split()
                    if read!= ['key', 'value', 'vehicle_id', 'location', 'distance', 'speed']:
                        f.writelines(read[1])
                        f.writelines("\n")
                        list4.append(read) # list4 consists of vehicles

       
            extract(list2,0,N)
    

        else:
            lucky_number = int(list2[i][-1])
            with open("vehicles.txt", "r") as f, open("call_history_1000.txt", "w") as fp:
                count2 = len(f.readlines(  ))
            with open("vehicles.txt", "r") as f, open("call_history_1000.txt", "w") as fp:
                for i in range(count2):
                    line = f.readline()
                    read = line.split()
                    if read != ["key", "value", "vehicle_id", "location", "distance", "speed"]:
                        list3.append(read)
                decrease_key(list3,lucky_number,N)
                
                
                
                #fp.writelines(list3[lucky_number][1])
                fp.writelines(list3[0][1])
                fp.writelines("\n")


        
        
time2 = time.time()

print(time2-time1)
















                
            
                