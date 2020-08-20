def solve(a,b):
    n = len(a)
    flag = False
    key = str(a)+" "+str(b)

    if(len(a) != len(b)):
        return False
    if(a==b):
        return True
    if(n<=1):
        return False
    if( key in d):
        return d[key]

    for i in range(1,n):
        swap=False
        nswap =False
        swap = (solve(a[:i],b[-i:]) and solve(a[i:],b[:-i]))
        nswap = (solve(a[:i], b[:i]) and solve(a[i:], b[i:]))
        if(swap or nswap):
            flag = True
            break
        d[key] = flag
    
    return flag
    
    
    

a = input()
b = input()
global d
d ={}

result = solve(a,b)
print(result)

