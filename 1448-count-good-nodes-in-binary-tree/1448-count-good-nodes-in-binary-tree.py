# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode,curMax = -10000000) -> int:
        return self.goodNodes(root.left,max(root.val,curMax)) + self.goodNodes(root.right , max(root.val,curMax)) + (root.val >= curMax) if root else 0        