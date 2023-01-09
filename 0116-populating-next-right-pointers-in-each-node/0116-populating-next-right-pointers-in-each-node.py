"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root is None:
            return None
        r = root
        arr = [root]
        # res = []
        if root is None:
            return []
        while len(arr) > 0:
            temp = []
            level = []
            while len(arr) > 0:
                node = arr.pop(0)
                # level.append(node.val)
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            # res.append(level)
            # print(temp)
            for i in range(len(temp)-1):
                temp[i].next = temp[i+1]
            # temp[-1].next = None
            arr = temp
        return r

        