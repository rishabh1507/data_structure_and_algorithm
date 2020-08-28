def bs(li,start1,end1):
    n1 = len(li)

    while(start1<end1):
        mid1 = start1 + (end1 - start1)//2
        if(li[mid1]== key):
            return mid1

        elif(li[mid1]>key):
            end1 = mid1 -1

        else:
            start1 = mid1 + 1
    return -1


def bs2(li,start2,end2):
    n2 = len(li)

    while(start2<end2):
        mid2 = start2 + (end2 - start2)//2
        if(li[mid2]== key):
            return mid2

        elif(li[mid1]>key):
            start2 = mid2 + 1

        else:
            end2 = mid2 -1

    return -1

def search_bio(li,key):
    n = len(li)
    start = 0
    end = len(li)-1
    temp_ans = 0
    while(start<=end):
        mid = start + (end - start)//2
        
        if(mid>0 and mid<n-1):
            if(li[mid]>li[mid-1] and li[mid]>li[mid+1]):
                temp_ans = mid
                break 
            elif(li[mid]<li[mid-1]):
                end = mid -1
            else:
                start = mid +1
                
        elif(mid==0):
            if(li[0]>li[1]):
                temp_ans = 0
                break
            else:
                temp_ans = 1
                break 
        
        elif(mid==n-1):
            if(li[n-1]>li[n-2]):
                temp_ans = n-1
                break
            else:
                temp_ans = n-2
                break

    result1 = bs(li,0,temp_ans-1)
    result2 = bs2(li,temp_ans,n-1)

    if(result1 == -1 and result2 == -1 ):
        return -1
    elif(result1 == -1 and result2 != -1 ):
        return result2
    else:
        return result1

        

li = list(map(int,input().split()))
global key
key = int(input())
result = search_bio(li,key)
print(result)