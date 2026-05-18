# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preorder(node):
            if not node:
                return
            res.append(node.val)
            preorder(node.right)
            preorder(node.left)
        preorder(root)
        res.reverse()
        return res
