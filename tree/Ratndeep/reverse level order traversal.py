def reverseLevelOrder(root):
    # code here
    stack=[]
    queue=[root]
    while queue!=[]:
        stack.insert(0,queue[0].data)
        cur_root=queue.pop(0)
        if cur_root.right:
            queue.append(cur_root.right)
        if cur_root.left:
            queue.append(cur_root.left)
    return stack
