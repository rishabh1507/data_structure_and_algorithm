def small_right(li):
    n = len(li)
    stack = []
    rev_li = []

    for i in range(n-1,-1,-1):
        if(len(stack)==0):
            rev_li.append(-1)
        elif(len(stack)>0 and li[i]>stack[len(stack)-1]):
            rev_li.append(stack[len(stack)-1])
        elif(len(stack) > 0 and li[i] < stack[len(stack)-1]):
            while(len(stack) > 0 and li[i] <stack[len(stack)-1]):
                stack.pop()
            if(len(stack)==0):
                rev_li.append(-1)
            else:
                rev_li.append(stack[len(stack)-1])
        stack.append(li[i])
    return rev_li[::-1]

                


li = list(map(int,input().split()))
result = small_right(li)
[print(i) for i in result]
