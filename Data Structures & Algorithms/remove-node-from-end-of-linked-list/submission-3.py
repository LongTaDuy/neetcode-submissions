# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        cur = head
        while cur:
            cur = cur.next
            N += 1
        RemoveNode = N - n
        cur = head
        if RemoveNode == 0:
            return head.next
        for i in range(RemoveNode - 1):
            cur = cur.next
        cur.next = cur.next.next
        return head

