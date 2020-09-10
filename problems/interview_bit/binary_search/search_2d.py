class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def searchRange(self, A, B):
        def left(A,B):
            start = 0 
            end = len(A)-1
            res = -1
            
            while(start<=end):
                mid = start + (end -start)//2
                if(A[mid]==B):
                    res = mid
                    end = mid - 1
                elif(A[mid]>B):
                    end = mid -1
                else:
                    start = mid + 1
            
            return res
            
        def right(A,B):
            start = 0 
            end = len(A)-1
            res = -1
            
            while(start<=end):
                mid = start + (end -start)//2
                if(A[mid]==B):
                    res = mid
                    start = mid + 1
                elif(A[mid]>B):
                    end = mid -1
                else:
                    start = mid + 1
            
            return res
            
        res1 = left(A,B)
        res2 = right(A,B)
                    
            
        
        if(res1 ==-1 and res2 !=-1):
            return [res2,res2]
        elif(res1 !=-1 and res2 ==-1):
            return [res1,res1]
        elif(res1 ==-1 and res2 ==-1):
            return [res1,res1]
        else:
            return [res1,res2]
            
        
            
                
