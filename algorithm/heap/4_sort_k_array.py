import heapq as hp


def k_sort(li,k):
    n = len(li)
    heap = []
    heap2 = []
    hp.heapify(heap)

    for i in range(n):
        hp.heappush(heap,li[i])

        if(len(heap)>k):
            heap2.append(hp.heappop(heap))

    
    while(len(heap)>0):
        heap2.append(hp.heappop(heap))

    for j in heap2:
        print(j,end=" ")
    print("")

    



        



li = [6,5,3,2,8,10,9]
k = 3
result = k_sort(li,k)
