def order1(li,x):
    start = 0
    mid = 0
    end = len(li)-1
    print(li[0], li[1])

    if(len(li)==1):
        return 1
    

    elif(li[0]>li[1]):
        while(start<end):
            mid = start + (end - start)//2
            print(mid)
            if(li[mid]>x):
                start=mid + 1
            elif(li[mid]<x):
                end = mid - 1
            else:
                return mid
    else:
        while(start<end):
            mid = start + (end - start)//2
            print(mid)
            if(li[mid] > x):
                end = mid - 1
            elif(li[mid] < x):
                start = mid + 1
            else:
                return mid
        

li = list(map(int, input().split()))
x = int(input())
print(order1(li,x))
