def mcm(st1,i,j):
    answer = float('inf')
    if(i>=j):
        return 0
    if(palen(st1,i,j)==True):
        return 0
    if(t[i][j] != -1):
        return t[i][j]
    else:
        for k in range(i,j):
            if(t[i][k]!=-1):
                left=t[i][k]
            else:
                left = mcm(st1,i,k)
                t[i][k] = left
            
            if(t[k+1][j]!=-1):
                right=t[k+1][j]
            else:
                right = mcm(st1,k+1,j)
                t[k+1][j] = right

            temp = 1 + left + right

            answer = min(temp,answer)
        
        t[i][j] = answer
        return t[i][j]

def palen(st1,i,j):
    st11 = st1[i:j+1]
    st22 = st11[::-1]
    if(st11 == st22):
        return True
    else:
        return False

st1 = input()
n = len(st1)

global t
t = [[-1 for i in range(n+1)]for j in range(n+1)]
result = mcm(st1,0,n-1)
print(result)