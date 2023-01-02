# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = 0
        root = head
        pre = None
        while root.next:
            print(root.val)
            pre = root
            if root.next.val ==0:
                s = 0
                # pre = root
                root = root.next
                
            else:
                root.val += root.next.val
                root.next = root.next.next
        pre.next = None
        return head
        