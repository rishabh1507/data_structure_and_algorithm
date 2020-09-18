import math
def kelem(n,k):
    if(n==1 and k==1):
        return 0

    mid = math.pow(2,n-1)//2
    print(mid)

    if(k<=mid):
        return kelem(n-1,k)
    else:
        return  not kelem(n-1, k-mid)




n = int(input())
k = int(input())
result = kelem(n,k)
if(result == False):
    print(0)
else:
    print(1)
