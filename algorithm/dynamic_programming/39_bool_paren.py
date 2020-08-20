def bool_par(st1,i,j,target):
    # bc
    if(i>j):
        return False
    if(i==j):
        if(target==True):
            return (st1[i] == 'T')
        else:
            return(st1[i] == 'F')
    answer = 0

    for k in range(i+1,j,2):
        lt = bool_par(st1,i,k-1,True)
        lf = bool_par(st1,i,k-1,False)
        rt = bool_par(st1,k+1,j,True)
        rf = bool_par(st1,k+1,j,False)

        if(st1[k] == "&"):
            if(target == True):
                answer += lt*rt
                print(answer)
            else:
                answer +=(lf*rf) + (lf*rt) + (lt*rf)
                print(answer)

        elif(st1[k] == "|"):
            if(target == True):
                answer +=(lt*rt) + (lf*rt) + (lt*rf)
                print(answer)

            else:
                answer += lf*rf
                print(answer)

        
        else:
            if(target == True):
                answer += (lt*rf) + (lf*rt)
                print(answer)

            else:
                answer +=(lt*rt) + (lf*rf)
                print(answer)

    
    return answer

st1 = input()
n=len(st1)
result = bool_par(st1,0,n-1,True)
print(result)
