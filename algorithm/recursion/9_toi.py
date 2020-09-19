#code
def toi(s, d, h, n, k):
    global count
    if(n == 1):
        count += 1
        if(count == k):
            print("{} {}".format(s, d))
        return

    toi(s, h, d, n-1, k)
    count += 1
    if(count == k):
        print("{} {}".format(s, d))
    toi(h, d, s, n-1, k)


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
