"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # tao hashmap of copy node
        oldtonew = {None : None}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldtonew[cur] = copy
            cur = cur.next

        # link new copy
        cur = head
        while cur:
            copy = oldtonew[cur]
            copy.next = oldtonew[cur.next]
            copy.random = oldtonew[cur.random]
            cur = cur.next
        return oldtonew[head]

            