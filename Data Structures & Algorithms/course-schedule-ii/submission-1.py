class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]
        for src, dst in prerequisites:
            adj[src].append(dst)
            indegree[dst] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        res = []
        finish = 0
        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for i in adj[node]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        if finish != numCourses:
            return []
        return res[::-1]
        