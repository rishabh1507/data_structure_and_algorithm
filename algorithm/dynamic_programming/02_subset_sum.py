
# recursion
"""

def subsetSum(val,n,sum):
    if(sum==0):
        return True
    if(n<0):
        return False
    else:
        include = subsetSum(val,n-1,sum-val[n])
        exclude = subsetSum(val, n-1, sum)

        return include or exclude 



val = [7,3,2,5,8]
n = len(val)
sum = 14
result = subsetSum(val,n-1,sum)
print(result)

"""
# recursion memoization

def subsetSum(val,dp,n,sum):
    m,n = len(val)+1 , sum +1
    T = [[False for x in range(n)] for x in range(m)]
    for i in range(n+1):
        T[i][0] = True

    for i in range(1,m+1):
        for j in range(1,n+1):
            if(val[i-1]>j):
                T[i][j] = T[i-1][j]
            else:
                T[i][j] = T[i-1][j] or T[i-1][j-A[i-1]]

        return T[n][sum]
    
    if(val[n-1]<sum):
        include = subsetSum(val,dp,n-1,sum-val[n])
        exclude = subsetSum(val,dp, n-1, sum)

        if(pick or drop):
            dp[n][sum] = 1
        else:
            dp[n][sum] = 0
        return include or exclude




val = [7,3,2,5,8]
n = len(val)
sum = 14
result = subsetSum(val,sum)
print(result)
