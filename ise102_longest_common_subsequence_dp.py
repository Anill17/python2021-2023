def lcs(s1,s2):
    dp = list([0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1))

    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1 #??

            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) #???

    
    ans = ""
    for i in dp:
        print(i) 
    for i in range(len(s1)+1,0,-1):
        for j in range(len(s2)+1,0,-1):
            if dp[i-1][j-1] > dp[i-2][j-2]:
                ans += s1[i-2]
    return ans[::-1]
print(lcs("AGGTAB","GXTXAYB"))


### en alt row sola doğru ###