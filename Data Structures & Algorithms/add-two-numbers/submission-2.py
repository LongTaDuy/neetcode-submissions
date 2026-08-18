# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        cur = dummy
        while l1 and l2:
            number = l1.val + l2.val + carry
            carry = number // 10
            number = number % 10
            cur.next = ListNode(number)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            number = l1.val + carry
            carry = number // 10
            number = number % 10
            cur.next = ListNode(number)
            cur = cur.next
            l1 = l1.next
        while l2:
            number = l2.val + carry
            carry = number // 10
            number = number % 10
            cur.next = ListNode(number)
            cur = cur.next
            l2 = l2.next
        if carry:
            cur.next = ListNode(carry)
        return dummy.next




            
            