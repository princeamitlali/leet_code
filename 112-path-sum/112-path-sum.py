# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        res = False
        def traverse(root,path):
            path.append(root.val)
            if root.left is None and root.right is None:
                print(path)
                if sum(path) == targetSum:
                    return True
                else:
                    return False
            
            if root.left and root.right:
                return traverse(root.left,list(path)) or traverse(root.right,list(path))
            elif root.left:
                return traverse(root.left,list(path))
            elif root.right:
                return traverse(root.right,list(path))
        return 0 if not root else traverse(root,[])