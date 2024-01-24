def reverse_int(n):
    reversed_int = 0 
    remainder = 0 
    
    while n>0:
        remainder = n % 10
        reversed_int = reversed_int*10 + remainder
        n = n//10

    return reversed_int

print(reverse_int(1234))