def knapsack(m,n,weight,value):
    if m == 0 or n == 0:
        return 0
    if weight[n-1] > m:
        return knapsack(m,n-1,weight,value)
    else:
        n_include = value[n-1] + knapsack(m-weight[n-1],n-1,weight,value)
        n_exclude = knapsack(m,n-1,weight,value)
        return max(n_include,n_exclude)
    
print(knapsack(10,3,[2,4,6],[2,5,10]))