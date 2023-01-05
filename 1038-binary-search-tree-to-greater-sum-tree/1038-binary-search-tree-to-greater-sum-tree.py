# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        r = root
        self.res = []
        def traverse(root,typ="get"):
            if root is None:
                return None
            if typ == "get":
                self.res.append(root.val)
            else:
                v = sum(self.res[self.res.index(root.val)+1 :])
                # print(v)
                root.val += v
            traverse(root.left,typ)
            traverse(root.right,typ)
        traverse(root)
        self.res.sort()
        root = r
        traverse(root,"put")
        return r
        