# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = k
        self.val = 0
        def traverse(root):
            if root is None:
                return None
            traverse(root.left)
            # if root.left is None and root.right is None:
            self.count -= 1
            if self.count == 0:
                self.val = root.val
            traverse(root.right)
        traverse(root)
        return self.val
        