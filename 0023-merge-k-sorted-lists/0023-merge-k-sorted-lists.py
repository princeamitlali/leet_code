# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            temp = ListNode(-1)
            prev = temp
            while l1 and l2:
                if l1.val <= l2.val:
                    prev.next = l1
                    l1 = l1.next
                else:
                    prev.next = l2
                    l2 = l2.next
                prev = prev.next
            prev.next = l1 if l1 else l2
            return temp.next
            
        if len(lists) == 0:
            return None
        res = ListNode(None)
        for i in lists:
            res.next = mergeTwoLists(res.next,i)
        return res.next