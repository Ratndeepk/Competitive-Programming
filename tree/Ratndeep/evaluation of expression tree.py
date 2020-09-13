
def evalExpressionTree(root):
    if root==None:
        return 0
    if root.left==None and root.right==None:
        return int(root.data)
    a = evalExpressionTree(root.left)
    b = evalExpressionTree(root.right)
    if root.data=="+":
        return a+b
    elif root.data=="-":
        return a-b
    elif root.data=="*":
        return a*b
    elif root.data=="/":
        return int(a/b)
