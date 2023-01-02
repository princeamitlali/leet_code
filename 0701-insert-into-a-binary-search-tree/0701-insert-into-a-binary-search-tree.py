# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        def insert(root,val):
            if root is None:
                return TreeNode(val)
            elif root.val <val:
                root.right = insert(root.right,val)
            elif root.val > val:
                root.left = insert(root.left,val)
            return root
        insert(root,val)
        return root
        