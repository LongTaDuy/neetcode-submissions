class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    def find(self, n):
        n = self.parent[n]
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n
    def union(self, n1, n2):
        n1, n2 = self.find(n1), self.find(n2)
        if n1 == n2:
            return False
        if self.rank[n1] < self.rank[n2]:
            self.parent[n1] = n2
            self.rank[n2] += self.rank[n1]
        else:
            self.parent[n2] = n1
            self.rank[n1] += self.rank[n2]
        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        dsu = DSU(n)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)
                edges.append((dist, i, j))
        edges.sort()
        res = 0
        for dist, u, v in edges:
            if dsu.union(u, v):
                res += dist
        return res
