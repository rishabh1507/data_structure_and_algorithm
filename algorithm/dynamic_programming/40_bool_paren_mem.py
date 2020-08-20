def bool_par(st1,i,j,target):
    answer = 0
    if(i>j):
        return False
    if(i==j):
        if(target == True):
            return st1[i]=='T'
        else:
            return st1[i] == 'F'

    temp = str(i)+' '+str(j)+' '+str(target)
    
    if(temp in d):
        print(d[temp],temp)
        return d[temp]
    else:
        for k in range(i+1,j,2):
            lt = bool_par(st1,i,k-1,True)
            lf = bool_par(st1,i,k-1,False)
            rt = bool_par(st1,k+1,j,True)
            rf = bool_par(st1,k+1,j,False)

            if(st1[k]=='&'):
                if(target == True):
                    answer += lt*rt
                else:
                    answer +=lf*rt + lf*rf + lf*rf 
            
            elif(st1[k]=='|'):
                if(target == True):
                    answer +=lt*rt + lt*rf + lf*rt 
                else:
                    answer += lf*rf
            
            elif(st1[k]=='^'):
                if(target == True):
                    answer +=lf*rt + lt*rf  
                else:
                    answer += lt*rt + lf*rt

        d[temp] = answer
    return d[temp]

    pass 



st1 = input()
n = len(st1)
global d
d = {}
result = bool_par(st1,0,n-1,True)
print(result)
