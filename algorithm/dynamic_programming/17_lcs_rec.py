def lcs(st1,n,st2,m,st):
    if(n==0 or m==0):
        print(st)
        return 0
    elif(st1[n-1]==st2[m-1]):
        st =  st1[n-1] + st  
        return 1+lcs(st1,n-1,st2,m-1,st)
    else:
        return max(lcs(st1,n-1,st2,m,st) , lcs(st1,n,st2,m-1,st))




st1 = input()
n = len(st1)
st2 = input()
st=""
m = len(st2)
result = lcs(st1,n,st2,m,st)
print(result)