# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        arr =[]
        def trav(x , s):
            nonlocal arr
            if x.left:
                trav(x.left, s + "->" + str(x.val))
            if x.right:
                trav(x.right, s + "->" + str(x.val))
            if not x.left and not x.right: 
                arr.append(s + "->" + str(x.val))

        if root.left:
            trav(root.left, str(root.val))

        if root.right:
            trav(root.right, str(root.val))
        
        if not root.right and not root.left:
            arr.append(str(root.val))

        return arr
