def middle(stack, k):
    if(k == 0):
        return
    temp = stack.pop(len(stack)-1)
    middle(stack, k-1)
    stack.insert(0,temp)


stack = list(map(int, input().split()))
k = len(stack)
result = middle(stack, k)
print(stack)
