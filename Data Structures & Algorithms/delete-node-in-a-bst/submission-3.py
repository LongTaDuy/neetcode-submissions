# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        parent = None
        cur = root
        while cur and cur.val != key:
            parent = cur
            if key > cur.val:
                cur = cur.right
            else:
                cur = cur.left
        if not cur:
            return root
        
        ## only one child or no child
        if not cur.left or not cur.right:
            child = cur.left if cur.left else cur.right
            if not parent:
                return child
            if parent.left == cur:
                parent.left = child
            else:
                parent.right = child
        else:
            par = None
            deleteNode = cur
            cur = cur.right
            while cur.left:
                par = cur
                cur = cur.left
            if par:
                par.left = cur.right
                cur.right = deleteNode.right
            cur.left = deleteNode.left
            if not parent:
                return cur
            if parent.right == deleteNode:
                parent.right = cur
            else:
                parent.left = cur
        return root

