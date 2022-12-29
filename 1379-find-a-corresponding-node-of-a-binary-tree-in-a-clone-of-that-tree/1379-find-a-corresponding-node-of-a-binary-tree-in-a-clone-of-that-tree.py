# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    res = None
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def traverse(original,cloned,target):
            # print(original.val,cloned.val)
            if original is None:
                return None
            if original == target:
                self.res = cloned
            traverse(original.right,cloned.right,target)
            traverse(original.left,cloned.left,target)
        traverse(original,cloned,target)
        return self.res
        