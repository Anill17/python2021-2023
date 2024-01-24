def unique_path(m,n):
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return unique_path(m-1,n) + unique_path(m,n-1)
    

print(unique_path(3,7))