def sqrt(num):
    min = 0
    max = num

    while min <= max:
        mid = (min + max) //2
        if mid * mid <= num < (mid+1)*(mid+1):
                return mid
        elif mid **2 < num:
            min = mid + 1

        else:
            max = mid-1


print(sqrt(9))