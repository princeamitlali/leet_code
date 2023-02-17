# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.res =[]
        def traverse(root):
            if root is None:
                return None 
            self.res.append(root.val)
            traverse(root.right)
            traverse(root.left)
        traverse(root)
        r = 99999999999
        self.res.sort()
        print(self.res)
        for i in range(len(self.res)-1):
            r = min(r, abs(self.res[i+1] - self.res[i]))
        return r
        