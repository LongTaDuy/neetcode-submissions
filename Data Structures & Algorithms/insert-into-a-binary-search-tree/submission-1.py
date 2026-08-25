# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur = root
        par = None
        while cur:
            if val > cur.val:
                par = cur
                cur = cur.right
            else:
                par = cur
                cur = cur.left
        if par.val > val:
            par.left = TreeNode(val)
        if par.val < val:
            par.right = TreeNode(val)
        return root
    