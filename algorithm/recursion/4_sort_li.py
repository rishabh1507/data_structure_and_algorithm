def Sort(li):
    if(len(li)==0):
        return
        
    temp = li[len(li)-1]
    li.pop(len(li)-1)
    Sort(li)
    Insert(li,temp)

def Insert(li,temp):
    if(len(li)==0 or li[len(li)-1]<=temp):
        li.append(temp)
        return
    val = li[len(li)-1]
    li.pop(len(li)-1)
    Insert(li,temp)
    li.append(val)
    return

li = list(map(int,input().split()))
Sort(li)
print(li)
