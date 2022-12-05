# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        double_head = head
        while double_head.next:
            if double_head.next.next:
                double_head = double_head.next.next
                head = head.next
            else:
                double_head = double_head.next
                head = head.next
        return head
        