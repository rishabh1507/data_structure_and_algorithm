def mcm(arr,start,end):
    min1 = float('inf')
    temp_ans=0
    
    if(start>=end):
        return 0

    for k in range(start,end-1):
        temp_ans = mcm(arr,start,k) + mcm(arr,k+1,end) + arr[start-1]*arr[k]*arr[end]
        print(temp_ans,start,k,end)

    if(temp_ans<min1):
        min1 = temp_ans

    return min1

arr = []
n = int(input())
for i in range(n):
    arr.append(int(input()))

start = 1
end = n-1
result = mcm(arr,start,end)
print(result)