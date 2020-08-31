def max_area(li):
    n = len(li)
    idx1 = []
    idx2 = []
    stack = []
    width = []
    answer = 0
    result1 = []

    # NSL
    for i in range(n):
        if(len(stack)==0):
            idx1.append(-1)
        elif(len(stack)>0 and stack[len(stack)-1][0]<li[i]):
            idx1.append(stack[len(stack)-1][1])
        elif(len(stack)>0 and stack[len(stack)-1][0]>li[i]):
            while(len(stack)>0 and stack[len(stack)-1][0]>li[i]):
                stack.pop()
            if(len(stack)==0):
                idx1.append(-1)
            else:
                idx1.append(stack[len(stack)-1][1])
        stack.append([li[i],i])

    stack=[]

    #NSR
    for j in range(n-1,-1,-1):
        if(len(stack)==0):
            idx2.append(n)
        elif(len(stack)>0 and stack[len(stack)-1][0]<li[j]):
            idx2.append(stack[len(stack)-1][1])
        elif(len(stack)>0 and stack[len(stack)-1][0]>li[j]):
            while(len(stack)>0 and stack[len(stack)-1][0]>li[j]):
                stack.pop()
            if(len(stack)==0):
                idx2.append(n)
            else:
                idx2.append(stack[len(stack)-1][1])
        stack.append([li[j],j])

    idx2=idx2[::-1]

    for k in range(n):
        width.append(idx2[k] - idx1[k] -1)
    
    for m in range(n):
        answer = max(answer,li[m]*width[m])

    return answer



li = list(map(int,input().split()))
result = max_area(li)
print(result)