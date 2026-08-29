# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = deque([(root, float('-inf'))])
        res = 0
        while q:
            for _ in range(len(q)):
                node, cur_max = q.popleft()
                if node.val >= cur_max:
                    res += 1
                if node.left:
                    q.append((node.left, max(cur_max, node.val)))
                if node.right:
                    q.append((node.right, max(cur_max, node.val)))
        return res

            
            
                