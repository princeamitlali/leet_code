# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = []  
        res = []
        queue.append(root)
        
        while(queue):   
            queue_len = len(queue)  
            tmp = 0
            for i in range(queue_len):   
                node = queue.pop(0)
                tmp += node.val
                if node.left:   
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp/queue_len)    
        
        return res