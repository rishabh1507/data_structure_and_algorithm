def rec(n):
    if(n == 1):
        print(n, end=" ")
        return
    print(n, end=" ")
    rec(n-1)


t = int(input())
for i in range(t):
    n = int(input())
    result = rec(n)
    print("")
