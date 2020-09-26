# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = ListNode()
        slow = head
        fast = ListNode()
        fast = head
        isBool = False
        
        
        
        while(slow and fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            if(slow==fast):
                isBool = True
                break
                
            
        
        return isBool
            