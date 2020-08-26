def rev_bs(li,x):
    start = 0
    end = len(li) - 1
    mid = 0

    while(start < end):
        mid = start + (end - start)//2

        if(li[mid]>x):
            start = mid + 1
        elif(li[mid]<x):
            end = mid - 1
        else:
            return mid
li = list(map(int,input().split()))
x = int(input())

result = rev_bs(li,x)
print(result)
