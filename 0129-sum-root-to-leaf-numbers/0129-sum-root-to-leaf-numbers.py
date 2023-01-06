# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans =[]
        def traverse(root,res=""):
            if root is None:
              
                return None
            res += str(root.val)
            if root.left is None and root.right is None:
                
                self.ans.append(int(res))
                res = res[:-1]
                return
            traverse(root.left,res)
            traverse(root.right,res)
            res = res[:-1]
   
        traverse(root)

        return sum(self.ans)
                