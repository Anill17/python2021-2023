# n = int(input("please enter the n: ", ))
# t0 = 3
# t1= 5
# list1 = [3,5]
# for i in range(n):
#     tn = ((4*t0) - (2*t1) + 4)
#     list1.append(tn)
#     t0 = t1
#     t1 = tn 
# print(tn)
### iterative method ###

### recursive ###
dict1 = {0:3,1:5}
def func(n):
    
    if n in dict1.keys():
        return dict1[n]
    else:
        s = ((4 * func(n - 2)) - (2 * func(n-1)) + 4)
        dict1[n] = s
        return s
print(func(15))
print(dict1)