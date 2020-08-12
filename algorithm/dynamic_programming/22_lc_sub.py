def lcsub(st1,st2):
    n = len(st1)
    m = len(st2)

    store = 0

    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                t[i][j]=0
                
    for i in range(1,n+1):
        for j in range(1,m+1):
            if(st1[i-1]==st2[j-1]):
                t[i][j] = t[i-1][j-1] + 1
                # max statement can be used result = max(result, LCSuff[i][j])
                if(t[i][j]>store):
                    store =t[i][j]
            else:
                t[i][j] = 0

    # print(t)
    return store
    # return (t[i][j])

    




st1 = input()
n = len(st1)
st2 = input()
m = len(st2)
global t 
t = [[-1 for i in range(m+1)] for j in range(n+1)]
result = lcsub(st1,st2)
print(result)
