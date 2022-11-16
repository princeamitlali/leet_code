# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack = []
        arr=[]
        if root.left:
            stack.append(root.left)
        if root.right:
            stack.append(root.right)
        
        while len(stack):
            temp = []
            arr = []
            while len(stack):
                n = stack.pop()
                if n == None:
                    arr.append(None)
                else:  
                    arr.append(n.val)
                    if n.left:
                        temp.append(n.left)
                    else:
                        temp.append(None)
                    if n.right:
                        temp.append(n.right)
                    else:
                        temp.append(None)
            print(arr)
            if arr != arr[::-1] or len(arr)%2 == 1:
                return False
            stack = temp
        return True
        