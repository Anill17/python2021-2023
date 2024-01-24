def fibo(n):
    list1 = [1,1]
    if n == 0:
        return list1[0]
    elif n == 1:
        return list1[1]

    else:
        new2 = fibo(n-1) + fibo(n-2)
        list1.append(new2)
        return list1[n]
    
print(fibo(5))