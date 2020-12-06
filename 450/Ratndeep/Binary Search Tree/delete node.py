
# Helper function to find minimum value node in subtree rooted at curr
def minimumKey(curr):
 
    while curr.left:
        curr = curr.left
 
    return curr
 
 
 
# Function to delete node from a BST
def deleteNode(root, key):
 
    # pointer to store parent node of current node
    parent = None
 
    # start with root node
    curr = root
 
    # search key in BST and set its parent pointer
    while curr and curr.data != key:
 
        # update parent node as current node
        parent = curr
 
        # if given key is less than the current node, go to left subtree
        # else go to right subtree
        if key < curr.data:
            curr = curr.left
        else:
            curr = curr.right
 
    # return if key is found not in the tree
    if curr is None:
        return root
 
    # Case 1: node to be deleted has no children i.e. it is a leaf node
    if curr.left is None and curr.right is None:
 
        # if node to be deleted is not a root node, then set its
        # parent left/right child to None
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
 
        # if tree has only root node, delete it and set root to None
        else:
            root = None
 
    # Case 2: node to be deleted has two children
    elif curr.left and curr.right:
 
        # find its in-order successor node
        successor = minimumKey(curr.right)
 
        # store successor value
        val = successor.data
 
        # recursively delete the successor. Note that the successor
        # will have at-most one child (right child)
        deleteNode(root, successor.data)
 
        # Copy the value of successor to current node
        curr.data = val
 
    # Case 3: node to be deleted has only one child
    else:
 
        # find child node
        if curr.left:
            child = curr.left
        else:
            child = curr.right
 
        # if node to be deleted is not a root node, then set its parent
        # to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
 
        # if node to be deleted is root node, then set the root to child
        else:
            root = child
 
    return root