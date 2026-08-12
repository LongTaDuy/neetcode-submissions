class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1
class LinkedList:
    def __init__(self):
        self.left = ListNode(0, 0)
        self.right = ListNode(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        self.size = 0

    def length(self):
        return self.size
    
    def pushright(self, node):
        nxt, prv = self.right, self.right.prev
        node.next, node.prev = nxt, prv
        nxt.prev, prv.next = node, node
        self.size += 1
    
    def pop(self, node):
        nxt, prv = node.next, node.prev
        nxt.prev, prv.next = prv, nxt
        self.size -= 1
    
    def popleft(self):
        if self.length() == 0:
            return
        node = self.left.next
        self.pop(node)
        return node

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.nodemap = {}
        self.listmap = defaultdict(LinkedList)
        self.lfucnt = 0
        
    def counter(self, node):
        cnt = node.freq
        self.listmap[cnt].pop(node)
        if cnt == self.lfucnt and self.listmap[cnt].length() == 0:
            self.lfucnt += 1
        node.freq += 1
        self.listmap[node.freq].pushright(node)

    def get(self, key: int) -> int:
        if key not in self.nodemap:
            return -1
        node = self.nodemap[key]
        self.counter(node)
        return node.val

        

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return
        if key in self.nodemap:
            node = self.nodemap[key]
            node.val = value
            self.counter(node)
            return
        if len(self.nodemap) == self.cap:
            node = self.listmap[self.lfucnt].popleft()
            self.nodemap.pop(node.key)
        node = ListNode(key, value)
        self.nodemap[key] = node
        self.listmap[1].pushright(node)
        self.lfucnt = 1




# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)