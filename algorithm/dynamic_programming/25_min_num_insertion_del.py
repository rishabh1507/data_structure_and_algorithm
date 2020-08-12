def lcs(st1,st2,n,m,t):
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

def min_ins_del(st1, st2, n, m, t):
    lcs1 = lcs(st1, st2, n, m, t)

    print("Number of Deletion :",(n-lcs1))
    print("Number of Insertion :",(m-lcs1))


    

st1 = input()
n = len(st1) 

st2 = input()
m = len(st2)

t = [[-1 for i in range(m+1)] for j in range(n+1)]


result = min_ins_del(st1,st2,n,m,t)
