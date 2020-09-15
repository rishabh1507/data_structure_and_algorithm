def height(root):
    if(root == None):
        return 0
    lh = height(root.left)
    rh = height(root.right)

    return 1+max(lh, rh)
