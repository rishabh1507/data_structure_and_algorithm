def next_letter(li,key):
    start = 0
    end = len(li) -1
    n = len(li)
    res = ""
    while(start<=end):
        mid = start + (end-start)//2
        if(li[mid]==key):
            start = mid + 1
        elif(ord(li[mid])<ord(key)):
            start = mid +1
        else:
            res = li[mid]
            end = mid -1
    
    return res






li = list(input().split())
key = input()
result = next_letter(li,key)
print(result)
