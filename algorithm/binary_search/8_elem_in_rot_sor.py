def bs(li,start,end):
    n= len(li)
    min1 = 0
    answer = 0
    in1 =0
    in2 = 0
    while(start<=end):
        mid = (start + end)//2
        next1 = (mid +1)%n
        prev = (mid+n-1)%n

        if(li[mid]<= li[next1] and li[mid]<=li[prev]):
            min1 =  mid
            break

        elif(li[mid]<li[end]):
            end = mid - 1
        
        else:
            start = mid + 1

    print(min1)
    
    in1 = bs1(li,0,min1-1)
    in2 = bs1(li,min1,n-1)

    # print(in1)
    # print(in2)

    if(in1 != None):
        answer = in1

    elif(in2 != None):
        answer = in2
    else:
        answer = -1

    return answer


def bs1(li,start1,end1):
    while(start1<=end1):
        mid1 = (start1 + end1)//2

        if(li[mid1]==x):
            return mid1
        elif(li[mid1]<x):
            start1 = mid1 +1
        else:
            end1 = mid1 -1



li = list(map(int,input().split()))
global x
x = int(input())
start = 0 
end = len(li) -1
result = bs(li,start,end)
print(result)
