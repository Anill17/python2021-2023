def daily(temperatures):
    l = 0 
    r = 1
    output = [0] * len(temperatures)

    while l < len(temperatures) -1:
        if r == len(temperatures)-1 and temperatures[r]< temperatures[l]:
            l += 1
            r = l+1
        elif temperatures[l] == temperatures[l+1]:
            l+= 1
            r = l+1
        elif temperatures[l] < temperatures[l+1] and len(temperatures) -1  == l+1:
            output[l] = 1
            l+= 1
            r = l+1
        elif temperatures[r] > temperatures[l]:
            output[l] = r-l
            l += 1
            r = l+1
        else:
            r += 1
    return output

print(daily([55,38,53,81,61,93,97,32,43,78]))