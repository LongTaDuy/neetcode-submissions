# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        cur = head
        leftpre = dummy
        for _ in range(left - 1):
            leftpre = cur
            cur = cur.next
        prev = None
        for _ in range(right - left + 1):
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        leftpre.next.next = cur
        leftpre.next = prev
        return dummy.next
