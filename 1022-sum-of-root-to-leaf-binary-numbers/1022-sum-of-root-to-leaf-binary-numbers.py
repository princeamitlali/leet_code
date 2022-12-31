# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    res = 0
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def traverse(root,li):
            if root is None:
                return None
            if root.left is None and root.right is None:
                li = li+str(root.val)
                self.res += int(li,2)
                return None
            # li.append(root.val)
            traverse(root.right,li+str(root.val))
            traverse(root.left,li+str(root.val))
        traverse(root,"")
        return self.res
            
        