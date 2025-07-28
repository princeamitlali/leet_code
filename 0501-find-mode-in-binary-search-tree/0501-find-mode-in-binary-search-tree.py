# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        nodes_list = [root]
        dic = {}
        while len(nodes_list) > 0:
            node = nodes_list.pop(0)
            val = node.val
            dic[val] = dic.get(val,0) + 1
            if node.left:
                nodes_list.append(node.left)
            if node.right:
                nodes_list.append(node.right)
        max_val = max(dic.values())
        ans = []
        for key,val in dic.items():
            if val == max_val:
                ans.append(key)
        return ans
        