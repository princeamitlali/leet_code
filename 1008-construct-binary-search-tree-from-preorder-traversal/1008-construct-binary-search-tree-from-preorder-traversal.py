# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def traverse(preorder,inorder):
            if len(inorder) == 0:
                return None
            if len(preorder) == 0:
                return None
            v = preorder.pop()
            idx = inorder.index(v)
            root = TreeNode(v)
            root.left = traverse(preorder,inorder[:idx])
            root.right = traverse(preorder,inorder[idx+1:])
            return root
        return traverse(preorder[::-1],sorted(preorder))
        