class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        INF = float("inf")
        for s, d, p in flights:
            adj[s].append([d, p])
        dist = [[INF] * (k + 2) for i in range(n)]
        dist[src][0] = 0
        minheap = [[0, src, 0]]
        while minheap:
            p, s, check = heapq.heappop(minheap)
            if s == dst:
                return p
            if dist[s][check] < p or check == k + 1:
                continue
            for d1, p1 in adj[s]:
                dist[d1][check + 1] = min(dist[d1][check + 1], p + p1)
                heapq.heappush(minheap, [p + p1, d1, check + 1])
        return -1
