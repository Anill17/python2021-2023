def fibo(n):
    list1 = [0 for i in range(n+1)]
    if n == 0:
        list1[0] = 1
        return list1[0]
    elif n == 1:
        list1[1] = 1
        return list1[1]
    else:
        new = fibo(n-2) + fibo(n-1)
        list1[n] = new
        return list1[n]
    
print(fibo(5))