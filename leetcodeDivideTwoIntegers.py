# without using multiplication, division, and mod operator.


def division(dividend, divisor):
    fnl = 0 
    ct = 0
    for i in range(dividend):
        fnl += divisor 
        ct += 1   
        if fnl == dividend:
            return ct
        if fnl > dividend:
            return ct-1

print(division(10,3))