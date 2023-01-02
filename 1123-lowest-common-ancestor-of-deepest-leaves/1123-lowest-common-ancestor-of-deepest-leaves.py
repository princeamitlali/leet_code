# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root):
            if not root: return 0,None
            h1, leftLCA=recurse(root.left)
            h2, rightLCA=recurse(root.right)
            
            if h1>h2:
                return h1+1,leftLCA
            if h1<h2:
                return h2+1,rightLCA
            return   h1+1,root
        return recurse(root)[1]

    