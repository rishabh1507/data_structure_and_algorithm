# def stock_span(li):
#     n = len(li)
#     li2 = []
#     stack = []
#     count = 0

#     for i in range(n):
#         if(len(stack) == 0):
#             li2.append(1)
#         elif(len(stack)>0 and stack[len(stack)-1][0]>li[i]):
#             li2.append(1)
#         elif(len(stack)>0 and stack[len(stack)-1][0]<=li[i]):
#             for j in range(len(stack)-1,-1,-1):
#                 if(stack[j][0]>li[i]):
#                     li2.append(abs(i-stack[j][1]))
#                     break
#                 elif(j==0 and stack[j][0]<li[i]):
#                     li2.append(abs(i-0))

#         stack.append([li[i],i])

#     return li2




# li = list(map(int,input().split()))
# result = stock_span(li)
# print(result)



def stock_span(li):
    n = len(li)
    li2 = []
    stack = []
    count = 0

    for i in range(n):
        if(len(stack) == 0):
            li2.append(-1)
        elif(len(stack)>0 and stack[len(stack)-1][0]>li[i]):
            li2.append(stack[len(stack)-1][1])
        elif(len(stack)>0 and stack[len(stack)-1][0]<=li[i]):
            while(len(stack)>0 and stack[len(stack)-1][0]<=li[i]):
                stack.pop()
            if(len(stack)==0):
                li2.append(-1)
            else:
                li2.append(stack[len(stack)-1][1])
                
        stack.append([li[i],i])
            
    for i in range(len(li2)):
        li2[i] = abs(i-li2[i])


    return li2




li = list(map(int,input().split()))
result = stock_span(li)
for j in result:
    print(j,end= " ")


# gfg
# for k in range(n1):
#     n2= int(input())
#     li = list(map(int,input().split()))
#     result = stock_span(li)
#     for j in result:
#         print(j,end=" ")
#     print("")