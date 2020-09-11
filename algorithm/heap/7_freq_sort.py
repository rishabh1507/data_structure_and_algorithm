import heapq as hp

def freq_sort(li):
    d1 = {}
    det= []
    heap = []
    hp.heapify(heap)
    
    for i in li:
        if(i not in d1):
            d1[i] = 1
        else:
            d1[i] +=1

    for j in d1.items():
        hp.heappush(heap,[-j[1],j[0]])
    while(len(heap)>0):
        pep = hp.heappop(heap)
        for l in range(-pep[0]):
            print(pep[1],end=" ")
        







li = list(map(int,input().split()))
result = freq_sort(li)
