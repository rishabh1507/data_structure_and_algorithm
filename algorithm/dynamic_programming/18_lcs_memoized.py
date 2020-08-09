def lcs(st1,st2,n,m):
    if(n==0 or m==0):
        return 0
        
    if(t[n][m]!=-1):
        return t[n][m]

    if(st1[n-1]==st2[m-1]):
        t[n][m] = 1 + lcs(st1,st2,n-1,m-1)
        return t[n][m]
    else:
        pick = lcs(st1, st2, n, m-1)
        drop = lcs(st1, st2, n-1, m)
        t[n][m] = max(pick,drop )
        return (t[n][m])

st1 = input()
st2 = input()

n = len(st1)
m = len(st2)
global t
t = [[-1 for i in range(m+1) ] for j in range(n+1)]

result=lcs(st1,st2,n,m)
print(result)
