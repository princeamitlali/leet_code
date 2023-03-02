# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        grand_parent = -1
        Solution.res = 0
        def traverse(root,grand_parent):
            if root.left is None and root.right is None:
                return
            if grand_parent % 2 == 0:
                if root.left:
                    Solution.res += root.left.val
                  
                if root.right :
                    Solution.res += root.right.val
                   
            if root.left:
                traverse(root.left,root.val)
            if root.right :
                traverse(root.right,root.val)
        traverse(root,grand_parent)
        return Solution.res
        
                
            
        