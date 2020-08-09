def cutRod(price,n):
    T = [0]*(n+1)
    for i in range(1,n+1):
        for j in range(1,i+1):
            T[i] = max(T[i],price[j-1] + T[i-j])
            print(T[i],end=" ")
        print("")
    return T[n] 





length = list(map(int,input().split()))
price = list(map(int,input().split()))
n = 4
print("Output is =",cutRod(price,n))

