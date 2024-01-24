def subset_sum(arr, idx, m):
    if idx == 0:
        return 
    else:
        return max(subset_sum(arr, idx-1, m), subset_sum(arr, idx-1,m-arr[idx]) + arr[idx])

print(subset_sum([5,2,3,1], 3, 9))