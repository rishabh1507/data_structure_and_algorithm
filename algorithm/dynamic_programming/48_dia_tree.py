class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def height(node):
    if(node is None):
        return 0
    return 1 + max(height(node.left),height(node.right))

def diameter(node):
    if(node is None):
        return 0
    l = height(node.left)
    r = height(node.right)

    ld = diameter(node.left)
    rd = diameter(node.right)

    return max(l+r+1,max(ld,rd))


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(diameter(root))
