# import sys

# def solve(arr,t,i,j):
#     if(i>=j):
#         t[i][j]=0
#         return 0
    
#     if(t[i][j] != -1):
#         return t[i][j]

#     min1 = 100000000000000000

#     for k in range(i,j):
#         temp_ans = solve(arr,t,i,k) + solve(arr,t,k+1,j) + arr[i-1]*arr[k]*arr[j]
        
#         if(temp_ans<min1):
#             min1 = temp_ans
        
    
    
#     t[i][j]=min1

#     return t[i][j] 
    
# arr = list(map(int,input().split()))
# n = len(arr)
# global t
# t = [[-1 for x in range(n+1)] for x in range(n+1)]

# result = solve(arr,t,1,n-1)
# print(result)

# def mcm(arr,i,j,t):

#     if(j<=i+1):
#         return 0
    
#     min = float('inf')

#     if (t[i][j] == 0):

#         for k in range(i+1,j):
#             cost = mcm(arr,i,k,t)
#             cost += mcm(arr,k,j,t)
#             cost += arr[i]*arr[k]*arr[j]
#             print(cost)

#             if(cost<min):
#                 min = cost

#         t[i][j] = min
#     return t[i][j]



# arr = list(map(int,input().split()))
# n = len(arr)
# t = [[0 for i in range(n)] for j in range(n)]

# result = mcm(arr,0,n-1,t)
# print(result)


# Function to find the most efficient way to multiply
# given sequence of matrices
def MatrixChainMultiplication(dims, i, j, T):

	# base case: one matrix
	if j <= i + 1:
		return 0

	# stores minimum number of scalar multiplications (i.e., cost)
	# needed to compute the matrix M[i+1]...M[j] = M[i..j]
	min = float('inf')

	# if sub-problem is seen for the first time, solve it and
	# store its result in a lookup table
	if T[i][j] == 0:

		# take the minimum over each possible position at which the
		# sequence of matrices can be split

		"""
			(M[i+1]) x (M[i+2]..................M[j])
			(M[i+1]M[i+2]) x (M[i+3.............M[j])
			...
			...
			(M[i+1]M[i+2]............M[j-1]) x (M[j])
		"""

		for k in range(i + 1, j):

			# recur for M[i+1]..M[k] to get an i x k matrix
			cost = MatrixChainMultiplication(dims, i, k, T)

			# recur for M[k+1]..M[j] to get a k x j matrix
			cost += MatrixChainMultiplication(dims, k, j, T)

			# cost to multiply two (i x k) and (k x j) matrix
			cost += dims[i] * dims[k] * dims[j]

			if cost < min:
				min = cost

		T[i][j] = min

	# return min cost to multiply M[j+1]..M[j]
	return T[i][j]


if __name__ == '__main__':

	# Matrix M[i] has dimension dims[i-1] x dims[i] for i = 1..n
	# input is 10 x 30 matrix, 30 x 5 matrix, 5 x 60 matrix
	dims = [40, 20, 30, 10, 30]

	# lookup table to store the solution to already computed sub-problems
	T = [[0 for x in range(len(dims))] for y in range(len(dims))]

	print("Minimum cost is", MatrixChainMultiplication(dims, 0, len(dims) - 1, T))
