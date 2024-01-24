pattern = "CABBCAABBBBCAACBCABBCBACBB"
target = "BBC"
# desired output = 2,9,18
str1 = ""
output = list()
for i in range(len(pattern)-len(target)-1):
    for j in range(len(target)):
        str1 += pattern[i+j]
    if str1 == target:
        output.append(i)
    else:
        str1 = ""


print(output)

