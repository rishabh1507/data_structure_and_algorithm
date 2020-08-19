def mcm(st1,i,j):

    answer = float('inf')
    
    if(i>=j):
        return 0
    
    if(t[i][j] != -1):
        return t[i][j]
    
    elif(palen(st1,i,j)==True):
        return 0
    
    else:
        for k in range(i,j):
            left = mcm(st1,i,k)
            right = mcm(st1,k+1,j)
            temp = 1 + left +right

            answer = min(answer,temp)
            print(temp)

        t[i][j] = answer
        return t[i][j]

def palen(st1,i,j):
    if(i==j):
        return True
    if(i>j):
        return True
    while(i<j):
        if(st1[i]!=st1[j]):
            return False
        i +=1
        j -=1
    return True

st1 = input()
n = len(st1)

global t
t = [[-1 for i in range(n+1)] for j in range(n+1)]

result = mcm(st1,0,n-1)
print(result)
print(t)
