
def egg_drop(e,f):
    if(f==0 or f == 0):
        return f
    
    if(e==1):
        return f
    
    min1 = float('inf')

    for k in range(1,f+1):
        temp = 1 + max(egg_drop(e-1, k-1), egg_drop(e-1, f-k))
        print(temp)

        min1 = min(temp,min1)

    return min1


e = int(input())
f = int(input())
result = egg_drop(e,f)
print(result)
