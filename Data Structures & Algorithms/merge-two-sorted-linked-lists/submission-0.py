# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        curr1 = list1
        curr2 = list2
        curr = None
        if curr1.val < curr2.val:
            head = curr1
            curr = curr1
            curr1 = curr1.next
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next

                else:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next
        else:
            curr = curr2
            head = curr2
            curr2 = curr2.next
            while curr1 and curr2:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next

        if curr1 != None:
            curr.next = curr1
        if curr2 != None:
            curr.next = curr2
        return head
        