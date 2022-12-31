"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    res = []
    def preorder(self, root: 'Node') -> List[int]:
        if root is None:
            return None 
        self.res = []
        def traverse(root):
            if root is None:
                return None 
            # print(len(root.children))
            self.res.append(root.val)
            if len(root.children) > 0:
                for  i in root.children:
                    if i is not None:
                        # print(i)
                        traverse (i)
                      
            
            # print(self.res)
                
        traverse (root)
        return self.res
        