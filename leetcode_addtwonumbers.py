#l1 = [9,9,9,9,9,9,9]
#l2 = [9,9,9,9]
#l3 = [8,9,9,9,0,0,0,1]
l1 = [2,4,3]
l2 = [5,6,4]

l3 = list()
elde = 0 


if len(l1) > len(l2):
    diff = len(l1) - len(l2)
    for i in range(diff):
        l2.append(0)
if len(l1) < len(l2):
    diff = len(l2)- len(l1)
    for i in range(diff):
        l1.append(0)


for i in range(len(l1)):
    var1 = l1[i] + l2[i] + elde
    elde = 0
    if var1 >= 10:
        var1 = var1 % 10
        elde = 1
        l3.append(var1)
    else:
        l3.append(var1)
if elde != 0:
    l3.append(elde)
print(l3)

    