"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return []
        
        queue = deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                queue += node.children
            yield level
        # stack= []
        # li = []
        # stack.append(root)
        # temp = []
        # while len(stack) > 0:
        #     curr = stack.pop()
        #     if curr is not None:
        #         if curr == "change":
        #             print()
        #             if len(temp) > 0:
        #                 li.append(temp)
        #             temp = []
        #         else:
        #             temp.append(curr.val)
        #             stack.insert(0,"change")
        #             for i in curr.children:
        #                 stack.insert(0,i)
        # return li
                
