# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        # arr = [root,None]
        # # res = []
        # temp = []
        # sol = 0
        # if root is None:
        #     return []
        # while len(arr) > 1:
        #     node = arr.pop(0)
        #     if node is None:
        #         # res.append(temp)
        #         temp = []
        #         arr.append(None)
        #     else:
        #         temp.append(node.val)
        #         sol += node.val
        #         if node.left:
        #             arr.append(node.left)
        #         if node.right:
        #             arr.append(node.right)
        #     sol = sum(temp)
        # # res.append(temp)
        # return sol
        
        curLayer = [root]
        while curLayer:
            lastSum, nextLayer = 0, [] # init sum to zero
            for node in curLayer:
                lastSum += node.val # rolling sum
                if node.left: nextLayer.append(node.left)
                if node.right: nextLayer.append(node.right)
            curLayer = nextLayer
        return lastSum
        