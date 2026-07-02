class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(points)):
            xi, yi = points[i][0], points[i][1]
            for j in range(i + 1, len(points)):
                xj, yj = points[j][0], points[j][1]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append([j, dist])
                adj[j].append([i, dist])
        visited = set()
        minheap = [(0, 0)]
        res = 0
        while minheap and len(visited) < len(points):
            cost, point = heapq.heappop(minheap)
            if point in visited:
                continue
            visited.add(point)
            res += cost
            for nei, neicost in adj[point]:
                if nei not in visited:
                    heapq.heappush(minheap, (neicost, nei))   
        return res