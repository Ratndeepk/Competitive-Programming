"""
Given a Binary Tree of size N , where each node can have positive or negative values. Convert this to a tree where each node contains the sum of the left and right sub trees of the original tree. The values of leaf nodes are changed to 0.

Example 1:

Input:
             10
          /      \
        -2        6
       /   \     /  \
     8     -4   7    5

Output:
            20
          /    \
        4        12
       /  \     /  \
     0     0   0    0

"""

def toSumTree(root) :
    if root==None:
        return 0
        
    oldval = root.data
    
    root.data = toSumTree(root.left)+toSumTree(root.right)
    
    return root.data+oldval