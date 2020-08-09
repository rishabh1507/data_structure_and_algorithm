def coin_change(n,amt):
    coins=[0]*n
    dp = [[0 for i in range(amt+1)] for j in range(n+1)]
    
    for i in range(len(coins)):
        coins[i]=int(input())

    for i in range(n):
        dp[i][0]=0
    for j in range(1,amt+1):
        dp[0][j]= float('inf')-1

    for i in range(1,n+1):
        for j in range(1,amt+1):
            if(coins[i-1]<=j):
                pick = 1 + dp[i-1][j-coins[i-1]]
                drop = dp[i-1][j]
                dp[i][j]= min(pick,drop)
                print(dp[i][j],end= " ")
            else:
                dp[i][j]=dp[i-1][j]
                print(dp[i][j],end=" ")
        print(" ")

    answer = dp[n][amt]
    return answer

    print(dp)

    pass




n = int(input("no of coins "))
amt = int(input("sum acc "))

result = coin_change(n,amt)
print("answer is",result)


