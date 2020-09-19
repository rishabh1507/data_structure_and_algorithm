#code
def toi(s, d, h, n, k):
    global count
    if(n == 1):
        print(s,d,h,n,k)
        count += 1
        if(count == k):
            print(s, d, h, n, k)
            print("{} {}".format(s, d))
        return

    print(s, d, h, n, k)
    toi(s, h, d, n-1, k)
    print(s, d, h, n, k)

    count += 1
    if(count == k):
        print(s, d, h, n, k)
        print("{} {}".format(s, d))
    toi(h, d, s, n-1, k)
    print(s, d, h, n, k)



t = int(input())
for i in range(t):
    n, k = input().split()
    n = int(n)
    k = int(k)
    s = "1"
    h = "2"
    d = "3"
    count = 0
    toi(s, d, h, n, k)
