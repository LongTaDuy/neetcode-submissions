# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def same_tree(self, root1, root2):
        queue1 = deque([root1])
        queue2 = deque([root2])
        while queue1 and queue2:
            node1 = queue1.popleft()
            node2 = queue2.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None  or node1.val != node2.val:
                return False
            queue1.append(node1.left)
            queue2.append(node2.left)
            queue1.append(node1.right)
            queue2.append(node2.right)
        return True

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if self.same_tree(node, subRoot):
                return True
            if node is not None:
                queue.append(node.left)
            if node is not None:
                queue.append(node.right)
        return False