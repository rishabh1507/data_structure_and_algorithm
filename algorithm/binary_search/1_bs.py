def bs(li,x):
    start = 0
    end = len(li)-1
    mid = 0

    while(start < end):
        mid = (start + end)//2
        if(li[mid]>x):
            end = mid -1
        elif(li[mid]<x):
            start = mid + 1
        else:
            return mid 


li = list(map(int,input().split()))
x = int(input())
result = bs(li,x)
print(result)