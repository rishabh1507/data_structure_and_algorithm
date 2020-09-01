def rain_water(li,n2):
    mxl = [0]*n2
    mxr = [0]*n2

    mxl[0] = li[0]
    
    for i in range(1,n2):
        mxl[i]=max(mxl[i-1],li[i])

    mxr[n2-1] = li[n2-1]
    for j in range(n2-2,-1,-1):
        mxr[j] = max(mxr[j+1], li[j])

    water=[0]*n2
    

    for k in range(n2):
        water[k] = (min(mxl[k],mxr[k])-li[k])
    

    return sum(water)





    


n1 = int(input())
for i in range(n1):
    n2 = int(input())
    li = list(map(int,input().split()))
    result = rain_water(li,n2)
    print(result)

