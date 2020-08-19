
def checkSum(sumLeft, k):

	r = True
	for i in range(k):
		if sumLeft[i]:
			r = False

	return r

def subsetSum(S, n, sumLeft, A, k):
	
	if checkSum(sumLeft, k):
		return True	
	if n < 0:
		return False

	result = False

	for i in range(k):
		if not result and (sumLeft[i] - S[n]) >= 0:			
			A[n] = i + 1
			sumLeft[i] = sumLeft[i] - S[n]
			result = subsetSum(S, n - 1, sumLeft, A, k)
			sumLeft[i] = sumLeft[i] + S[n]
	return result



def partition(S, k):
	n = len(S)

	if n < k:
		print("k-Partition of set S is not Possible")
		return

	total = sum(S)
	A = [None] * n

	sumLeft = [total // k] * k
	
	result = (total % k) == 0 and subsetSum(S, n - 1, sumLeft, A, k)

	if not result:
		print("k-Partition of set S is not Possible")
		return

	for i in range(k):
		print([S[j] for j in range(n) if A[j] == i + 1])

n = int(input())
li = []
S = []
k = n
for i in range(n):
    n2 = int(input())
    li.append(list(map(int,input().split())))

for i in range(n):
    for j in range(len(li[i])):
                S.append(li[i][j])


    partition(S, k)
