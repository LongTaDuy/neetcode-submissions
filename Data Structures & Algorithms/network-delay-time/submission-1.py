class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([v, t])
        visited = set()
        minheap = [(0, k)]
        res = 0
        while minheap:
            t1, u1 = heapq.heappop(minheap)
            if u1 in visited:
                continue
            visited.add(u1)
            res = max(res, t1)
            for v2, t2 in adj[u1]:
                if v2 not in visited:
                    heapq.heappush(minheap, (t1 + t2, v2))
        return res if len(visited) == n else -1
