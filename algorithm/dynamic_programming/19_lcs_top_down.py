"""
def lcs(st1,st2,m,n,t):
    # for i in range(1,m+1):
    #     for j in range(1,n+1):
    #         if(i == 0 or j== 0):
    #             t[i][j] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(st1[i-1] == st2[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i-1][j],t[i][j-1])
    return t[m][n]
st1 = input()
m = len(st1)
st2 = input()
n = len(st2)

t = [[0 for i in range(m+1)] for j in range(n+1)]
print(t)


result = lcs(st1,st2,m,n,t)
print(result)
"""
def lcs(st1,st2):
    n = len(st1)
    m = len(st2)

    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                t[i][j] = 0
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(st1[i-1]==st2[j-1]):
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])
                
    return t[n][m]

    pass

st1 = input()
n = len(st1)
st2 = input()
m = len(st2)
global t
t = [[-1 for i in range(m+1)] for j in range(n+1)] 
result = lcs(st1,st2)
print(result)
