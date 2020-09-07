import heapq as hp

def topk(li,k):
    d1 = {}
    heap = []
    hp.heapify(heap)

    for i in li:
        if(i not in d1):
            d1[i] =1
        else:
            d1[i] +=1

    for j in d1.items():
        hp.heappush(heap,[j[1],j[0]])
        if(len(heap)>k):
            hp.heappop(heap)
    while(len(heap)>0):
        print((hp.heappop(heap))[1],end=" ")
    print("")



li = [1,1,1,3,3,2,4,2,4]
k = 2
result = topk(li,k)
print(result)