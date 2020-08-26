def bs(li,x):
    start = 0
    end = len(li) - 1
    n = len(li)
    res = 0

    while(start<=end):
        mid = start +(end -start)//2
        
        if(li[mid]== x):
            return x
        
        elif(li[mid]<x):
            start = mid +1
        else:
            res = li[mid]
            end = mid -1

    return res



li = list(map(int,input().split()))
x = int(input())

result = bs(li,x)
print(result)