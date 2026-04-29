# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue1 = deque([p])
        queue2 = deque([q])
        while queue1 and queue2:
            for i in range(len(queue1)):
                nodeP = queue1.popleft()
                nodeQ = queue2.popleft()
                
                if nodeP is None and nodeQ is None:
                    continue
                if nodeP is None or nodeQ is None or nodeP.val != nodeQ.val:
                    return False
                
                queue1.append(nodeP.left)
                queue2.append(nodeQ.left)
                queue1.append(nodeP.right)
                queue2.append(nodeQ.right)
        return True