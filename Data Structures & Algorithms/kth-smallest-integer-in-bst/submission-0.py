# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        queue = deque([root])
        lst = []
        while queue:
            node = queue.popleft()
            if node:
                lst.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        lst.sort()
        if k <= len(lst):
            return lst[k - 1]
        return 0