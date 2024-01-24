def knapsack(n,W,wt,value):
    s = list([0 for _ in range(W+1)] for _ in range(n+1))

    for i in range(n+1):
        for w in range(W+1):
            if i == 0 and w == 0:
                s[i][w] = 0
            elif wt[i-1] <= w:
                s[i][w] = max(value[i-1] + s[i-1][w-wt[i-1]], s[i-1][w])
            else:
                s[i][w] = s[i-1][w]

    return s[n][w]

#print(knapsack(3,50,[10,20,30],[60,100,120]))

### other variation

def knapsack_dp(n,W,wt,value):
    s = list(0 for _ in range(W+1))
    
    for i in range(1,n+1):
        for j in range(W,0,-1):
            if wt[i-1] <= j:
                s[j] = max(s[j],value[i-1] + s[j - wt[i-1]])
    
    print(s)

knapsack_dp(3,50,[10,20,30],[60,100,120])



