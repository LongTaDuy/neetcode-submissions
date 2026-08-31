# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return [0, 0]
            leftRoot = dfs(root.left)
            rightRoot = dfs(root.right)
            withRoot = leftRoot[1] + rightRoot[1] + root.val
            withoutRoot = max(leftRoot) + max(rightRoot)
            return [withRoot, withoutRoot]
        return max(dfs(root))