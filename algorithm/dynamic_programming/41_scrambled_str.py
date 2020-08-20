def isScramble(a,b):
    n=len(a)
    m=len(b)
    flag = False
    if(a==b):
        return True
    if(n<=1):
        return False

    for i in range(1,n):
        swap = False
        nswap = False
        
        if(isScramble(a[0:i], b[n-i:i]) and isScramble(a[i:n-i], b[0:n-i])):
            swap = True
        if(isScramble(a[0:i], b[0:i]) and isScramble(a[i:n-i], b[i:n-i])):
            nswap =True

        if(swap or nswap):
            flag=True
            break

    return flag

    



a = input()
b = input()
n = len(a)
m = len(b)

# if(n != m):
#     print("no")
# elif(a == b):
#     print("yes")
if(isScramble(a,b)):
    print("yes")
else:
    print("no")
