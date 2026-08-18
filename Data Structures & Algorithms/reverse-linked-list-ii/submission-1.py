# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for i in range(left - 1):
            prev = prev.next
        cur = prev.next
        headsub = cur
        presub = None
        for i in range(right - left + 1):
            tmp = cur.next
            cur.next = presub
            presub = cur
            cur = tmp
        prev.next = presub
        headsub.next = cur
        return dummy.next


        

