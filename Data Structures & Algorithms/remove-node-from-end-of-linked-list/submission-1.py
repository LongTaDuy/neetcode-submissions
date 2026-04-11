# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1
        tempt = head
        if n == 1 and length == 1:
            return None
        
        for _ in range(length - n - 1):
            tempt = tempt.next

        if length == n:
            head = head.next
        if tempt.next and tempt.next.next:
            tmp = tempt.next.next
            tempt.next = tmp
        else:
            tempt.next = None
        return head