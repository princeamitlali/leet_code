# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        root = head
        while head:
            if head.next:
                temp = head.val
                head.val = head.next.val
                head.next.val = temp
                head = head.next
            head = head.next
        return root
            