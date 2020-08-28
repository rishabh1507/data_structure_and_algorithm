def bio_max(li):
    n = len(li)
    start = 0
    end = n-1

    while(start<=end):
        mid = start + (end - start)//2

        if(mid>0 and mid <n-1):
            if(li[mid]>li[mid-1] and li[mid]>li[mid+1]):
                return li[mid]
            elif(li[mid]<li[mid-1]):
                end = mid -1
            else:
                start = mid +1
        
        elif(mid==0):
            if(li[0]>li[1]):
                return li[0]
            else:
                return li[1] 
        
        elif(mid==n-1):
            if(li[n-1]>li[n-2]):
                return li[n-1]
            else:
                return li[n-2] 



li = list(map(int,input().split()))
result = bio_max(li)
print(result)