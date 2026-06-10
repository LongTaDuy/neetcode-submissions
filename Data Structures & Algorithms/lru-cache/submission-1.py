class Node:
    def __init__(self, key: int, val: int):
        self.key, self.val = key, val
        self.next = self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.right, self.left = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left
        
    def remove(self, node):
        pre, nxt = node.prev, node.next
        pre.next = nxt
        nxt.prev = pre

    def insert(self, node):
        pre, nxt = self.right.prev, self.right
        node.next, node.prev = nxt, pre
        pre.next = nxt.prev = node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1   
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if self.cap < len(self.cache):
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        
