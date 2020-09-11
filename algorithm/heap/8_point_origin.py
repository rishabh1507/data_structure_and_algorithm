import heapq as hp
def kClosest(points,K):
    heap = []
    n = len(points)
    hp.heapify(heap)
    heap2 = []
    
    for i in range(n):
        hp.heappush(heap,[-(points[i][0]*points[i][0]+points[i][1]*points[i][1]),points[i]])

        if(len(heap)>K):
            hp.heappop(heap)

    while(len(heap)>0):
        heap2.append(hp.heappop(heap)[1])

    print(heap2[::-1])

    
# points = [[3, 3], [5, -1], [-2, 4]]
# K = 2
#custom
n = int(input())
points = [[int(input()) for j in range(2)] for i in range(n)]
K= int(input())
result = kClosest(points,K)
