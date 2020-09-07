import heapq


def klarge(li,k):
    n = len(li)
    heap = []
    heapq.heapify(heap)

    for i in range(n):
        heapq.heappush(heap,li[i])
        if(i>k):
            heapq.heappop(heap)

    print(len(heapq))

    for j in range(len(heap),1,-1):
        print(heap[j-1],end=" ")



li = [7,10,4,3,20,15]
k = 3
result = klarge(li,k)
print(result)


# def klarge(li, n, k):
#     heap = []
#     heapq.heapify(heap)

#     for i in range(n):
#         heapq.heappush(heap, li[i])
#         if(len(heap) > k):
#             heapq.heappop(heap)

#     out = heapq.nlargest(k, heap)
#     for j in out:
#         print(j, end=" ")
#     print("")


# t = int(input())
# for i in range(t):
#     n, k = input().split()
#     li = list(map(int, input().split()))
#     n = int(n)
#     k = int(k)
#     result = klarge(li, n, k)
