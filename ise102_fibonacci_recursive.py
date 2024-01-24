def fib(n):
    if n == 1:
        return 1 
    elif n == 2:
        return 2 
    else:
        return fib(n-2) + fib(n-1)
    
print(fib(50))


def fib_dict(n,d):
    
    if n in d:
        return d[n]
    else:
        
        d[n] = fib_dict(n-2,d) + fib_dict(n-1,d)
        return d[n]
    
print(fib_dict(50,{0:1,1:1}))

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