# import heapq

# def k_small(li,k):

#     n = len(li)
#     heap = []
#     heapq.heapify(heap)

#     for i in range(n):
#         if(i>k):
#             heapq.heappop(heap)
#         heapq.heappush(heap,-1*li[i])

#     return -heap[1]
        



# li = [7,10,4,3,20,15]
# k = 3
# result= k_small(li,k)
# print(result)

import heapq


def k_small(li, n, k):
    heap = []
    heapq.heapify(heap)

    for i in range(n):
        if(i > k):
            heapq.heappop(heap)
        heapq.heappush(heap, -1*li[i])

    for j in range(1, len(heap)):
        print(-1*heap[j], end=" ")


t = int(input())
for i in range(t):
    n, k = input().split()
    li = list(map(int, input().split()))
    n = int(n)
    k = int(k)
    result = k_small(li, n, k)
