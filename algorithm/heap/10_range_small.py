import heapq as hp

def ksmall(li,k1,k2):
    heap = []
    n = len(li)
    sum1 = 0
    hp.heapify(heap)

    for k in range(n):
        hp.heappush(heap,-1*li[k])
    print(heap)
    li1 = hp.nlargest(k1,heap)
    li2 = hp.nlargest(k2,heap)
    print(li1,li2)


    for j in range(n):
        if(li[j]>=-li1[-1] and li[j]<=-li2[-1]):
            sum1 += li[j]
    
    return sum1



li = list(map(int,input().split()))
k1 = int(input())
k2 = int(input())
result = ksmall(li,k1,k2)
print(result)


#gfg

"""
#code

def ksmall(li, k1, k2, n):
    heap = []
    sum1 = 0
    hp.heapify(heap)

    for k in range(n):
        hp.heappush(heap, -1*li[k])

    li1 = hp.nlargest(k1, heap)
    li2 = hp.nlargest(k2, heap)

    for j in range(n):
        if(li[j] > -li1[-1] and li[j] < -li2[-1]):
            sum1 += li[j]

    return sum1


t = int(input())
for m in range(t):
    n1 = int(input())
    li = list(map(int, input().split()))
    k1, k2 = input().split()
    k1 = int(k1)
    k2 = int(k2)
    result = ksmall(li, k1, k2, n1)
    print(result)


"""