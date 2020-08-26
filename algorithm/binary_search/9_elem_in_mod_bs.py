def bs(li,x,start,end):
    n = len(li)

    while(start<end):
        mid = start + (end-start)//2
        if(x==li[mid]):
            return mid

        elif(mid-1>= start and li[mid-1] == x):
            return mid -1
        
        elif(mid+1<= end and li[mid+1] == x):
            return mid +1

        elif(li[mid]<x):
            start= mid+2

        elif(li[mid]>x):
            end = mid-2
            
li = list(map(int,input().split()))
x = int(input())
start = 0
end = len(li)-1
result = bs(li,x,start,end)
print(result)