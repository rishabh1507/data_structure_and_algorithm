def f_l(li,x):
    start = 0
    end = len(li) - 1
    mid1 = 0
    mid2 = 0
    res = 0
    res2 = 0

    while(start<=end):
        mid1 = start + (end-start)//2

        if(li[mid1]>x):
            end = mid1 - 1
        elif(li[mid1]<x):
            start = mid1 +1
        else:
            res=mid1
            end = mid1 - 1
    
    start = 0
    end = len(li)-1

    while(start<=end):
        mid2 = start + (end-start)//2
        print(mid2)

        if(li[mid2]>x):
            end = mid2 - 1
        elif(li[mid2]<x):
            start = mid2 +1
        else:
            res2 = mid2
            start = mid2 + 1

    print(res,res2)
    return res,res2



li = list(map(int, input().split()))
x = int(input())
result1, result2 = f_l(li, x)
print(result1, result2)

#interview bit
we have to make 2 function other wise space issues
