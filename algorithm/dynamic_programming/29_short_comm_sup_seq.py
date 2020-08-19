def scs(st1,st2):
    n = len(st1)
    m = len(st2)
    s = ""

    for i in range(n+1):
        for j in range(m+1):
            if(i==0 or j==0):
                t[i][j]=0

    for i in range(n+1):
        for j in range(m+1):
            if(st1[i-1]==st2[j-1]):
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1],t[i-1][j])

    i = n
    j = m

    while(i>0 and j>0):
        if(st1[i-1]==st2[j-1]):
            s = st1[i-1] + s
            i -=1
            j -=1
        else:
            if(t[i][j-1]>t[i-1][j]):
                s = st2[j-1] + s
                j -=1
            elif(t[i-1][j]>t[i][j-1]):
                s = st1[i-1] + s
                i -=1
    
    while(i>0):
        s = st1[i-1] + s
        i -=1
    
    while(j>0):
        s = st2[j-1] + s
        j -=1

    return s
            

st1 = input()
st2 = input()

n = len(st1)
m = len(st2)

global t

t = [[-1 for i in range(m+1)] for j in range(n+1)]

result = scs(st1,st2)
print(result)
