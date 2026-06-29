class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dist = [float('INF')] * n
        dist[src] = 0
        for _ in range(k + 1):
            tmp_dist = dist.copy()
            for u, v, w in flights:
                if dist[u] == float('INF'):
                    continue
                if dist[u] + w < tmp_dist[v]:
                    tmp_dist[v] = dist[u] + w
            dist = tmp_dist
        return -1 if dist[dst] == float("inf") else dist[dst]