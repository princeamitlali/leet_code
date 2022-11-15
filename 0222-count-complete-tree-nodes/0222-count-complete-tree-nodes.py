# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
c = 0
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        global c
        c = 0
        if not root:
            return 0
        def traverse(n):
            global c
            c = c + 1
            if n.left:
                traverse(n.left)
            if n.right:
                traverse(n.right)
        traverse(root)
        return c
            
        