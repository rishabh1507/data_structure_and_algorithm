global stack 
stack = []
global ss
ss = []

def push(a):
    stack.append(a)
    if(len(ss)== 0 or ss[len(ss)-1]>=a):
        ss.append(a)
    return

def pop1(a):
    if(len(stack)==0):
        return -1
    ans = stack[len(stack)-1]
    stack.pop()
    if(ss[len(ss)-1]==ans):
        ss.pop()
    return ans

def getMin():
    if(len(ss)==0):
        return -1
    else:
        return ss[len(ss)-1]


push(18)
push(19)
push(29)
push(15)
pop1(15)
push(16)
result = getMin()
print(result)


#for gfg
