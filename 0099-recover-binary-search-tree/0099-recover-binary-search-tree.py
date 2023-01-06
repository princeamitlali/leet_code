# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.prev=self.first=self.sec = None
        def traverse(root):
            if root is None :
                return None
            traverse(root.left)
            if self.prev:
                if self.prev.val > root.val :
                    if self.first is None:
                        self.first = self.prev
                    self.sec = root
            self.prev = root
            traverse(root.right)
        traverse(root)
        self.first.val,self.sec.val = self.sec.val,self.first.val
        print(self.first.val,self.sec.val)

        