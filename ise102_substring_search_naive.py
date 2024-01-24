def naive_search(arr,text):
    m = len(arr)
    n = len(text)


    for i in range(n-m+1):
        j = 0
        while j < m:

            if text[i+j] == arr[j]:
                break

            j += 1

        if j == m:
            print("found a match in index %s" %i)


naive_search("xxxtenetxx","tenet")