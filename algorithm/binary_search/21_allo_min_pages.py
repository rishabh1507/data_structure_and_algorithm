def isValid(li,key,n,mid):
    student = 1
    sum1 = 0

    for i in range(n):
        sum1 = +li[i]
        if(sum1>mid):
            student +=1
            sum1 = li[i]
        if(student>key):
            return False
    return True



def all_pages(li,key):
    start = max(li)
    end = sum(li)
    res = -1
    n = len(li)

    if(n<key):
        return -1

    while(start<=end):
        mid = start +(end-start)//2
        if(isValid(li,key,n,mid)):
            res = mid 
            end = mid -1
        else:
            start = mid +1

    return (sum(li)-res,res)



li = list(map(int,input().split()))
key = int(input())

result = all_pages(li,key)
print(result)