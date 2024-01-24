#You are climbing a staircase. It takes n steps to reach the top.
#Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
def stairs(n):
    two, one = n//2, n

    for i in range(two + 1):
        for j in range(one + 1):
            sum = i * 2 + j
            if sum == n:
                print(i, " times 2 steps +", j, " times 1 steps +")
stairs(10)