def greater_right(li,n):
    stack = []
    rev_li = []

    for i in range(n-1,-1,-1):
        if(len(stack) == 0):
            rev_li.append(-1)
        elif(len(stack)>0 and stack[len(stack)-1]>li[i]):
            rev_li.append(stack[len(stack)-1])
        elif(len(stack) > 0 and stack[len(stack)-1] <= li[i]):
            while(len(stack) > 0 and stack[len(stack)-1] <= li[i]):
                stack.pop()
            if(len(stack)==0):
                rev_li.append(-1)
            else:
                rev_li.append(stack[len(stack)-1])
        
        stack.append(li[i])

    rev_li.reverse()

    return rev_li



li = list(map(int,input().split()))
n = len(li)

result = greater_right(li,n)
print(result)
