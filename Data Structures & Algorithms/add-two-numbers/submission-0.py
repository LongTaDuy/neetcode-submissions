# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nums1 = 0
        nums2 = 0
        sums = 0
        cur1 = l1
        cur2 = l2
        tmp1 = 1
        tmp2 = 1
        while cur1:
            nums1 = tmp1 * cur1.val + nums1
            tmp1 = tmp1 * 10
            cur1 = cur1.next
        while cur2:
            nums2 = tmp2 * cur2.val + nums2
            tmp2 = tmp2 * 10
            cur2 = cur2.next
        sums = nums1 + nums2
        cur = ListNode(sums % 10)
        sums = sums // 10
        head = cur
        while sums:
            cur.next = ListNode(sums % 10)
            cur = cur.next
            sums = sums // 10

        return head




            
            