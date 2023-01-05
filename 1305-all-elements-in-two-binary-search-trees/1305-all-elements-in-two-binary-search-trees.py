# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.res = []
        def traverse(root):
            if root is None:
                return None
            self.res.append(root.val)
            traverse(root.right)
            traverse(root.left)
        traverse(root1)
        traverse(root2)
        return sorted(self.res)
        