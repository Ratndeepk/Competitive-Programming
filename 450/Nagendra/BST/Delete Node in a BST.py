#link https://leetcode.com/problems/delete-node-in-a-bst/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        temp = root
        f = 0
        prev = temp
        while temp:
            if temp.val == key:
                f = 1
                break
            prev = temp
            if temp.val > key:
                temp = temp.left
            else:
                temp = temp.right
        if f == 1:

            if root.left == None and root.right == None:
                return None
            elif temp.left == None and temp.right == None:
                if prev.left == temp:
                    prev.left = None
                else:
                    prev.right = None
            elif temp.left == None or temp.right == None:

                if root.val == key:
                    if root.left == None:
                        root = root.right
                    else:
                        root = root.left
                elif prev.left == temp:
                    if temp.left == None:
                        prev.left = temp.right
                    else:
                        prev.left = temp.left
                else:
                    if temp.left == None:
                        prev.right = temp.right
                    else:
                        prev.right = temp.left
            else:
                temp1 = temp
                temp = temp.right
                while temp.left:
                    temp1 = temp
                    temp = temp.left
                if temp1.left == temp:
                    temp1.left = temp.right
                else:
                    temp1.right = temp.right

                if root.val == key:
                    temp.left = prev.left
                    temp.right = prev.right
                    root = temp

                elif prev.left and prev.left.val == key:
                    temp.left = prev.left.left
                    temp.right = prev.left.right
                    prev.left = temp
                else:
                    temp.left = prev.right.left
                    temp.right = prev.right.right
                    prev.right = temp

        return root
