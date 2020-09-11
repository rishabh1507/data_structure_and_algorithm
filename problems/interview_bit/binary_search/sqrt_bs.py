import math
def sqrt1(num):
    low = 0
    high = num

    while(low<high):
        mid = low + (high - low)/2

        if(mid*mid == num):
            return mid
        elif(mid*mid>num):
            high = mid
        else:
            low = mid +1
    
    print(math.floor(mid))
    pass

num = 11
sqrt1(num)


class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        import math
        low = 1
        high = A//2
        result = 0
        if(A < 2):
            return A

        while(low <= high):
            mid = low + (high - low)//2

            if(mid*mid == A):
                return math.floor(mid)
            elif(mid*mid > A):
                high = mid - 1
            else:
                low = mid + 1
                result = mid

        return math.floor(result)
