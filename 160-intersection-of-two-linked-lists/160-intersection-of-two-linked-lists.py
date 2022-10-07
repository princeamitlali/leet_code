# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1,ptr2 = headA,headB
        if ptr1 == ptr2:
            return ptr1
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
            if ptr1 == ptr2:
                return ptr1
            if ptr1 == None:
                ptr1 = headB
            if ptr2 == None:
                ptr2 = headA
        return ptr1
        # l1=[]
        # while headA:
        #     l1.append(headA)
        #     headA = headA.next
        # while headB:
        #     if headB in l1:
        #         return headB
        #     headB = headB.next
        # return None
        
                
        