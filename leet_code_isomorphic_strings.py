s = "egg"
t = "add"

def iso(s,t):
    map1 = list()
    map2 = list()

    for i in s:
        map1.append(s.index(i))
    for i in t:
        map2.append(t.index(i))

    return map1 == map2


print(iso("egg", "add"))