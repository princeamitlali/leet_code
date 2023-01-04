# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # count = 0
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.matchCount = 0
        
        self.explore(root)
        
        return self.matchCount
    
    def explore(self, root):
        if root is None:
            return 0, 0
        
        ls, lc = self.explore(root.left)
        rs, rc = self.explore(root.right)
        
        childTotal = ls + rs + root.val
        childCount = lc + rc + 1
        
        if childCount != 0 and root.val == childTotal // childCount:
            self.matchCount += 1
        
        return childTotal, childCount
            
        