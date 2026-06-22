class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i : [] for i in range(n)} # [cost, node]
        for i in range(len(points)):
            xi, yi = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                xj, yj = points[j][0], points[j][1]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        visit = set()
        res = 0
        minheap = [(0, 0)]
        while len(visit) < n:
            cost, node = heapq.heappop(minheap)
            if node in visit:
                continue
            res += cost
            visit.add(node)
            for neicost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(minheap, (neicost, nei))
        return res