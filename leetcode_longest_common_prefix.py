strs = ["flower","flow","flight"]
def a():

    res = ""
    for i in zip(*strs):
        if len(set(i)) == 1: 
            res += i[0]
        else: 
            return res
    return res

print(a())



#a=["Johnny", "Mike", "Dave"]
#x=zip(*a)
#print(tuple(x))

#Output:
#(('J', 'D', 'M'), ('o', 'a', 'i'), ('h', 'v', 'k'), ('n', 'e', 'e'))

