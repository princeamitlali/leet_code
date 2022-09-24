# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def traverse(root,path):
            if not root:
                return
            path.append(root.val)
            if root.left is None and root.right is None:
                if sum(path) == targetSum:
                    ans.append(path)
            
            if root.left:
                traverse(root.left,list(path))
                
            if root.right:    
                traverse(root.right,list(path))
        if root:        
            traverse(root,[])
        return ans
        