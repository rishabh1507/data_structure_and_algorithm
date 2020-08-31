#function call
def nsr(hist,m):
    st2 = []
    li2 = []

    for i in range(m-1,-1,-1):
        if(len(st2) == 0):
            li2.append(m)
        elif(len(st2) > 0 and st2[len(st2)-1][0] <= hist[i]):
            li2.append(st2[len(st2)-1][1])
        elif(len(st2) > 0 and st2[len(st2)-1][0] >= hist[i]):
            while(len(st2) > 0 and st2[len(st2)-1][0] >= hist[i]):
                st2.pop()
            if(len(st2) == 0):
                li2.append(m)
            else:
                li2.append(st2[len(st2)-1][1])
        st2.append([hist[i], i])

    li2 = li2[::-1]
    return li2

def nsl(hist,m):
    st1 = []
    li1 = []

    for i in range(m):
        if(len(st1)==0):
            li1.append(-1)
        elif(len(st1)>0 and st1[len(st1)-1][0]<hist[i]):
            li1.append(st1[len(st1)-1][1])
        elif(len(st1) > 0 and st1[len(st1)-1][0]>=hist[i]):
            while(len(st1) > 0 and st1[len(st1)-1][0] >=hist[i]):
                st1.pop()
            if(len(st1)==0):
                li1.append(-1)
            else:
                li1.append(st1[len(st1)-1][1])
        st1.append([hist[i],i])

    return li1


# single row
def mah(hist,m):
    width = [0]*m
    area = [0]*m
    right = nsr(hist,m)
    left = nsl(hist,m)
    
    for k in range(m):
        width[k] = right[k] - left[k] -1
        area[k] = hist[k]*width[k]

    return max(area)

# main func
def max_area(bmat,n,m):
    v = []
    for i in range(m):
        v.append(bmat[0][i])
    mx = mah(v,m)

    for i in range(1,n):
        for j in range(m):
            if(bmat[i][j]==0):
                v[j]=0
            else:
                v[j]=v[j]+bmat[i][j]
        mx = max(mx,mah(v,m))
    
    return mx

# main

n = int(input())
m = int(input())

bmat = []

for i in range(n):
    tbmat = []
    for j in range(m):
        tbmat.append(int(input()))
    bmat.append(tbmat)


result = max_area(bmat,n,m)
print(result)
