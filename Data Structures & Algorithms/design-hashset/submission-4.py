class ListNode:
    def __init__(self, key: int):
        self.val = key
        self.next = None
class MyHashSet:

    def __init__(self):
        self.set = [ListNode(0) for i in range(10000)]

    def add(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.val == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
        
    def remove(self, key: int) -> None:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.val == key:
                tmp = cur.next.next
                cur.next = tmp
                return
            cur = cur.next
                
    def contains(self, key: int) -> bool:
        cur = self.set[key % len(self.set)]
        while cur.next:
            if cur.next.val == key:
                return True
            cur = cur.next        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)