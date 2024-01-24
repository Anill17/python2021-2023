arr = [1,3,2,5,10,15,7]

for i in range(len(arr)):

    for j in range(len(arr) - 1):

        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print(arr)