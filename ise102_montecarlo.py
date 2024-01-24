import random
# r = int(input("please enter the r of the circle: ", ))
# range_val = 10**6 ## 10**7 will provide us more precise answer but it will be slower.
# iter = 0 
# ct = 0 
# while iter <  range_val:
#     x = random.uniform(-r,r)
#     y = random.uniform(-r,r)
#     iter += 1 
#     hipo = (x**2 + y**2)**0.5
#     if hipo < r:
#         ct += 1
    
# area_circle = ct
# area_square = range_val
# pi = (area_circle / area_square) * 4

# print(pi)

# print("================================================================",end="\t")

def func(x):
    return x**2

range_val = 10**6 ## 10**7 will provide us more precise answer but it will be slower.
iter = 0 
ct = 0 


while iter < range_val:
    x = random.uniform(3,7)
    y = random.uniform(0,50)
    iter += 1 
    if y < func(x):
        ct += 1

total_area = 200
area_under_curve = total_area * (ct / range_val)
print("area under the curve is: {}".format(area_under_curve))