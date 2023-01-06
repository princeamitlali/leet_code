# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        res = []
        arr = [root]
        flag = False
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
            if flag:
                r = r[::-1]
            flag = not flag
            res.append(r)
        print(res)
        return res
        