"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
def insert_in_between(head):
    temp = head
    while temp:
        temp.next = Node(temp.val,temp.next)
        temp = temp.next.next

def connect_random_node(head):
    temp = head
    while temp:
        if temp.random is None:
           temp.next.random = None
        else: 
            temp.next.random = temp.random.next
        temp = temp.next.next

def get_deep_copy(head):
    res = Node(-1)
    temp = head
    sol = res
    while temp:
        res.next = temp.next
        res = res.next
        temp.next = res.next
        temp = temp.next
    return sol.next



class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        insert_in_between(head)
        print
        connect_random_node(head)
        
        return get_deep_copy(head)

        