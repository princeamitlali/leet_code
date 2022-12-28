# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,root):
        if root is not None:
            self.traverse(root.left)
            self.elements.append(root.val)
            self.traverse(root.right) 
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.elements = []
        
        self.traverse(root)
        root = TreeNode(self.elements[0])
        r = root
        for i in self.elements[1:]:
            root.right = TreeNode(i)
            root = root.right
            
        return r
        