# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergetwolist(self, l1, l2):
        if not l2:
            return l1
        if not l1:
            return l2
        head = None
        if l1.val < l2.val:
            head = ListNode(l1.val)
            l1 = l1.next
        else:
            head = ListNode(l2.val)
            l2 = l2.next
        curr = head
        while l1 and l2:
            if l1.val > l2.val:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
            else:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
        if not l1:
            curr.next = l2
        if not l2:
            curr.next = l1
        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            merge_list = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None
                merge_list.append(self.mergetwolist(l1, l2))
            lists = merge_list
        return lists[0]