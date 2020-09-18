def middle(stack,k):
    if(k==1):
        stack.pop(len(stack)-1)
        return
    temp = stack.pop(len(stack)-1)
    middle(stack,k-1)
    stack.append(temp)

stack = list(map(int,input().split()))
k = len(stack)//2 +1

result = middle(stack,k)
print(stack)
