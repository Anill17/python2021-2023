haystack = "sadbutsad"
needle = "sad"
test_str = ""
for i in range(len(haystack)):
    for j in range(1,len(haystack)):
        if haystack[i:j] == needle:
            print(i)
    

        
