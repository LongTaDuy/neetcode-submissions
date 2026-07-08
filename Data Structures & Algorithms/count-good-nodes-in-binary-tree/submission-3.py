# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, max_val):
            if not node:
                return None
            if node.val >= max_val:
                self.res += 1
            dfs(node.left, max(node.val, max_val))
            dfs(node.right, max(node.val, max_val))
        dfs(root, float("-inf"))
        return self.res