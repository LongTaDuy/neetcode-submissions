# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same_tree(self, root1, root2):
        q1, q2 = deque([root1]), deque([root2])
        while q1 and q2:
            for _ in range(len(q1)):
                node1, node2 = q1.popleft(), q2.popleft()
                if node1 is None and node2 is None:
                    continue
                if node1 is None or node2 is None or node1.val != node2.val:
                    return False
                q1.append(node1.left)
                q2.append(node2.left)
                q1.append(node1.right)
                q2.append(node2.right)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            node = q.popleft()
            if self.same_tree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
    