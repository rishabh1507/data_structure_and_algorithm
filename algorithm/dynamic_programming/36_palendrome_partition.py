def mcm(st1,i,j):
    answer = float('inf')

    if(i>=j):
        return 0
    if(palendrome(st1,i,j) == True):
        return 0

    for k in range(i,j):
        left = mcm(st1,i,k)
        right = mcm(st1,k+1,j)
        temp_ans = 1 + left + right
        answer = min(temp_ans,answer)
        print(answer)
    
    return answer

def palendrome(st1,i,j):
    st11 = st1[i:j+1]
    st22 = st11 [::-1]
    if(st11 == st22):
        return True
    else:
        return False

st1 = input()
n = len(st1)
result = mcm(st1,0,n-1)
print(result)