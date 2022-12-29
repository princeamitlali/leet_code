# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    s = 0
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # s = 0
        def traverse(root,side):
            if root is None:
                return None
            if root.left is None and root.right is None:
                if side == "l":
                    self.s += root.val
            traverse(root.right,"r")
            traverse(root.left,"l")
        traverse(root,"c")
        return self.s
        