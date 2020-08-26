def count_elem(li,x):
    start = 0
    end = len(li)-1
    mid = 0
    res = 0
    res2 = 0

    while(start<=end):
        mid = start + (end-start)//2
        if(li[mid]>x):
            end = mid -1
        elif(li[mid]<x):
            start = mid+1
        else:
            res +=mid
            end = mid - 1

    start  = 0
    end = len(li)-1

    while(start<=end):
        mid = start + (end-start)//2
        if(li[mid]>x):
            end = mid -1
        elif(li[mid]<x):
            start = mid+1
        else:
            res2 +=mid
            start = mid + 1
    
    return res2-res+1




li = list(map(int,input().split()))
x = int(input())

result = count_elem(li,x)
print(result)
