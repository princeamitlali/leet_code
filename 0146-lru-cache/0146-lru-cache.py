class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node("head", 0)
        self.tail = Node("tail", 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert_top(self, new_node):
        left = self.head
        right = self.head.next
        left.next = new_node
        right.prev = new_node
        new_node.next = right
        new_node.prev = left

    def remove_last(self):
        left = self.tail
        right = left.prev
        if right == self.head:
            return

        last = right
        right = right.prev
        right.next = left
        left.prev = right
        key, val = last.key, last.val
        return key, val

    def move_to_start(self, node):
        left = node.prev
        right = node.next
        if left == self.head:
            return
        left.next = right
        right.prev = left

        left2, right2 = self.head, self.head.next
        left2.next = node
        right2.prev = node
        node.next = right2
        node.prev = left2


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict()
        self.capacity = capacity
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.linked_list.move_to_start(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.linked_list.move_to_start(node)
        else:
            if len(self.cache) == self.capacity:
                lk, lv = self.linked_list.remove_last()
                del self.cache[lk]
            node = Node(key, value)
            self.cache[key] = node
            self.linked_list.insert_top(node)