import heapq as hp


def close_num(li, x, k):
    n = len(li)
    heap = []
    hp.heapify(heap)

    for i in range(n):
        hp.heappush(heap, [-abs(li[i]-x), -1*li[i]])
        print(heap)
        if(len(heap) > k):
            hp.heappop(heap)
            print(heap)

    while(len(heap) > 0):
        print(-hp.heappop(heap)[1], end=" ")
    print("")


x, k = input().split()
x = int(x)
k = int(k)
li = list(map(int, input().split()))
close_num(li, x, k)

# 5 3
# 10 2 14 4 7 6
# [[-5, -10]]
# [[-5, -10], [-3, -2]]
# [[-9, -14], [-3, -2], [-5, -10]]
# [[-9, -14], [-3, -2], [-5, -10], [-1, -4]]
# [[-5, -10], [-3, -2], [-1, -4]]
# [[-5, -10], [-3, -2], [-1, -4], [-2, -7]]
# [[-3, -2], [-2, -7], [-1, -4]]
# [[-3, -2], [-2, -7], [-1, -4], [-1, -6]]
# [[-2, -7], [-1, -6], [-1, -4]]
# 7 6 4
