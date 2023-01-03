"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        res = 0
        arr = [root]
        while len(arr) > 0:
            r = []
            next_arr = []
            for i in arr:
                # r.append(i.val)
                if i is not None:
                    for j in i.children:
                        next_arr.append(j)
            arr = next_arr
            res += 1
        return res
        