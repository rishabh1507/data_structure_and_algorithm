def countSubset(val,W,dp,n):

    for i in range(n):
        dp[i][0] = 1

    for j in range(W):
        dp[0][j] = 0

    for i in range(n):
        for j in range(W):
            if(val[i-1] <=j):
                dp[i][j]= dp[i-1][j] + dp[i-1][j-val[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    print(dp[n][W])


val = [2,3,5,6,8,10]

W = 10
n= len(val) + 1
dp = [[-1 for x in range(W+1)] for x in range(n+1)]
print(dp)
result = countSubset(val,W,dp,n)
print(result)
