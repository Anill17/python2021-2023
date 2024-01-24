def palindrome(x):
    if x < 0 :
        return False
    elif x == 0:
        return True
    else:
        x = str(x)
        
        for i in range(1,len(x)):
            if x[i-1] == x[-i]:
                continue
            else:
                return False
        return True
    

print(palindrome(1221))
            