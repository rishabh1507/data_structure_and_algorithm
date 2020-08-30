def nearest_left(li):
    n = len(li)
    stack = []
    li2 = []

    for i in range(n):
        if(len(stack)==0):
            li2.append(-1)
        elif(len(stack)>0 and li[i]>stack[len(stack)-1]):
            li2.append(stack[len(stack)-1])
        elif(len(stack) > 0 and li[i] < stack[len(stack)-1]):
            while(len(stack) > 0 and li[i] < stack[len(stack)-1]):
                stack.pop()
            if(len(stack)==0):
                li2.append(-1)
            else:
                li2.append(stack[len(stack)-1])
        stack.append(li[i])

    return li2



li = list(map(int,input().split()))
result = nearest_left(li)
print(result)
