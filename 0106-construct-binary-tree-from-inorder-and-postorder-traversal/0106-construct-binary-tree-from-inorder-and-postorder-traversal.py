# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    postIndex = 0
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        i_start,i_end = 0,len(postorder)-1
        self.postIndex = i_end
        def construct(inorder,postorder,i_start,i_end):
            if i_start > i_end:
                return None
            if self.postIndex<0:
                return None
            root = TreeNode(postorder[self.postIndex])
            self.postIndex -= 1
            if i_start == i_end:
                return root
            inIndex = inorder.index(root.val)
            root.right = construct(inorder,postorder,inIndex + 1, i_end)
            root.left = construct(inorder,postorder,i_start,inIndex - 1)
            
            return root
            
        return construct(inorder,postorder,i_start,i_end)