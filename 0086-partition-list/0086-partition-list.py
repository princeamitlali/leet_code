# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head is None:
            return head
            
        res = [[],[]]
        while head:
            v = head.val
            if v < x:
                res[0].append(v)
            else:
                res[1].append(v)
            head = head.next
        for i in res[1]:
            res[0].append(i)
        head = ListNode(res[0][0])
        root = head
        for i in res[0][1:]:
            h = ListNode(i)
            root.next = h
            root = h
        return head
        
            
        