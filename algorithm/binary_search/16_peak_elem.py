def peak_elem(li):
    low = 0
    high = len(li) -1
    n = len(li)

    while(low<=high):
        mid = low +(high-low)//2
        if(mid>0 and mid<n-1):
            if(li[mid] > li[mid-1] and li[mid]>li[mid+1]):
                return mid
            elif(li[mid-1]>li[mid]):
                high = mid -1
            else:
                low = mid+1
        
        elif(mid==0):
            if(li[0]>li[1]):
                return 0
            else:
                return 1
        
        elif(mid == n-1):
            if(li[n-1]>li[n-2]):
                return n-1
            else:
                return n-2

li = list(map(int,input().split()))
result = peak_elem(li)
print(result)