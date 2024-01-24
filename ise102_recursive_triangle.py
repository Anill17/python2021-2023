def triangle(start,n):
    if start == n+1:
        return 
    else:
        print("*" * start)
        return triangle(start+1,n)


triangle(1,5)