def min_del(st1):
    st1 = st1
    st2 = st1[::-1]
    n = len(st1)
    m = len(st2)
    result1 = len(st1) - lcs(st1,st2,n,m)
    return result1

def lcs(st1,st2,n,m):
    if(n == 0 or m == 0):
        return 0
    if(st1[n-1]==st2[m-1]):
        return 1 + lcs(st1,st2,n-1,m-1)
    else:
        return max(lcs(st1, st2, n, m-1), lcs(st1, st2, n-1, m))


st1 = input()
result = min_del(st1)
print(result)

n = int(input())
li = []
for i in range(n):
    n1 = int(input())
    li.append(list(map(int, input().split())))
li.sort()

print(li)
