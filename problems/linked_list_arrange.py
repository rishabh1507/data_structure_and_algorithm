class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

def push(head , data):
    newNode = Node(data)
    newNode.next = head
    return newNode

def construct(keys):
    dummy = Node()
    tail = dummy

    for key in keys:
        tail.next = push(tail.next,key)
        tail = tail.next

    return dummy.next

def reverse(head):
    prev = None
    curr = head

    while(curr):
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    return head

def printList(head):
    ptr = head
    while(ptr!=None):
        print(ptr.data)
        ptr=ptr.next
    print('Done')


def getCount(head):
    temp = head 
    count = 0  
    while (temp):
        count += 1
        temp = temp.next
    return count

def printList2(head1,head2):
    ptr1 = head1
    ptr2 = head2
    count1 = 0
    count2 = 2
    print(count2)

    while(2):
        print(ptr1.data)
        # print(ptr2.data)
        ptr1 = ptr1.next
        # ptr2 = ptr2.next
    print("Done")



keys = [1,2,3,4]
ll = construct(keys)
l2 = reverse(ll)
printList(l2)
printList2(ll,l2)
