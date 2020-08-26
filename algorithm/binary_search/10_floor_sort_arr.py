def bs1(li,x):
    start = 0
    end = len(li) -1
    n = len(li)
    res =0

    while(start<=end):
        mid = start + (end-start)//2
        if(li[mid] == x):
            return x
        elif(li[mid] <x):
            res = li[mid]
            start = mid +1
        else:
            end = mid -1

    return res


li = list(map(int,input().split()))
x = int(input())
result = bs1(li,x)
print(result)