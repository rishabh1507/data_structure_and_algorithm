# dict method

# def egg_drop(e, f):
#     if(f == 0 or f == 0):
#         return f

#     if(e == 1):
#         return f
    
#     key = str(e)+" "+str(f)

#     if(key in d):
#         return d[key]

#     min1 = float('inf')

#     for k in range(1, f+1):
#         temp = 1 + max(egg_drop(e-1, k-1), egg_drop(e-1, f-k))
#         print(temp)

#         min1 = min(temp, min1)

#     d[key] = min1

#     return d[key]

#  arr method

def egg_drop(e,f):
    if(f==0 or f==1):
        return f
    
    if(e==1):
        return f
    
    if(t[e][f] != -1):
        return t[e][f]

    answer = float('inf')

    for k in range(1,f+1):
        temp = 1 + max(egg_drop(e-1, k-1), egg_drop(e, f-k))

        answer = min(answer,temp)
    
    t[e][f] = answer

    return t[e][f]


e = int(input())
f = int(input())
global t 
t = [[-1 for i in range(11)] for j in range(11)]
global d
d = {}
result = egg_drop(e, f)
print(result)
