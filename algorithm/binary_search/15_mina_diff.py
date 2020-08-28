def min_diff(li,key):
    start = 0
    end = len(li)-1
    mid = 0
    while(start<=end):
        mid = start + (end -start)//2
        if(li[mid] == key ):
            return li[mid]
        elif(li[mid] > key ):
            end = mid -1
        else:
            start = mid +1
    
    if(abs(li[start]-key)<abs(li[end]-key)):
        return li[start]
    else:
        return li[end]

li = list(map(int,input().split()))
key = int(input())
result = min_diff(li,key)
print(result)