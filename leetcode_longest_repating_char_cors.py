def characterReplacement(s,k):
    l = 0 

    d = {}
    for r in s:
        if r not in d:
            d[r] = 1 
        else:
            d[r] += 1 

    cells_count = r-l +1 
    if cells_count - max(d.values()) <= k:
        longest_str_len = max(longest_str_len,cells_count)
    else:
        d[s[l]] -= 1 
        l += 1
    return longest_str_len
        



