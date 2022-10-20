# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        temp = head
        pre = temp
        while temp:
            count += 1
            pre = temp
            temp = temp.next
        l = count
        if l == 0:
            return 
        if l == 1:
            return head
        k = k % l
        pre.next = head
        
        
        temp = head
        for _ in range( l - k - 1 ):
            print(temp.val)
            temp = temp.next
        answer = temp.next
        temp.next = None
        
        return answer
        