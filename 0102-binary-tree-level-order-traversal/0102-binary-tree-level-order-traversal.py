# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        # arr = [root,None]
        # res = []
        # temp = []
        # if root is None:
        #     return []
        # while len(arr) > 1:
        #     node = arr.pop(0)
        #     if node is None:
        #         res.append(temp)
        #         temp = []
        #         arr.append(None)
        #     else:
        #         temp.append(node.val)
        #         if node.left:
        #             arr.append(node.left)
        #         if node.right:
        #             arr.append(node.right)
        # res.append(temp)
        # return res
        res = []
        arr = [root]
        while len(arr) > 0:
            r = []
            next_arr = []
            for i in arr:
                r.append(i.val)
                if i.left:
                    next_arr.append(i.left)
                if i.right:
                    next_arr.append(i.right)
            arr = next_arr
            res.append(r)
        return res
            

        