# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res = []
        def traverse(root):
            if root is None:
                return 
            res.append(root.val)
            if root.left:
                traverse(root.left)
            if root.right:
                traverse(root.right)
        traverse(root)
        # print(res)
        return len(set(res)) == 1
            
        