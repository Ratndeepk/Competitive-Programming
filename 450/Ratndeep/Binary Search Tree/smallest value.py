def minValue(root):
    ##Your code here
    if root is None:
        return -1
    temp=root
    while temp.left!=None:
        temp=temp.left
    return temp.data