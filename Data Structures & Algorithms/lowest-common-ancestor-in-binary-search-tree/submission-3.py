# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        q1 = deque([root])
        while q1:
            node = q1.popleft()
            if node.left and node.val > p.val and node.val > q.val:
                q1.append(node.left)
            elif node.right and node.val < p.val and node.val < q.val:
                q1.append(node.right)
            else:
                return node
        