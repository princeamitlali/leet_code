# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def merge(l1,l2):
    dummy = ListNode(-1)
    temp = dummy

    while l1 is not None and l2 is not None:
        if l1.val < l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next

    if l1 is not None:
        temp.next = l1

    if l2 is not None:
        temp.next = l2

    return dummy.next

def find_mid(head):
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        mid = find_mid(head)

        low = head
        high = mid.next
        mid.next = None

        left = self.sortList(low)
        right = self.sortList(high)

        return merge(left,right)


        