# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
       
        def traverse(nums):
            if len(nums) == 0:
                return None
            
            m = max(nums)
            idx = nums.index(m)
            root = TreeNode(m)
            root.right = traverse(nums[idx+1:])
            root.left = traverse(nums[:idx])
            return root
        return traverse(nums)
        