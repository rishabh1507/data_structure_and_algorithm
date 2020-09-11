#nlogn
#n
import heapq as hp

def connect_ropes(li):
    n = len(li)
    heap = []
    hp.heapify(heap)
    sum1 = 0

    for i in range(n):
        hp.heappush(heap,li[i])

    while(len(heap)>1):
        a = hp.heappop(heap)
        b = hp.heappop(heap)
        sum2 = a + b
        sum1 +=sum2
        hp.heappush(heap,sum2)

    return sum1

li = list(map(int,input().split()))
result = connect_ropes(li)
print(result)
