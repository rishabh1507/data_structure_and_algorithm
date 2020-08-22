def egg_drop(e,f):
    if(f==0 or f==1):
        return f
    if(e==1):
        return f
    if(t[e][f] != -1):
        return t[e][f]

    answer = float('inf')
    low = 0
    high = 0
    for k in range(1,f+1):
        if(t[e-1][k-1] != -1):
            low = t[e-1][k-1]
        else:
            low = egg_drop(e-1,k-1)
        if(t[e][f-k] != -1):
            high = t[e][f-k]
        else:
            high = egg_drop(e,f-k)
        
        temp = 1+ max(low,high)
        print(temp)
        answer = min(temp,answer)
    
    t[e][f] = answer

    return t[e][f] 



e = int(input())
f = int(input())

global t 
t = [[-1 for i in range(11)]for j in range(11)]
result = egg_drop(e,f)
print(result)
