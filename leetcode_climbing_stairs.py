# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# n = 3


def climbStairs(n):
    dict1 = {0:0,1:1,2:2}
    if n in dict1:
        return dict1[n]
    else:
        dict1[n] = climbStairs(n-1) + climbStairs(n-2) 
        return dict1[n]
    
print(climbStairs(2))

