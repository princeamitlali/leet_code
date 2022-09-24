# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def tree_traversal(root, curr_sum, curr_path):
            curr_sum += root.val
            curr_path.append(root.val)
            if root.left == None  and root.right == None:
                if curr_sum == targetSum:
                    ans.append(curr_path)
                return
            
            if root.left:
                tree_traversal(root.left, curr_sum, list(curr_path))
            
            if root.right:
                tree_traversal(root.right, curr_sum, list(curr_path))
        if root:
            tree_traversal(root, 0, [])
        return ans
        