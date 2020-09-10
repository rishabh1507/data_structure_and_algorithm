def search2d(li,key):
    n = len(li)
    m = len(li[0])
    i = 0
    j = m-1

    while((i>=0 and i<n) and (j>=0 and j<m)):
        if(li[i][j] == key):
            return [i,j]
        
        elif(li[i][j]>key):
            j -=1
        
        elif(li[i][j]<key):
            i +=1
        
    return [-1,-1]


n = int(input())
m = int(input())
# li = [list(map(int,input().split())) for i in range(n)]
li = [[int(input()) for j in range(m)] for i in range(n)]
key = int(input())
result =  search2d(li,key)
print(result)

# 4
# 4
# 10
# 20
# 30
# 40
# 15
# 25
# 35
# 45
# 27
# 29
# 37
# 48
# 32
# 33
# 39
# 50
# 29
