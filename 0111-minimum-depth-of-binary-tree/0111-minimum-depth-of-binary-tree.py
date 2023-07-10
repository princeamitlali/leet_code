# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 100000000000
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # res =   1000000000
        if root is None:
            return 0
        def traverse(root,count = 0):
            if root and root.left is None and root.right is None:
                self.res = min(self.res,count+1)
            if root.left:
                traverse(root.left,count+1)
            if root.right:
                traverse(root.right,count+1)
        traverse(root)
        return self.res 
        