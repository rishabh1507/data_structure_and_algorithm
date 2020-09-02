class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minelem = -1
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if(len(self.stack)==0):
            self.stack.append(x)
            self.minelem = x
        elif(x>=self.minelem):
            self.stack.append(x)
            
        elif(x<self.minelem):
            self.stack.append(2*x-self.minelem)
            self.minelem = x
    
    def pop(self):
        """
        :rtype: None
        """
        if(len(self.stack)==0):
            return -1
        elif(self.stack[len(self.stack)-1]>=self.minelem):
            self.stack.pop()
        elif(self.stack[len(self.stack)-1]<self.minelem):
            self.minelem = 2*self.minelem-self.stack[len(self.stack)-1]
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if(len(self.stack)==0):
            return -1
        elif(self.stack[len(self.stack)-1]>=self.minelem):
            return self.stack[len(self.stack)-1]
        elif(self.stack[len(self.stack)-1]<self.minelem):
            return self.minelem

    def getMin(self):
        """
        :rtype: int
        """
        if(len(self.stack)==0):
            return -1
        return self.minelem
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()