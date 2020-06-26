#recursive

"""
def knapSack(W,wt,val,n):
    if(n==0 or W==0):
        return 0
    if(wt[n-1] > W):
        return knapSack(W,wt,val,n-1)
    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1))

val = [60,100,120]
wt = [10,20,30]
W = 50
n = len(val)

result = knapSack(W,wt,val,n)
print(result)

"""

# recursive + memoziation

def knapSack(wt,val,dp,W, n):
    if(n == 0 or W == 0):
        return 0
    if(dp[n][W] != -1):
        return dp[n][W]
    if(wt[n-1] <= W):
        pick = val[n-1] + knapSack(wt,val,dp,W-wt[n-1],n-1)
        drop = knapSack(wt,val,dp,W,n-1)
        dp[n][W] = max(pick,drop)
        return dp[n][W]
    else:
        dp[n][W] = knapSack(wt, val, dp, W, n-1)
        return dp[n][W]





val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
dp = [[-1 for x in range(W+1)] for x in range(n+1)] 
print(dp)

result = knapSack(wt, val, dp,W,n)
print(result)


#top-down approach

