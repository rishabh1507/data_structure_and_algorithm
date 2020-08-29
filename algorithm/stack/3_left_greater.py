def left_great(li):
    stack = []
    li2 = []
    n = len(li)

    for i in range(n):
        if(len(stack)==0):
            li2.append(-1)
        elif(len(stack) > 0 and stack[len(stack)-1]>li[i]):
            li2.append(stack[len(stack)-1])
        elif(len(stack) > 0 and stack[len(stack)-1] < li[i]):
            while(len(stack) > 0 and stack[len(stack)-1] < li[i]):
                stack.pop()
            if(len(stack)==0):
                li2.append(-1)
            else:
                li2.append(stack[len(stack)-1])
        
        stack.append(li[i])

    return li2

li = list(map(int, input().split()))
result = left_great(li)
print(result) 
