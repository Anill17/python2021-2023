height = [1,8,6,2,5,4,8,3,7]
dict1 = dict()
for i in (height):
    for j in (height):
        if i > j or j > i:
            var1 = min((i,j))
        else:
            var1 = i
        area = var1 * abs(height.index(i) - height.index(j))
        dict1[(i, j)] = area

value_list = list(dict1.values())
key_list = list(dict1.keys())
print(value_list)
print(max(value_list))