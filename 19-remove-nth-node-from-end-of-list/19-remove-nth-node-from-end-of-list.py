# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        root = head
        while n > 0 and temp:
            temp = temp.next
            n -= 1
        pre = None
        print(temp)
        if temp is None:
            root = root.next
            return root
        while temp:
            pre = head
            temp = temp.next
            head = head.next
        if pre is not None:    
            pre.next = head.next
        return root
        