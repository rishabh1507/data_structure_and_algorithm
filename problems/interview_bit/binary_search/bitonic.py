class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def bs1(self, A, B, start1, end1):
        while(start1 <= end1):
            mid1 = start1 + (end1 - start1)//2
            if(A[mid1] == B):
                return mid1
            elif(A[mid1] > B):
                end1 = mid1 - 1
            else:
                start1 = mid1 + 1
        return -1

    def bs2(self, A, B, start2, end2):
        while(start2 <= end2):
            mid2 = start2 + (end2 - start2)//2
            if(A[mid2] == B):
                return mid2
            elif(A[mid2] > B):
                start2 = mid2 + 1
            else:
                end2 = mid2 - 1
        return -1

    def solve(self, A, B):
        n = len(A)
        start = 0
        end = n - 1
        res = 0

        while(start <= end):
            mid = start + (end - start)//2
            if(mid > 0 and mid < n-1):
                if(A[mid] == B):
                    return mid
                elif(A[mid] > A[mid - 1] and A[mid] > A[mid + 1]):
                    res = mid
                    break
                elif(A[mid-1] > A[mid]):
                    end = mid - 1
                else:
                    start = mid + 1

        result1 = self.bs1(A, B, 0, res-1)
        result2 = self.bs2(A, B, res, n-1)

        if(result1 == -1 and result2 == -1):
            return -1
        elif(result1 == -1 and result2 != -1):
            return result2
        else:
            return result1
