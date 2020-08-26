def no_sort(li):
    start = 0
    end = len(li) - 1
    n = len(li)
    answer = 0
    
    while(start<=end):
        mid = start + (end -start)//2
        next1 = (mid + 1)%n
        prev = (mid + n -1)%n
        print('')
        print(start,end,mid,next1,prev)

        if(li[mid]<=li[next1] and li[mid]<= li[prev]):
            answer = mid
            break
        
        elif(li[mid]<li[end]):
            end = mid - 1
        
        else:
            start = mid + 1
    
    return answer



li = list(map(int,input().split()))
result = no_sort(li)
print(result)