from bisect import bisect_right as upper_bound

MAX = 100

# Function to find median in the matrix


def binaryMedian(m, r, d):
    mi = m[0][0]
    mx = 0
    for i in range(r):
        if m[i][0] < mi:
            mi = m[i][0]
        if m[i][d-1] > mx:
            mx = m[i][d-1]

    desired = (r * d + 1) // 2

    while (mi < mx):
        print("----")
        mid = mi + (mx - mi) // 2
        print("mid mi mx",mid,mi,mx)
        print("mid",mid)
        place = [0]

        # Find count of elements smaller than mid
        for i in range(r):
            j = upper_bound(m[i], mid)
            print("ub",j)
            place[0] = place[0] + j
            print("place",place[0])
        if place[0] < desired:
            mi = mid + 1
        else:
            mx = mid
    print ("Median is", mi) 
    return    
      
# Driver code 
r, d = 3, 3
  
m = [ [1, 3, 5], [2, 6, 9], [3, 6, 9]] 
binaryMedian(m, r, d) 


# class Solution:
#     # @param A : list of list of integers
#     # @return an integer
#     def findMedian(self, A):
#         from bisect import bisect_right as upper_bound
#         MAX = 100

#         n = len(A)
#         m = len(A[0])
#         min1 = A[0][0]
#         max1 = 0

#         for i in range(n):
#             if(min1 > A[i][0]):
#                 min1 = A[i][0]
#             elif(max1 < A[i][m-1]):
#                 max1 = A[i][m-1]

#         medi = (n*m+1)//2

#         while(min1 < max1):
#             mid = min1 + (max1-min1)//2

#             place = [0]

#             for i in range(n):
#                 temp = upper_bound(A[i], mid)
#                 place[0] = place[0] + temp
#             if(place[0] < medi):
#                 min1 = mid + 1
#             else:
#                 max1 = mid

#         return min1
