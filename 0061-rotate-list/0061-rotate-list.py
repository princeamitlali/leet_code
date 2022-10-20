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
        
        # Get the next node from the tempNode and then set the tempNode.next as None
        # Example: In 1->2->3->4->5, and k = 2
        #          tempNode = Node(3)
        #          answer = Node(3).next => Node(4)
        #          Node(3).next = None ( cut the linked list from here )
        answer = temp.next
        temp.next = None
        
        return answer
        