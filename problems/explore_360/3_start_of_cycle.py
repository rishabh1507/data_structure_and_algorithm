# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = ListNode(0)
        slow = head
        
        fast = ListNode(0)
        fast = head
        
        
        isBool = False

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if(slow==fast):
                isBool=True
                break
            
        if(isBool):
            slow=head
            while(slow!=fast):
                slow = slow.next
                fast = fast.next
                
            return slow
        return None